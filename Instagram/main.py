from selenium import webdriver
import time

users = ['midhun_k.o', 'arjunvinayan96']

browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver')

browser.maximize_window()

time.sleep(1)

for user in users:
    browser.get(f"https://www.instagram.com/{user}")
    time.sleep(1)
    post, followers, following = browser.find_elements_by_css_selector('.g47SY')
    bio = browser.find_element_by_css_selector('.-vDIg')
    with open(f"{user}.txt", "w", encoding="utf-8") as f:
        f.write(f"No of posts: {post.text}\nNo of followers: {followers.text}\nNo of following: {following.text}\n\nBio:\n{bio.text}")
    time.sleep(2)  

browser.close()


