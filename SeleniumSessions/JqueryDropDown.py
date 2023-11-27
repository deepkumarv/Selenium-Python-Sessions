import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

# driver=webdriver.Chrome(ChromeDriverManager().install())
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.find_element(By.ID, "justAnInputBox").click()
time.sleep(3)
dropdown_elements=driver.find_elements(By.CSS_SELECTOR,'span.comboTreeItemTitle')
for ele in dropdown_elements:
    if(ele.text=="choice 1"):
        ele.click()
        break

time.sleep(5)
driver.quit()
