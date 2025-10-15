from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest


def test_click_visibility_icon():
    """Test clicking the visibility icon for a testrack item."""
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    try:
        # Navigate to the page (replace with actual URL)
        driver.get("YOUR_URL_HERE")
        
        # Find testrack item (testing88)
        testrack_item = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//testrack-list-item[.//div[@class="name" and contains(text(), "testing88")]]')
            )
        )
        
        # Find the visibility icon within the testrack item
        visibility_icon = testrack_item.find_element(By.XPATH, ".//mat-icon[text()='visibility']")
        
        # Scroll the element into view
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", visibility_icon)
        
        # Wait a moment for any animations to complete
        wait.until(EC.element_to_be_clickable(visibility_icon))
        
        # Move to the element to ensure it's interactable
        actions = ActionChains(driver)
        actions.move_to_element(visibility_icon).perform()
        
        # Try clicking using ActionChains first (more reliable for complex UI)
        try:
            actions.click(visibility_icon).perform()
        except Exception as e:
            # Fallback to JavaScript click if ActionChains fails
            print(f"ActionChains click failed, using JavaScript click: {e}")
            driver.execute_script("arguments[0].click();", visibility_icon)
        
        # Verify the click worked (add your verification logic here)
        # For example, wait for a detail page or modal to appear
        
    finally:
        driver.quit()


if __name__ == "__main__":
    test_click_visibility_icon()
