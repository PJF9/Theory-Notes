from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


path = "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"

driver = webdriver.Firefox(executable_path=path)
driver.get("https://python.org")

pycon = driver.find_element_by_link_text("PSF News")
pycon.click()

"""
    Waits maximum specified seconds until all elementsare loaded
    correctly. If all are set ready before the sepcified seconds,
    then the program will continue normally. Else it will raise
    an error.
"""
driver.implicitly_wait(10)
driver.find_element_by_link_text("ΟΚ").click()

driver.find_element_by_link_text("Python Software Foundation").click()
driver.implicitly_wait(5)
driver.find_element_by_link_text("Donate").click()

"""
    The above wait is called Implicit Wait. This wait is called
    External Wait and only waits for a specific element to be ready.

    Expected Conditions:
        visibility_of_element_located
        element_located_to_be_selected
        element_to_be_selected
        element_to_be_clickable
"""
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "edit-name")))
driver.find_element_by_id("edit-name").send_keys("Commando")   
