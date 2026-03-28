"""Unit tests for src/xlsx_reader.py."""

import os
import sys
import tempfile
import unittest

import openpyxl

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.xlsx_reader import XlsxReader


def _make_workbook(sheets):
    """Create an in-memory workbook and save it to a temp file.

    ``sheets`` is a list of ``(name, [rows])`` pairs where each row is a tuple
    of cell values.  Returns the path to the saved file.
    """
    wb = openpyxl.Workbook()
    # Remove the default sheet
    wb.remove(wb.active)
    for name, rows in sheets:
        ws = wb.create_sheet(title=name)
        for row in rows:
            ws.append(list(row))
    fd, path = tempfile.mkstemp(suffix=".xlsx")
    os.close(fd)
    wb.save(path)
    return path


class TestXlsxReaderContextManager(unittest.TestCase):
    def setUp(self):
        self.path = _make_workbook([
            ("Data", [("name", "age"), ("Alice", 30), ("Bob", 25)]),
        ])

    def tearDown(self):
        os.remove(self.path)

    def test_context_manager_reads_rows(self):
        with XlsxReader(self.path) as reader:
            rows = reader.read_sheet()
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0], {"name": "Alice", "age": 30})
        self.assertEqual(rows[1], {"name": "Bob", "age": 25})

    def test_workbook_closed_after_context(self):
        with XlsxReader(self.path) as reader:
            pass
        self.assertIsNone(reader._workbook)


class TestXlsxReaderManualLifecycle(unittest.TestCase):
    def setUp(self):
        self.path = _make_workbook([
            ("Sheet1", [("x",), (1,), (2,)]),
        ])

    def tearDown(self):
        os.remove(self.path)

    def test_open_close(self):
        reader = XlsxReader(self.path)
        reader.open()
        self.assertIsNotNone(reader._workbook)
        rows = reader.read_sheet()
        self.assertEqual(rows, [{"x": 1}, {"x": 2}])
        reader.close()
        self.assertIsNone(reader._workbook)

    def test_requires_open(self):
        reader = XlsxReader(self.path)
        with self.assertRaises(RuntimeError):
            reader.read_sheet()


class TestXlsxReaderMultipleSheets(unittest.TestCase):
    def setUp(self):
        self.path = _make_workbook([
            ("Animals", [("animal", "legs"), ("cat", 4), ("bird", 2)]),
            ("Colors", [("color",), ("red",), ("blue",)]),
        ])

    def tearDown(self):
        os.remove(self.path)

    def test_get_sheet_names(self):
        with XlsxReader(self.path) as reader:
            names = reader.get_sheet_names()
        self.assertEqual(names, ["Animals", "Colors"])

    def test_read_named_sheet(self):
        with XlsxReader(self.path) as reader:
            rows = reader.read_sheet("Colors")
        self.assertEqual(rows, [{"color": "red"}, {"color": "blue"}])

    def test_read_all_sheets(self):
        with XlsxReader(self.path) as reader:
            data = reader.read_all_sheets()
        self.assertIn("Animals", data)
        self.assertIn("Colors", data)
        self.assertEqual(len(data["Animals"]), 2)
        self.assertEqual(len(data["Colors"]), 2)


class TestXlsxReaderEdgeCases(unittest.TestCase):
    def test_empty_sheet_returns_empty_list(self):
        path = _make_workbook([("Empty", [])])
        try:
            with XlsxReader(path) as reader:
                rows = reader.read_sheet()
            self.assertEqual(rows, [])
        finally:
            os.remove(path)

    def test_header_only_returns_empty_list(self):
        path = _make_workbook([("Headers", [("col1", "col2")])])
        try:
            with XlsxReader(path) as reader:
                rows = reader.read_sheet()
            self.assertEqual(rows, [])
        finally:
            os.remove(path)

    def test_none_cell_values_preserved(self):
        path = _make_workbook([("Data", [("a", "b"), (1, None)])])
        try:
            with XlsxReader(path) as reader:
                rows = reader.read_sheet()
            self.assertEqual(rows[0]["b"], None)
        finally:
            os.remove(path)


if __name__ == "__main__":
    unittest.main()
