import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestBackend:

    def setup_method(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def test_add(self):
        self.driver.get('http://localhost:5000/add/1&2')
        assert "Add 1 and 2. Got 3!" in self.driver.find_element(By.TAG_NAME, "body").text

    def test_multiply(self):
        self.driver.get('http://localhost:5000/multiply/2&2')
        assert "Multiply 2 and 2. Got 4!" in self.driver.find_element(By.TAG_NAME, "body").text

    def test_divide(self):
        self.driver.get('http://localhost:5000/divide/10&2')
        assert "Divide 10 and 2. Got 5.0!" in self.driver.find_element(By.TAG_NAME, "body").text

    def test_subtract(self):
        self.driver.get('http://localhost:5000/subtract/9&2')
        assert "Subtract 9 and 2. Got 7!" in self.driver.find_element(By.TAG_NAME, "body").text

    def teardown_method(self):
        if self.driver:
            self.driver.quit()