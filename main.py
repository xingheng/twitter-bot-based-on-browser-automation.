#! /usr/bin/env python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def main():
    # Set up Chrome options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run in headless mode if you don't need a GUI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # Add proxy settings
    # chrome_options.add_argument('--proxy-server=http://127.0.0.1:7890')

    # Get the ChromeDriver path
    # driver_path = ChromeDriverManager().install()
    driver_path = "/usr/local/bin/chromedriver"
    print(f"ChromeDriver path: {driver_path}")
    # Create service with explicit path
    service = Service(executable_path=driver_path)

    # Set up the WebDriver with the service
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open x.com timeline
        driver.get("https://x.com")

        # Wait for the page to load
        driver.implicitly_wait(10)  # seconds

        # You can add more interactions here if needed

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
