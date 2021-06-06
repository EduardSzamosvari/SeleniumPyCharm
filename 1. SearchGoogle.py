import time
# saa
from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\\Curs Software tester\\Softuri\chromedriver.exe")

class Google():

    def SearchGoogle(self):
        driver.get("https://www.google.ro/")
        #agree = driver.find_element_by_xpath("//div[normalize-space()='Sunt de acord']")
        agree = driver.find_element_by_id("L2AGLb")
        agree.click()
        #find = driver.find_element_by_xpath("//input[@title='Căutați']")
        find = driver.find_element_by_name("q")
        find.send_keys("selenium")
        find.submit()

        time.sleep(10)


search = Google()
search.SearchGoogle()
driver.quit()