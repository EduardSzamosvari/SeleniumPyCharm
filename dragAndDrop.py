import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from config.settings import *

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options,executable_path=CHROME_PATH)

class DragAndDrop():

    def testingDragAndDrop(self):
        driver.get(URL)
        driver.maximize_window()

        pathIframe = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
        driver.switch_to.frame(pathIframe)

        fromElement = driver.find_element_by_id("draggable")
        toElement = driver.find_element_by_id("droppable")

        action = ActionChains(driver)
        action.drag_and_drop(fromElement, toElement)
        action.perform()

        time.sleep(5)
        print("Am terminat")

dragAndDrop = DragAndDrop()
dragAndDrop.testingDragAndDrop()
driver.quit()