import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\\Curs Software tester\\Softuri\\chromedriver")

USERID = "mngr327236"
PASSWORD = "rehavAs"
class Login():

    def Common(self, USERID , PASSWORD):
        driver.get("http://www.demo.guru99.com/V4/")
        user = driver.find_element_by_xpath("//input[@name='uid']")
        user.send_keys(USERID)
        passw = driver.find_element_by_xpath("//input[@name='password']")
        passw.send_keys(PASSWORD)
        butlogin = driver.find_element_by_xpath("//input[@name='btnLogin']")
        butlogin.click()
        time.sleep(10)



    def logOK(self, USERID, PASSWORD, testcase):
        self.Common(USERID, PASSWORD)
        try:
            titlu = driver.title
            if titlu == "Guru99 Bank Manager HomePage":
                print("Login with " + testcase + " is PASS")
            else:
                print("Login with " + testcase + " is FAILED")
        except:
            print("Login with " + testcase + " is FAILED")
    def logNOK(self, USERID, PASSWORD, testcase):
        self.Common(USERID,PASSWORD)
        try:
            titlu = driver.title
            if titlu == "Guru99 Bank Manager HomePage":
                print("Login with " + testcase + " is FAILED" )
            else:
                print("Login with " + testcase + " is PASS")
        except:
                print("Login with " + testcase + " is PASS")


log = Login()
log.logOK(USERID, PASSWORD,"user OK pass OK")
log.logNOK(USERID,"pass NOK", "user OK and pass NOK")
log.logNOK("user NOK",PASSWORD, "user NOK and pass OK")
log.logNOK(USERID,"", "user OK and pass empty")
log.logNOK("",PASSWORD, "user empty and pass OK")
log.logNOK("user NOK","pass NOK", "user NOK and pass NOK")
log.logNOK("","", "user empty and pass empty")
driver.quit()
