import time

from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# from config.settings import *
#
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-ssl-errors=yes')
# options.add_argument('--ignore-certificate-errors')
# driver = webdriver.Chrome(options=options,executable_path=CHROME_PATH)


class TestingLogin():

    def loginTemplate(self, username, parola):
        driver.get("http://www.demo.guru99.com/V4/")

        user = driver.find_element(By.XPATH, USERNAME_XPATH)
        user.send_keys(username)

        password = driver.find_element(By.XPATH, PASSWORD_XPATH)
        password.send_keys(parola)

        button = driver.find_element_by_name("btnLogin")
        button.click()

    def LoginNOK(self , username, parola, testcase):

        self.loginTemplate(username, parola)

        time.sleep(5)

        try:
            actualTitle = driver.title
            print(actualTitle)
            if (actualTitle == "Guru99 Bank Manager HomePage"):
                print("TEST CASE LOGIN " + testcase + " NOK FAILED ")
            else:
                print("TEST CASE LOGIN "+ testcase+" NOK PASS")
        except:
            print("TEST CASE LOGIN "+ testcase+" NOK PASS")


    def LoginOK(self, username, parola):

        self.loginTemplate(username, parola)

        try:
            actualTitle = driver.title
            print(actualTitle)
            if (actualTitle == "Guru99 Bank Manager HomePage"):
                print("TEST CASE LOGIN PASS")
            else:
                print("TEST CASE LOGIN FAILED")
        except:
            print("TEST CASE LOGIN FAILED")


test = TestingLogin()
test.LoginOK(USERNAME, PASSWORD)

test.LoginNOK(USERNAME, "parolaNOK", "user ok , password nok")
test.LoginNOK("userNOK", PASSWORD, "user NOK, password ok")
test.LoginNOK("userNOK", "parolaNOK", "user NOK, password nok")
test.LoginNOK("","rehavAs", "user <empty>, password ok")
test.LoginNOK(USERNAME,"", "user ok, password <empty>")

driver.quit()