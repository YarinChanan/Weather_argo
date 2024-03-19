from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import unittest

class TestWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        time.sleep(4)

    def test_positive(self):
        self.driver.get("http://127.0.0.1:8080")
        self.driver.implicitly_wait(1)

        text_box = self.driver.find_element(By.CLASS_NAME, value="form-control")
        submit_button = self.driver.find_element(By.CLASS_NAME, value="btn-primary")

        text_box.send_keys("London")
        submit_button.click()

        title_element = self.driver.find_element(By.NAME, value="header")
        self.assertEqual("London, England, United Kingdom", title_element.text)

        time.sleep(4)

    def test_negative(self):
        self.driver.get("http://127.0.0.1:8080")
        self.driver.implicitly_wait(1)

        text_box = self.driver.find_element(By.CLASS_NAME, value="form-control")
        submit_button = self.driver.find_element(By.CLASS_NAME, value="btn-primary")

        text_box.send_keys("000000000")
        submit_button.click()

        title_element = self.driver.find_element(By.NAME, value="error-head")
        self.assertEqual("Error!", title_element.text)

        time.sleep(4)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
