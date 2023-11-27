from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(0)
driver.get("https://www.spicejet.com/")
time.sleep(10)
ele = driver.find_element(By.CLASS_NAME, "css-76zvg2 r-jwli3a r-ubezar r-16dba41 r-1pzd9i8")
actionChains = ActionChains(driver)
actionChains.move_to_element(ele).perform()
ele_ourprogram = driver.find_element(By.CLASS_NAME, "css-76zvg2 r-homxoj r-ubezar")
actionChains.move_to_element(ele_ourprogram).perform()