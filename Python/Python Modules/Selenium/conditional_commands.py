from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


path = "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"

driver = webdriver.Firefox(executable_path=path)
driver.get("https://python.org")

search_bar = driver.find_element_by_id("id-search-field")

""" Returns True only if search bar is on the page (has loaded successfully) """
if search_bar.is_displayed():
    search_bar.send_keys("Docs")
    search_bar.send_keys(Keys.RETURN)

    sleep(2)

    """ 
        Returns True if the link is not clicked, the is_selected() method works 
        well with radio buttons, checkboxes and some times at dropdown menus.
    """
    first_link = driver.find_element_by_link_text("Linux RPMs for Python 2.2.1")
    if not first_link.is_selected():
        first_link.click()

sleep(5)
driver.quit()
