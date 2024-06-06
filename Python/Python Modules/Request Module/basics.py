import requests


r = requests.get("https://xkcd.com/353/")
# print(r)
# All the atributes and methods
# print(dir(r))
# Help
# print(help(r)) 

# Print all the html off the site
# print(r.text)

R = requests.get("https://imgs.xkcd.com/comics/python.png")
# Print the contenct in bytes
# print(R.content)

# Saving this image using python
# wb is write in bytes
with open("comic.png", "wb") as f:
    f.write(R.content)

# If the we get a good response
# print(r.status_code)
# 200 is success
# 300 redirects
# 400 client errors
# 500 server errors
# The ok response is 200 and 300
# We have
# print(r.ok)
# print(r.headers)

# Passing parameters to the url
params = {"page": 2, "count": 25}
r = requests.get("https://httpbin.org/get", params=params)
# print(r.text)

# Post informations
params = {"username": "Petros", "password": "123"}
r = requests.post("https://httpbin.org/post", data=params)
# print(r.text)
# print(r.json())
r_dict = r.json()

r_username = r_dict["form"]["username"]
print(r_username)