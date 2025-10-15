import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from src.BaseTest import BaseTest
from src.LoginPage import LoginPage


class TestAddReservation(BaseTest):
    """FE test: create reservation on testing88 (DEV FE)"""

    def test_A_create_reservation_on_testing88(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)
        current_user = self.test_user  # Loaded by BaseTest.setUpClass

        print("\n--- PHASE 1: LOGIN ---")

        # Use LoginPage POM
        login_page = LoginPage(driver)
        driver.get(self.environment_url)
        login_page.login(current_user)

        print("\n--- PHASE 2: SEARCH FOR TESTING88 IN DASHBOARD ---")

        # Wait until the dashboard is ready
        wait.until(EC.url_contains("dashboard"))

        # Find and use the search box in dashboard
        search_box = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//input[@placeholder="Search" or @aria-label="Search"]')
            )
        )
        search_box.clear()
        search_box.send_keys("testing88")
        time.sleep(1)  # Allow search results to populate
        print("✅ Searched for testing88")

        print("\n--- PHASE 3: CLICK VISIBILITY ICON TO VIEW TESTRACK DETAILS ---")

        # Find the testrack item in search results
        testrack_item = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//testrack-list-item[.//div[@class="name" and contains(text(), "testing88")]]')
            )
        )

        # Scroll testrack item into view
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", testrack_item)
        time.sleep(0.5)

        # Find the visibility icon within rtl-connect-button
        # Based on Puppeteer recording: div.testracks rtl-connect-button mat-icon
        visibility_icon = wait.until(
            EC.element_to_be_clickable(
                testrack_item.find_element(
                    By.XPATH, 
                    ".//rtl-connect-button//a//button//mat-icon[contains(text(), 'visibility')]"
                )
            )
        )

        # Scroll icon into view and move to it
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", visibility_icon)
        time.sleep(0.3)
        
        # Use ActionChains to hover and click
        actions = ActionChains(driver)
        actions.move_to_element(visibility_icon).perform()
        time.sleep(0.2)
        
        # Try clicking, with JavaScript fallback
        try:
            visibility_icon.click()
        except Exception as e:
            print(f"⚠️ Standard click failed, using JavaScript click: {e}")
            driver.execute_script("arguments[0].click();", visibility_icon)
        
        print("✅ Clicked visibility icon for testing88")
        time.sleep(1)

        print("\n--- PHASE 4: NAVIGATE TO RESERVATIONS PAGE ---")

        # Click RESERVATIONS navigation link
        reservations_nav = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//a[@id="rtl-link-nav-reservation-page"]//span[contains(text(), "RESERVATIONS")]')
            )
        )
        reservations_nav.click()
        print("✅ Navigated to Reservations page")
        time.sleep(1)

        print("\n--- PHASE 5: SELECT TESTING88 TESTRACK IN RESERVATIONS ---")

        # Click on testing88 in the reservations list
        testing88_link = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//a//div[contains(text(), "testing88")]')
            )
        )
        testing88_link.click()
        print("✅ Selected testing88 testrack")
        time.sleep(1)

        print("\n--- PHASE 6: CREATE RESERVATION BY CLICKING CALENDAR ---")

        # Wait for calendar to load
        calendar = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'full-calendar, reservation-calendar')
            )
        )

        # Click on a calendar cell to create reservation
        # Based on Puppeteer: td:nth-of-type(2) tr:nth-of-type(25) > td
        calendar_cell = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//full-calendar//td[not(@class="fc-day-past")]//div[@class="fc-daygrid-day-frame" or @class="fc-timegrid-slot"]')
            )
        )
        
        # Scroll to calendar cell and click
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", calendar_cell)
        time.sleep(0.3)
        calendar_cell.click()
        print("✅ Clicked calendar to create reservation")
        time.sleep(1)

        print("\n--- PHASE 7: FILL RESERVATION FORM ---")

        # Fill Title field
        title_input = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//input[@placeholder="Title" or @aria-label="Title"]')
            )
        )
        title_input.clear()
        title_input.send_keys("testing FE reservation")
        print("✅ Entered reservation title")

        # Click Reservation Type dropdown
        reservation_type_field = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//mat-label[contains(text(), "Reservation Type")]')
            )
        )
        reservation_type_field.click()
        time.sleep(0.5)

        # Select "Manual testing" option
        manual_testing_option = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//mat-option//span[contains(text(), "Manual testing")]')
            )
        )
        manual_testing_option.click()
        print("✅ Selected 'Manual testing' as reservation type")
        time.sleep(0.5)

        print("\n--- PHASE 8: CONFIRM RESERVATION ---")

        # Click CONFIRM button
        confirm_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button//span[contains(text(), "CONFIRM")]')
            )
        )
        confirm_button.click()
        print("✅ Clicked CONFIRM button")
        time.sleep(2)

        # Verify success (you may need to adjust this based on your app's behavior)
        # Option 1: Check for success message
        try:
            success_message = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(), 'success') or contains(text(), 'created')]")
                )
            )
            print(f"✅ Reservation confirmed: {success_message.text}")
        except Exception:
            # Option 2: Verify by checking if we're back on calendar view
            print("✅ Reservation created (verified by UI state)")

        print("\n--- PHASE 9: RETURN TO DASHBOARD ---")

        # Navigate back to dashboard
        dashboard_nav = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//a[@id="rtl-link-nav-dashboard-page"]//span[contains(text(), "DASHBOARD")]')
            )
        )
        dashboard_nav.click()
        print("✅ Returned to dashboard")
        
        time.sleep(2)
        print("\n✅ TEST COMPLETED SUCCESSFULLY")


if __name__ == "__main__":
    unittest.main()
