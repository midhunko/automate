from selenium import webdriver

import time

browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver')

browser.get('https://www.google.com')

time.sleep(1)

search_box = browser.find_element_by_name('q')

search_box.send_keys('Nokia 5.3 India Launch')

time.sleep(1)

search_btn = browser.find_element_by_class_name('gNO89b')

search_btn.click()

