from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://localhost:4200/")
driver.maximize_window()
driver.implicitly_wait(5)

my_element = driver.find_element(By.ID, 'CreateHeroButton')
my_element.click()

time.sleep(5)
driver.quit()