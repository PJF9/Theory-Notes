"""
    This file is showing us how to access search bars and how to get
    informations, from them.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



path = "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"

driver = webdriver.Firefox(executable_path=path)
driver.get("https://duckduckgo.com")

""" 
    Finding the search bar out of the html page. 
    The search variable is an object that represent the search bar.
"""
search = driver.find_element_by_id("search_form_input_homepage")

""" Clearing all the text from the search bar. """
search.clear()

""" Sending text to the search bar. """
search.send_keys("Linux Os")
search.send_keys(Keys.RETURN)

""" 
    Waiting 10 seconds until Python finds the r1-0 id at the page.
    If the whatever we are looking for doesn't exist, meaning that
    if 10 second are passed, we willl get an error.
    With 'By' we can also use .NAME, .CLASS_NAME, .LING_TEXT, and
    much more.
"""
try:
    """ Reach the first link. """
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "r1-0"))
    )

    """ Click the link object. """
    link.click()
    
    """ Get all the text of the page. """
    all_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "td-outer-wrap"))
    )

    """ Get all the page headers. The ...elements... method returns a list. """
    headers = all_text.find_elements_by_tag_name('h2')
    for header in headers:
        print(header.text)
    
finally:
    sleep(3)
    driver.quit()
