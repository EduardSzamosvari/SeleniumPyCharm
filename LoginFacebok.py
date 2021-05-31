import time

from selenium import webdriver
from config.settings import CHROME_PATH

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options,executable_path=CHROME_PATH)

class Facebook():

    def login(self):
        driver.get("https://www.facebook.com/")
        acceptAll= driver.find_element_by_xpath("//button[normalize-space()='Accept All']")
        acceptAll.click()

        email = driver.find_element_by_xpath("//input[@id='email']")
        email.send_keys("email@yahoo.com")

        password = driver.find_element_by_xpath("//input[@id='pass']")
        password.send_keys("parola")

        LogIn = driver.find_element_by_xpath("//button[normalize-space()='Log In']")
        LogIn.click()

        time.sleep(10)



fb = Facebook()
fb.login()
driver.quit()
