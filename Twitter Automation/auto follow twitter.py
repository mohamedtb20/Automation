#Twitter auto Follow

import time
# selenium is an automation library
# webdriver is the path to the webbrowser which we can work with
from selenium import webdriver
# we define chrome with webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

# we give our driver chrome as a webdriver
s = Service('C:\\Users\\DELL\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe')
driver: WebDriver = webdriver.Chrome(service=s)
# opening the driver and enter to our twitter
# open the twitter website waiting 2 seconds and then login
driver.get('https://twitter.com/i/flow/login')
time.sleep(2)
# we select the part that we will fill it and interact with
# will go to the driver in twitter page and will find the username and the password field to fill
# we locate our element by name
username = driver.find_element_by_name("text")
# filling the informations
username.send_keys('your_username')
time.sleep(5)
# click on Next button we use the css selector with the class
Next = driver.find_element_by_css_selector(
    'div.css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu')
Next.click()
time.sleep(2)
password = driver.find_element_by_name("password")
password.send_keys('your_password')
time.sleep(2)
# click on log in
log = driver.find_element_by_css_selector('div.css-1dbjc4n.r-pw2am6')
log.click()
#our url of the list of X that we want to follow
driver.get(
    "https://twitter.com/search?q=ceo%20startup&src=typed_query&f=user")
time.sleep(5)


def repeat():
    # we define a list of a web element definded by tag name : button
    all_buttons: list[WebElement] = driver.find_elements_by_xpath("//button[@role='button']")
    #we define the follow button
    follow_buttons = [btn2 for btn2 in all_buttons if btn2.text == "Follow"]
    for btn2 in follow_buttons:
        driver.execute_script("arguments[0].click();", btn2)
        time.sleep(10)

# we can a fix a time to do that or doing like what i do by execute until not finiding result

while True:
    repeat()
