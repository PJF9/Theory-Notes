from selenium import webdriver


path = "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"

driver = webdriver.Firefox(executable_path=path)
driver.get("https://www.skroutz.gr/")
driver.implicitly_wait(5)

""" Getting all the cookies the browser has stored. """
all_cookies = driver.get_cookies()
print(len(all_cookies))
print(all_cookies, '\n')

""" Adding cookies to the browser. """
cookie = {'name': 'My cookie', 'value': '369'}
driver.add_cookie(cookie)

all_cookies = driver.get_cookies()
print(len(all_cookies))
print(all_cookies, '\n')

""" Deleting cookies. """
driver.delete_cookie('My cookie')

all_cookies = driver.get_cookies()
print(len(all_cookies))
print(all_cookies, '\n')

""" Delete all cookies. """
driver.delete_all_cookies()

all_cookies = driver.get_cookies()
print(len(all_cookies))
print(all_cookies)
