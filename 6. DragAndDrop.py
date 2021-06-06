import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\\Curs Software tester\\Softuri\\chromedriver.exe")

class DragAndDrop():

    def draganddrop(self):
        driver.get("https://jqueryui.com/droppable/")
        iframe = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
        driver.switch_to.frame(iframe)
        dragelement = driver.find_element_by_xpath("//div[@id='draggable']")
        dropelement = driver.find_element_by_xpath("//div[@id='droppable']")
        action = ActionChains(driver)
        action.drag_and_drop(dragelement,dropelement)
        action.perform()
        print("Drag and Drop OK")
        time.sleep(5)


test = DragAndDrop()
test.draganddrop()
driver.quit()