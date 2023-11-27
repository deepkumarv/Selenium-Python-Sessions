import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="/Users/vaku5928/Downloads/chromedriver")
#driver = webdriver.firefox()
driver.implicitly_wait(5)
driver.get("http://www.google.com")
print(driver.title)
driver.find_element(By.NAME, 'q').send_keys("Automation tasks")

#body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.UUbT9 > div.aajZCb > div.mkHrUc > ul.erkvQe > div > ul > li:nth-child(4) > div > div.pcTkSc > div.wM6W7d > span > b
search_suggestions_list_elements=driver.find_elements(By.CSS_SELECTOR, 'ul.G43f7e li div.wM6W7d')
print(search_suggestions_list_elements.__len__())
print(len(search_suggestions_list_elements))
for ele in search_suggestions_list_elements:
    print(ele.text)
    if(ele.text=='automation tasks with python'):
        ele.click()
        break
time.sleep(5)
#driver = webdriver.Chrome(executable_path="/Users/vaku5928/Downloads/chromedriver")
#driver.implicitly_wait(5)
#driver.close()
driver.get("https://www.amazon.in/")
a_search_bar=driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')
a_search_bar.send_keys("laptop")
a_search_button=driver.find_element(By.CSS_SELECTOR, "input[id='nav-search-submit-button']")
a_search_button.click()
a_featured_button_0 = driver.find_element(By.CSS_SELECTOR, 'span.a-dropdown-prompt')
a_featured_button_0.click()
a_featured_button_1 = driver.find_element(By.XPATH, "//a[@id='s-result-sort-select_2']")
# select_1 = Select(a_featured_button_1);ƒ
# a_featured_button_1.click()
a_featured_button_1.click()
time.sleep(10)
driver.quit()