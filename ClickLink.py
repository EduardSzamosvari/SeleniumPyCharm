import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path=PATH)
from conf


class TestingClickLink():

    def clickLink(self):

        driver.get(URL)

        links = driver.find_elements_by_link_text("click here")
        for onelink in links:
            att = onelink.get_attribute('href')
            if att == "http://www.fb.com/":
                onelink.click()
                title = driver.title
                if "Facebook" in title:
                    print("Found")
                break

test = TestingClickLink()
test.clickLink()

driver.quit()
