# tests/test_checkout.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import BASE_URL, USERNAME, PASSWORD

class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_checkout_first_product(self):
        driver = self.driver
        driver.get(BASE_URL)
        
        driver.find_element(By.ID, "user-name").send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "login-button").click()
        
        driver.find_element(By.XPATH, "//button[@name='add-to-cart-sauce-labs-backpack']").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
        
        driver.find_element(By.ID, "first-name").send_keys("Test")
        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        
        driver.find_element(By.ID, "finish").click()
        
        success_message = driver.find_element(By.XPATH, "//h2[@class='complete-header']")
        self.assertTrue(success_message.is_displayed())

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
