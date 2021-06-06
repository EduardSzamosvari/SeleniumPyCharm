import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Curs Software tester\\Softuri\\chromedriver.exe")

class Click():

    def ClickLink(self):
        driver.get("http://demo.guru99.com/test/link.html")
        links = driver.find_elements_by_link_text("click here")

        for link in links:
            att = link.get_attribute("href")
            if att == "http://www.fb.com/":
                link.click()
                titlu = driver.title
                if "Facebook" in titlu:
                    print("Found page Facebook")
                break


        time.sleep(10)

open = Click()
open.ClickLink()
driver.quit()