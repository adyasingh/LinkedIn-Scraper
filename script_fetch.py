# import web driver
from selenium import webdriver
import time
timeout = time.time() + 60*10
# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('YOUR_PATH')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/login')
driver.maximize_window() 
driver.implicitly_wait(20) 

# locate email form by_class_name
username = driver.find_element_by_id('username')

# send_keys() to simulate key strokes
username.send_keys('YOUR_EMAIL')

# locate password form by_class_name
password = driver.find_element_by_id('password')

# send_keys() to simulate key strokes
password.send_keys('YOUR_PSWD')

# locate submit button by_class_name
log_in_button = driver.find_element_by_tag_name('button')

# .click() to mimic button click
log_in_button.click()

URL = 'URL_TO_SCRAPE'
driver.get(URL)

while True:
    if (time.time() > timeout):
        break
    try:
        morebtn = driver.find_element_by_xpath("//button[@data-control-name='more_comments']")
        morebtn.click()
    except:
        break
    
# print(driver.find_element_by_xpath("//a[contains(@href, 'mailto')]"))

f = open("temp.html", "w")
f.write(driver.page_source)
