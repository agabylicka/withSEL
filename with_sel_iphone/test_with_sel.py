from selenium import webdriver
from selenium.webdriver.common.by import By


def test_with_sel_iphone():
    # Creates a new instance of the Chrome driver
    driver = webdriver.Chrome()
    # window maximize
    driver.maximize_window()
    # Loads URL to memory
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")
    # Search Iphone in Search bar
    driver.find_element(By.XPATH, "//input[@placeholder='Search For Products']") \
        .send_keys('IPhone')
    # Click search button
    driver.find_element(By.XPATH, "//button[text()='Search']").click()
    # Assert element present of first found item's amount
    assert (driver.find_element(By.XPATH, "(//span[text()='$123.20'])[1]") is not None)
