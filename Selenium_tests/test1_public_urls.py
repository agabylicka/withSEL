from selenium import webdriver


def test_google():
    # Get the driver
    driver = webdriver.Chrome()
    # Maximize window
    driver.maximize_window()
    # Get the URL
    driver.get("https://www.lambdatest.com/certifications/selenium-python-101")
    # Check response
    print(driver.title)

