from selenium import webdriver


path = "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"

""" To download something from the web we need to add some settings. """
firefox_prof = webdriver.FirefoxProfile()
firefox_prof.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,applization/pdf")
firefox_prof.set_preference("browser.download.manager.showWhenStarting", False)
firefox_prof.set_preference("drowser.download.dir", "c:\\User\\jacob\\Downloads")

driver = webdriver.Firefox(executable_path=path)
driver.get("https://ubuntu.com/download/desktop")
driver.implicitly_wait(5)

driver.find_element_by_id("cookie-policy-button-accept").click()
driver.find_element_by_link_text("Download").click()
driver.find_element_by_link_text("20.04 LTS").click()
