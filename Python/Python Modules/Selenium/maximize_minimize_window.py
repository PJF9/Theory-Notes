from selenium import webdriver
from time import sleep


path = "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"

driver = webdriver.Firefox(executable_path=path)
driver.get("https://ultimateqa.com/dummy-automation-websites/")
driver.implicitly_wait(5)

""" Maximize the window """
driver.maximize_window()

sleep(2)

""" Minimize the window """
driver.minimize_window()

sleep(2)
driver.maximize_window()
sleep(2)
driver.quit()
