from selenium import webdriver
from selenium.webdriver.common.keys import Keys


path = "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"

driver = webdriver.Firefox(executable_path=path)
driver.get("https://xrysoi.pro")
driver.implicitly_wait(5)

""" Searching for the input box and writing the text """
input_box = driver.find_element_by_id("searchbox").send_keys("avengers")
submit_button = driver.find_element_by_id("searchbutton").click()

driver.implicitly_wait(5)
movie = driver.find_element_by_link_text("Captain America 3: Civil War (2016)").click()
