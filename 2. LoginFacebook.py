import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\\Curs Software tester\\Softuri\\chromedriver.exe")

class logFB():

    def loginFB(self):
        driver.get("https://www.facebook.com/")
        accept = driver.find_element_by_xpath("//button[contains(text(),'Acceptă tot')]")
        accept.click()
        email = driver.find_element_by_xpath("//input[@id='email']")
        email.send_keys("emailul tau")
        parola= driver.find_element_by_xpath("//input[@id='pass']")
        parola.send_keys("parola ta")
        buttonconnect = driver.find_element_by_xpath("//button[contains(text(),'Conectează-te')]")
        buttonconnect.click()
        time.sleep(10)



log = logFB()
log.loginFB()
driver.quit()