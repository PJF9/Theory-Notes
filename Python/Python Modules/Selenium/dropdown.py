from selenium import webdriver
from selenium.webdriver.support.ui import Select


path = "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"

driver = webdriver.Firefox(executable_path=path)
driver.get("https://xrysoi.pro")

""" Only works with select tags. """
m1 = driver.find_element_by_id("menu-item-4805")
drop = Select(m1)

drop.select_by_index(1)
