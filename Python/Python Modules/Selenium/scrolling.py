from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


path = "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"

driver = webdriver.Firefox(executable_path=path)
driver.get("https://ultimateqa.com/dummy-automation-websites/")
driver.implicitly_wait(5)

""" With this way we can scroll down by some pixels """
driver.execute_script("window.scroll(0, 1000)", "")
sleep(1)

""" To go up the page the eaziest way is throught ActionChains. """
a = ActionChains(driver)
a.send_keys(Keys.PAGE_UP)
a.send_keys(Keys.PAGE_UP)
a.send_keys(Keys.PAGE_UP)
a.send_keys(Keys.PAGE_UP)
a.perform()


""" We can also scroll down until we found an element. """
driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_link_text("API documentation here"))

sleep(2)

""" Scroll to the end of the page. """
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

sleep(2)
driver.quit()
