# tests/test_login.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import BASE_URL, USERNAME, PASSWORD

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_successful_login(self):
        driver = self.driver
        driver.get(BASE_URL)
        
        driver.find_element(By.ID, "user-name").send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "login-button").click()

        self.assertIn("inventory.html", driver.current_url)

    def test_unsuccessful_login_empty_credentials(self):
        driver = self.driver
        driver.get(BASE_URL)
        
        driver.find_element(By.ID, "login-button").click()
        
        error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        self.assertTrue(error_message.is_displayed())
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
