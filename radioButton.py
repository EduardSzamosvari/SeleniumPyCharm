import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from config.settings.setari import *

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(executable_path=PATH)


class TestingRadioButton():

    driver.get("http://demo.guru99.com/test/radio.html")

    def selectElements(self, xpath):

        lista = driver.find_elements_by_xpath(xpath)

        for x in lista:
            isSelected = x.is_selected()
            if isSelected:
                print("button is selected "+ x.get_attribute("value"))
            else:
                x.click()
                print("button just selected "+ x.get_attribute("value"))
                time.sleep(5)


radioAndCheckBox = TestingRadioButton()
radioAndCheckBox.selectElements(XPATH_RADIO)
radioAndCheckBox.selectElements(XPATH_CHECKBOX)
#radioAndCheckBox.radioButton()
#radioAndCheckBox.checkBox()

driver.quit()
