"""
    Selenium is a web automation framework. With Selenium we can automate
    any task on the web, meaning that we can control the browser using Python
    code.

    The web drivers that works with Selenium are:
        Chrome
        Firefox
        Edge
        Safari
        Opera

    To open any web site we need to call the webdriver.'webriver'(path),
        where the 'path' is the path of the web driver.
    To open a specific website we use the get('site') method.
    To quit close all tabs we use the quit() method.
    To close only one tab we use the close() method.
    To get the title of a site we use the title() method.
    To get the url we use the current_url() method.
    To get the sorce code of any site we use the page_source().
"""

from selenium import webdriver
from time import sleep


""" This is the path of the forefox driver. """
# path = "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"
path = "C:\\Users\\jacob\\Documents\geckodriver.exe"

"""
    Creating the firefox driver object. By creating this object a selenium
    firefox browser is being open.
"""
driver = webdriver.Firefox(executable_path=path)

""" 
    Go to the specified location on the web. We can access as many site we
    want, but each time we call the get() method the new site will overwrite 
    the old one. Althought we can go back to the old site using back() method
"""
driver.get("https://duckduckgo.com")

sleep(3)

""" Closing all the tabs. Close the selenium browser. """
driver.quit()
