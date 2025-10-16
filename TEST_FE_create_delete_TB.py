import unittest
import time
from datetime import datetime

# --- FRAMEWORK IMPORTS ---
from src.BaseTest import BaseTest 
from src.LoginPage import LoginPage 
from src.TestBenchPage import TB_Page
from src.FE_helper import click_edit_button_by_title


# ============================================================
# DEBUG CONFIGURATION
# ============================================================
# Adjust this value to control pause duration between steps
# - Set to 0 for normal test execution
# - Set to 2-3 for debugging and visual observation
# - Set to 5+ for detailed step-by-step inspection
DEBUG_DELAY = 2  # seconds
# ============================================================


class TestCreateTestBench(BaseTest):
    """FE test: Create and delete a Test Bench"""
    
    # Configuration
    USER_KEY = "super_admin" 
    
    # Test Constants
    PROJECT_NAME = "Regress Testing - relays add autotest"
    
    def setUp(self):
        super().setUp()
        
        # Generate a unique name for the Test Bench
        timestamp = datetime.now().strftime("%m%d%H%M%S")
        self.TB_NAME = f"NewTB_{timestamp}"
        print(f"\n{'='*60}")
        print(f"Test Bench Name: {self.TB_NAME}")
        print(f"{'='*60}")
        
    def test_A_create_and_verify_test_bench(self):
        """Tests successful login, creation of a unique test bench, and verification."""
        
        # Initialize Page Objects
        login_page = LoginPage(self.driver)
        tb_page = TB_Page(self.driver)
        current_user = self.test_user 
        
        print("\n--- PHASE 1: LOGIN ---")
        self.driver.get(self.environment_url)
        login_page.login(current_user)
        print('✅ Login successful and on Dashboard')
        time.sleep(DEBUG_DELAY)
        
        
        print("\n--- PHASE 2: NAVIGATE TO PROJECT EDIT SCREEN ---")
        click_edit_button_by_title(self.driver, self.PROJECT_NAME)
        print(f"✅ Navigated to edit screen for project: {self.PROJECT_NAME}")
        time.sleep(DEBUG_DELAY)
        
        
        print("\n--- PHASE 3: CREATE TEST BENCH ---")
        tb_page.create_test_bench(self.PROJECT_NAME, self.TB_NAME)
        time.sleep(DEBUG_DELAY)
        
        
        print("\n--- PHASE 4: VERIFICATION ---")
        # Verify the new TB exists in the list
        tb_page.verify_test_bench_exists(self.TB_NAME)
        time.sleep(DEBUG_DELAY)
        
        print("\n✅ TEST COMPLETED SUCCESSFULLY - Test Bench created and verified")
        time.sleep(DEBUG_DELAY)

    def tearDown(self):
        """Cleanup function to delete the created Test Bench via UI."""
        if hasattr(self, 'TB_NAME') and self.TB_NAME:
            print(f"\n{'='*60}")
            print(f"CLEANUP: Deleting Test Bench '{self.TB_NAME}' via UI")
            print(f"{'='*60}")

            try:
                # Initialize TB_Page for cleanup
                tb_page = TB_Page(self.driver)
                time.sleep(DEBUG_DELAY)
                
                # Perform the deletion
                tb_page.delete_test_bench(self.TB_NAME)
                
                print(f"\n✅ CLEANUP SUCCESSFUL: Test Bench '{self.TB_NAME}' deleted")
                time.sleep(DEBUG_DELAY)

            except Exception as e:
                # Catch any error during cleanup and print a warning
                print(f"\n❌ CLEANUP FAILED for TB '{self.TB_NAME}': {e}")
                import traceback
                traceback.print_exc()

        # Call parent tearDown
        super().tearDown()


if __name__ == "__main__":
    unittest.main()
