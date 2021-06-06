import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\\Curs Software tester\\Softuri\\chromedriver.exe")
url1 = "https://www.google.ro/"
url2 = "https://www.facebook.com/"
url3 = "http://www.demo.guru99.com/V4/"
url4 = "http://demo.guru99.com/test/link.html"
url5 = "http://demo.guru99.com/test/radio.html"
url6 = "https://jqueryui.com/droppable/"
USERID = "mngr327236"
PASSWORD = "rehavAs"


class tot():
    def SG(self):
        driver.get(url1)
        agree = driver.find_element_by_id("L2AGLb").click()
        element = driver.find_element_by_name("q")
        element.send_keys("selenium")
        element.submit()
        time.sleep(5)

    def FB(self):
        driver.get(url2)
        accept = driver.find_element_by_xpath("//button[contains(text(),'Acceptă tot')]").click()
        email = driver.find_element_by_xpath("//input[@id='email']").send_keys("emaiulul tau")
        parola = driver.find_element_by_xpath("//input[@id='pass']").send_keys("parola ta")
        connect = driver.find_element_by_xpath("//button[contains(text(),'Conectează-te')]").click()
        time.sleep(5)
    def Login(self,USERID, PASSWORD):
        driver.get(url3)
        userid = driver.find_element_by_xpath("//input[@name='uid']")
        userid.send_keys(USERID)
        password = driver.find_element_by_xpath("//input[@name='password']")
        password.send_keys(PASSWORD)
        login = driver.find_element_by_xpath("//input[@name='btnLogin']").click()

    def LoginOK(self,USERID,PASSWORD, testcase):
        self.Login(USERID,PASSWORD)
        try:
            title = driver.title
            if title == "Guru99 Bank Manager HomePage":
                print ("Login with " + testcase + " is PASS")
            else:
                print("Login with " + testcase + " is FAILED")
        except:
            print("Login with " + testcase + " is FAILED")
        time.sleep(5)
    def LoginNOK(self,USERID,PASSWORD, testcase):
        self.Login(USERID,PASSWORD)
        try:
            title = driver.title
            if title == "Guru99 Bank Manager HomePage":
                print ("Login with " + testcase + " is FAILED")
            else:
                print("Login with " + testcase + " is PASS")
        except:
            print("Login with " + testcase + " is PASS")
        time.sleep(5)


    def clicklink(self):
        driver.get(url4)
        links = driver.find_elements_by_link_text("click here")
        for link in links:
            att = link.get_attribute("href")
            if att == "http://www.fb.com/":
                link.click()
                titlu = driver.title
                if "Facebook" in titlu:
                    print("Found page Facebook")
                break
        time.sleep(5)

    def radiocheckbox(self):
        driver.get(url5)
        #radioschecboxes = driver.find_elements_by_name("webform")
        radioschecboxes = driver.find_elements_by_xpath("//input[@name='webform']")
        for radio in radioschecboxes:
            if radio.is_selected():
                radio.click()
                time.sleep(2)
                print("selected " + radio.get_attribute("value"))
            else:
                radio.click()
                print("selected " + radio.get_attribute("value"))
                time.sleep(5)
    def draganddrop(self):
        driver.get(url6)
        iframe = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
        driver.switch_to.frame(iframe)
        element1 = driver.find_element_by_xpath("//div[@id='draggable']")
        element2 = driver.find_element_by_xpath("//div[@id='droppable']")
        action = ActionChains(driver)
        action.drag_and_drop(element1,element2)
        action.perform()
        print("Drag and drop OK")
        time.sleep(5)

test = tot()
test.SG()
test.FB()
test.LoginOK(USERID,PASSWORD, "USER OK and PASSWORD OK")
test.LoginNOK(USERID,"NOK", "USER OK and PASSWORD NOK")
test.LoginNOK("NOK",PASSWORD, "USER NOK and PASSWORD OK")
test.LoginNOK("NOK","NOK", "USER NOK and PASSWORD NOK")
test.LoginNOK("",PASSWORD, "USER <empty> and PASSWORD OK")
test.LoginNOK(USERID,"", "USER OK and PASSWORD <empty>")
test.LoginNOK("","", "USER <empty> and PASSWORD <empty>")
test.clicklink()
test.radiocheckbox()
test.draganddrop()
driver.quit()