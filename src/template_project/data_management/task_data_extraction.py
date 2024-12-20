"Task for web scraping recycling and composting facilities"

from selenium import webdriver
from eaibgap.config import DRIVER_PATH

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# Navigate to the URL
driver.get('https://google.com')

# It's a good practice to close the browser when done
driver.quit()