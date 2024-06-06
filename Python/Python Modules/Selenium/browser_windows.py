from selenium import webdriver
from time import sleep

path = "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"

driver = webdriver.Firefox(executable_path=path)
driver.get("https://ultimateqa.com/dummy-automation-websites/")
driver.implicitly_wait(5)

driver.find_element_by_link_text("SauceDemo.com").click()

""" 
    The specified site contains some link for sites that will open in 
    a different window. So we need a way to change the windows we want
    to use.
"""

""" With this command we are getting the unique id of each and every window. """
windows = driver.window_handles

""" This is how we change the current window. This is where the close() might be usefull."""
driver.switch_to_window(windows[0])
