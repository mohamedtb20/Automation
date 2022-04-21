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
# opening the driver and enter to our linkedin
# open the linkedin website waiting 2 seconds and then login
driver.get('https://www.linkedin.com')
time.sleep(2)
# we select the part that we will fill it and interact with
# will go to the driver in linkdin page and will find the username and the password field to fill
# we locate our element by xpath
username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")
# filling the informations
username.send_keys('your_email')
password.send_keys('your_password')
time.sleep(2)
# click on submit
submit = driver.find_element_by_xpath("//button[@type='submit']").click()
# giving our driver the link that we will interract with i mean the list which we want to connect with
driver.get(
    "https://www.linkedin.com/search/results/people/?keywords=cyber%20security&network=%5B%22S%22%5D&origin=FACETED_SEARCH&sid=2-u")
time.sleep(2)


# we define a function which give us the possibility to repeat the same action a lot of times
def repeat():
    # we define a list of a web element definded by tag name : button
    all_buttons: list[WebElement] = driver.find_elements_by_tag_name("button")
    # our button connect is the same type of all_buttons with a text "Connect"
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]
    for btn in connect_buttons:
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(2)
        # we define and click on other button which appear when clicking on connect button
        send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
        driver.execute_script("arguments[0].click();", send)
        time.sleep(2)
        close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
        driver.execute_script("arguments[0].click();", close)
        time.sleep(10)
    # in the case of the existence of just follow button not a connect button
    follow_buttons = [btn2 for btn2 in all_buttons if btn2.text == "Follow"]
    for btn2 in follow_buttons:
        driver.execute_script("arguments[0].click();", btn2)
        time.sleep(10)
    # we scroll down to find the element that permit us to skipe to the next page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
    # the next page button
    Next_button = driver.find_element_by_xpath("//button[@aria-label='Next']")
    driver.execute_script("arguments[0].click();", Next_button)
    time.sleep(5)


# we can a fix a time to do that or doing like what i do by execute until not finiding result
while True:
    repeat()
