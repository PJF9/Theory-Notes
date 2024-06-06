"""
    This file is showing how to navigate throw the page,
    via button and link clicking.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


path = "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"

driver = webdriver.Firefox(executable_path=path)
driver.get("https://www.linux.com/what-is-linux/")

""" Finding the link that has the text: 'ABOUT US' and clicking it """
link = driver.find_element_by_link_text("ABOUT US")
link.click()

""" Here we need to wait, else we will get an error. """
try:
    link2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Stack Overflow"))
    )
    link2.click()

    """ Get to Stack Overflow log in page. """
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Log in"))
    )
    button.click()

    """ Getting back three pages """
    driver.back()
    driver.back()
    driver.back()

    """ Getting forward one page. """
    driver.forward()

finally:
    sleep(3)
    driver.quit()
