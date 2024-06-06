from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


path = "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"

driver = webdriver.Firefox(executable_path=path)
driver.get("https://www.python.org/")

"""
Hover action (the dropdown from the menues). 

sleep(2)
products = driver.find_element_by_class_name("sf-with-ul")
p = driver.find_element_by_link_text("Evening Dresses")

action1 = ActionChains(driver)
action1.move_to_element(products)
action1.move_to_element(p)
action1.click()
action1.perform()
"""

""" Preforming double click """
sbar = driver.find_element_by_id("id-search-field")
sbar.send_keys("test")
sleep(1)

ActionChains(driver).double_click(sbar).perform()
sbar.send_keys("a")
sbar.send_keys(Keys.RETURN)

driver.back()
sleep(2)
