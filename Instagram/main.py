from selenium import webdriver
import time

users = ['midhun_k.o', 'arjunvinayan96']

browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver')

browser.maximize_window()

time.sleep(1)

for user in users:
    browser.get(f"https://www.instagram.com/{user}")
    post, followers, following = browser.find_element_by_css_selector('.g47SY')

