from selenium import webdriver


path = "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"

driver = webdriver.Firefox(executable_path=path)
driver.get("https://app.betterimpact.com/Login/Volunteer")
driver.implicitly_wait(5)

""" Finding the the checkbutton. """
check_1 = driver.find_element_by_id("FilterPublicSearchCovidRecruit")
""" With is_selected() we can know if the button is clicked or not. """
print(check_1.is_selected())
check_1.click()
print(check_1.is_selected())
