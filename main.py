import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument('--headless')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(path=os.environ.get("CHROMEDRIVER_DOWNLOAD_PATH")).install(), executable_path=os.environ.get("CHROMEDRIVER_PATH")), options=options,)
  
driver.get('https://sssinstagram.com/')
driver.save_screenshot('screenshot.png')

driver.quit()