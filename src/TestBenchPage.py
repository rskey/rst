# src/TestBenchPage.py
from pyautogui import click
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest


# ============================================================
# DEBUG CONFIGURATION
# ============================================================
# Adjust this value to control pause duration between steps
# - Set to 0 for normal test execution
# - Set to 2-3 for debugging and visual observation
# - Set to 5+ for detailed step-by-step inspection
DEBUG_DELAY = 2  # seconds
# ============================================================


class TB_Page:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # --- LOCATORS ---
    
    # Generic locators
    TEST_BENCHES_TAB = (By.XPATH, '//span[@class="mdc-tab__text-label"]//h2[text()="Test Benches"]')
    RELAYS_TAB = (By.XPATH, '//span[@class="mdc-tab__content"]//span[@class="mdc-tab__text-label" and contains(text(), "Relays")]')
    SAVE_BUTTON = (By.XPATH, "//span[@class='mdc-button__label']//span[text()='SAVE']")
    UPDATE_SUCCESS_TOAST = (By.XPATH, "//*[contains(text(), 'Successfully updated Testrack')]")
    
    # Relay-specific locators
    ADD_FUNCTIONALITY_BUTTON = (By.XPATH, "//button[contains(@class, 'add-functionality') and contains(@mattooltip, 'Add new relay functionality')]")
    # Generic mat-select locator (may need to be more specific if issues arise)
    FUNCTIONALITY_DROPDOWN = (By.XPATH, '//*[contains(@id, "mat-select-")]') 
    POSITION_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='position']")
    
    # Test Bench Creation/Deletion locators
    CREATE_TB_BUTTON = (By.ID, "rtl-button-create-test-bench")
    TB_TITLE_INPUT = (By.ID, "rtl-input-general-name") 
    TB_MAKE_DROPDOWN = (By.ID, "rtl-button-general-make")
    TB_PROJECT_MODEL_DROPDOWN = (By.ID, "rtl-button-general-model")
    TB_EL_ARCHITECTURE_DROPDOWN = (By.ID, "rtl-button-general-architecture")
    CREATE_TB_CONFIRM_BUTTON = (By.XPATH, "//span[@class='mdc-button__label']//span[normalize-space()='CREATE']")
    TB_CREATE_SUCCESS_TOAST = (By.XPATH, "//*[contains(text(), 'Successfully created Testrack')]")
    TB_DELETE_BUTTON_ID = "btn-delete-test-bench"
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[contains(@class, 'confirm-button') and .//span[text()='CONFIRM']]")
    TB_DELETE_SUCCESS_TOAST = (By.XPATH, "//*[contains(text(), 'Successfully deleted') or contains(text(), 'deleted successfully')]")
    
    
    # --- ACTIONS ---
    
    def _click_test_benches_tab(self):
        """Internal method to handle the specific, reliable click on the Test Benches tab."""
        print("Navigating to Test Benches tab...")
        
        test_benches_tab = self.wait.until(
            EC.visibility_of_element_located(self.TEST_BENCHES_TAB)
        )
        self.wait.until(EC.element_to_be_clickable(self.TEST_BENCHES_TAB))
        time.sleep(0.2)  # Stabilizing delay
        test_benches_tab.click()
        print("✅ Clicked Test Benches tab")
        time.sleep(DEBUG_DELAY)
    
    def navigate_to_test_bench_details(self, project_name="Regress Testing - relays add autotest", tb_name="testing88"):
        """Navigates to a specific Test Bench's details page."""
        
        # Click Test Benches tab (REUSE HELPER)
        self._click_test_benches_tab()
        
        # Locate row and click DNS icon
        row_xpath = f'//mat-row[.//mat-cell[contains(text(), "{tb_name}")]]'
        row_element = self.driver.find_element(By.XPATH, row_xpath)

        icon_element = row_element.find_element(By.XPATH, './/mat-cell//mat-icon[text()="dns"]')
        icon_element.click() 
        print(f'✅ Clicked on the TB DNS icon for {tb_name}')
        time.sleep(DEBUG_DELAY)


    def add_relay_functionality(self, functionality_name, position="1"):
        """Adds a new relay functionality and position."""
        
        print(f"Adding relay: {functionality_name} at position {position}...")
        
        # 1. Click Relays tab
        self.wait.until(EC.element_to_be_clickable(self.RELAYS_TAB)).click()
        print("✅ Clicked Relays tab")
        time.sleep(DEBUG_DELAY)

        # 2. Click "ADD FUNCTIONALITY" button
        self.wait.until(EC.element_to_be_clickable(self.ADD_FUNCTIONALITY_BUTTON)).click()
        print("✅ Clicked ADD FUNCTIONALITY button")
        time.sleep(DEBUG_DELAY)

        # 3. Click Drop down
        self.wait.until(EC.element_to_be_clickable(self.FUNCTIONALITY_DROPDOWN)).click()
        print("✅ Relay list dropdown opened")
        time.sleep(DEBUG_DELAY)

        # 4. Select the functionality option
        option_xpath = f"//mat-option[starts-with(@id, 'mat-option-') and contains(., '{functionality_name}')]"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath))).click()
        print(f"✅ Selected {functionality_name} from dropdown")
        time.sleep(DEBUG_DELAY)

        # 5. Input Position
        position_input = self.wait.until(EC.visibility_of_element_located(self.POSITION_INPUT))
        position_input.clear()
        position_input.send_keys(position)
        print(f"✅ Entered position: {position}")
        time.sleep(DEBUG_DELAY)
        
        # 6. Click SAVE
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        print("✅ Clicked SAVE button")
        time.sleep(DEBUG_DELAY)
        
        self.wait.until(EC.presence_of_element_located(self.UPDATE_SUCCESS_TOAST))
        print("✅ Relay functionality added successfully")

    def delete_all_relays(self):
        """Deletes all relays by clicking the 'close' icon on the relay tab and saving."""
        
        print("Starting relay deletion...")
        
        # 1. Click Relays tab
        self.wait.until(EC.element_to_be_clickable(self.RELAYS_TAB)).click()
        print("✅ Clicked Relays tab")
        time.sleep(DEBUG_DELAY)

        # 2. Locate and click the close icon
        close_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//mat-icon[text()='close']]"))
        )
        close_button.click()
        print("✅ Clicked close icon to remove relay")
        time.sleep(DEBUG_DELAY)

        # 3. Click SAVE button
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        print("✅ Clicked SAVE button")
        time.sleep(DEBUG_DELAY)

        # 4. Wait for the success message
        self.wait.until(EC.presence_of_element_located(self.UPDATE_SUCCESS_TOAST))
        print("✅ Relay successfully deleted and changes saved")
        
    def check_relay_on_dashboard(self, project_name, tb_name, relay_name):
        """Checks for the presence of a relay button on the dashboard view."""
        
        # 1. Locate and expand the project panel
        panel_header_xpath = f"//mat-expansion-panel-header[.//mat-panel-title[text()='{project_name}']]"
        panel_header = self.wait.until(EC.element_to_be_clickable((By.XPATH, panel_header_xpath)))
        
        # Click the indicator to expand
        indicator = panel_header.find_element(By.XPATH, ".//span[contains(@class, 'mat-expansion-indicator')]")
        indicator.click()
        print(f"✅ Expanded project panel: {project_name}")
        time.sleep(DEBUG_DELAY)

        # 2. Locate the test rack box
        testrack_xpath = f'//testrack-list-item[.//div[@class="name" and contains(text(), "{tb_name}")]]'
        testrack_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, testrack_xpath)))
        
        # 3. Click the visibility icon to view details
        visibility_icon = testrack_box.find_element(By.XPATH, ".//mat-icon[text()='visibility']")
        visibility_icon.click()
        print(f"✅ Clicked visibility icon for {tb_name}")
        time.sleep(DEBUG_DELAY)

        # 4. Locate the relay button by its text
        relay_button_xpath = f".//button[contains(@class, 'mat-ripple') and text()='{relay_name}']"
        button = self.driver.find_element(By.XPATH, relay_button_xpath)
        
        assert button is not None, f"Relay button '{relay_name}' not found on dashboard view."
        print(f"✅ Relay '{relay_name}' button visible on dashboard")
        
        
    def create_test_bench(self, project_name, tb_name):
        """
        Navigates to the Test Benches tab and creates a new Test Bench.
        Assumes we are already on the Project Edit screen.
        """
        print(f"\n--- Creating new Test Bench: {tb_name} ---")
        
        # 1. Click Test Benches tab
        self._click_test_benches_tab()
        
        # 2. Click CREATE TEST BENCH button
        self.wait.until(EC.element_to_be_clickable(self.CREATE_TB_BUTTON)).click()
        print("✅ Clicked CREATE TEST BENCH button")
        time.sleep(DEBUG_DELAY)
        
        # 3. Wait for and input the Title
        title_input = self.wait.until(EC.visibility_of_element_located(self.TB_TITLE_INPUT))
        title_input.send_keys(tb_name)
        print(f"✅ Title input filled with '{tb_name}'")
        time.sleep(DEBUG_DELAY)
        
        # 4. Select 'Make' = Bugatti
        make_dropdown = self.wait.until(EC.element_to_be_clickable(self.TB_MAKE_DROPDOWN))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", make_dropdown)
        time.sleep(0.3)

        try:
            make_dropdown.click()
        except Exception as e:
            print(f"⚠️ Dropdown click failed: {e} - Using JS click")
            self.driver.execute_script("arguments[0].click();", make_dropdown)
        print("✅ Opened 'Make' dropdown")
        time.sleep(DEBUG_DELAY)

        option_xpath = "//mat-option[starts-with(@id, 'mat-option-') and contains(., 'Bugatti')]"
        bugatti_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        bugatti_option.click()
        print("✅ Selected 'Bugatti' from Make dropdown")
        time.sleep(DEBUG_DELAY)
        
        # 5. Select Project Model = Chiron
        self.wait.until(EC.element_to_be_clickable(self.TB_PROJECT_MODEL_DROPDOWN)).click()
        print("✅ Project model dropdown opened")
        time.sleep(DEBUG_DELAY)
        
        option_xpath = "//mat-option[starts-with(@id, 'mat-option-') and contains(., 'Chiron')]"
        chiron_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        chiron_option.click()
        print("✅ Selected 'Chiron' from Project Model dropdown")
        time.sleep(DEBUG_DELAY)

        # 6. Select El Architecture = 2007+
        self.wait.until(EC.element_to_be_clickable(self.TB_EL_ARCHITECTURE_DROPDOWN)).click()
        print("✅ Element architecture dropdown opened")
        time.sleep(DEBUG_DELAY)

        option_xpath = "//mat-option[starts-with(@id, 'mat-option-') and contains(., '2007+')]"
        element_architecture_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        element_architecture_option.click()
        print("✅ Selected '2007+' from El Architecture dropdown")
        time.sleep(DEBUG_DELAY)

        # 7. Click CREATE button
        self.wait.until(EC.element_to_be_clickable(self.CREATE_TB_CONFIRM_BUTTON)).click()
        print("✅ Clicked CREATE confirmation button")
        time.sleep(DEBUG_DELAY)
        
        # 8. Wait for success message
        self.wait.until(EC.presence_of_element_located(self.TB_CREATE_SUCCESS_TOAST))
        print(f"✅ Test Bench '{tb_name}' created successfully")
        time.sleep(DEBUG_DELAY)


    def verify_test_bench_exists(self, tb_name):
        """Checks if a Test Bench is visible in the list on the Test Benches tab."""
        print(f"\n--- Verifying Test Bench: {tb_name} ---")
        
        row_xpath = f'//mat-row[.//mat-cell[contains(text(), "{tb_name}")]]'
        row_element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, row_xpath)),
            message=f"Test Bench '{tb_name}' was not found in the list."
        )
        
        if row_element:
            print(f"✅ Test Bench '{tb_name}' verification successful")
            time.sleep(DEBUG_DELAY)
        else:
            raise AssertionError(f"Test Bench '{tb_name}' was not found in the list.")
         
         
    def delete_test_bench(self, tb_name):
        """
        Locates a specific Test Bench row by title, clicks the delete button within that row,
        and confirms the action in the dialog.
        Assumes we are already on the Project Edit screen.
        """
        print(f"\n--- Deleting Test Bench: {tb_name} ---")

        # 1. Ensure we are on the Test Benches tab
        self._click_test_benches_tab()
        
        # 2. Locate the row containing the specific Test Bench name
        row_xpath = f'//mat-row[.//mat-cell[contains(text(), "{tb_name}")]]'
        
        try:
            row_element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, row_xpath)),
                message=f"Row for Test Bench '{tb_name}' not found for deletion."
            )
            print(f"✅ Found Test Bench row: {tb_name}")
            time.sleep(DEBUG_DELAY)
        except Exception:
            print(f"⚠️ TB '{tb_name}' not found in the list. Assuming already deleted or creation failed.")
            return  # Exit gracefully if TB isn't found
            
        # 3. Find and click the Delete button within that specific row
        delete_button_xpath = f'{row_xpath}//button[@id="{self.TB_DELETE_BUTTON_ID}"]'
        
        delete_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, delete_button_xpath)),
            message=f"Delete button for TB '{tb_name}' not clickable."
        )
        
        # Scroll delete button into view
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", delete_button)
        time.sleep(0.3)
        print(f"✅ Delete button scrolled into view")
        time.sleep(DEBUG_DELAY)

        # Click with JavaScript fallback
        try:
            delete_button.click()
        except Exception as e:
            print(f"⚠️ Standard click failed: {e} - Using JS click")
            self.driver.execute_script("arguments[0].click();", delete_button)
        
        print(f"✅ Clicked delete button for TB '{tb_name}'")
        time.sleep(DEBUG_DELAY)

        # 4. Handle the CONFIRM dialog
        confirm_button = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BUTTON))
        confirm_button.click()
        print("✅ Clicked 'CONFIRM' button in the delete dialog")
        time.sleep(DEBUG_DELAY)
        
        # 5. Wait for success message
        try:
            self.wait.until(EC.presence_of_element_located(self.TB_DELETE_SUCCESS_TOAST))
            print(f"✅ Delete success message appeared")
        except Exception:
            print("⚠️ Success message not found, but continuing...")
        
        time.sleep(DEBUG_DELAY)
        
        # 6. Verify the table row is gone
        try:
            self.wait.until(EC.staleness_of(row_element))
            print(f"✅ Test Bench '{tb_name}' removed from the list")
        except Exception:
            print(f"⚠️ Row still visible, but delete may have succeeded")
        
        time.sleep(DEBUG_DELAY)
        print(f"✅ Deletion completed for Test Bench '{tb_name}'")
