from bs4 import BeautifulSoup


# First we need to make our html file a soup object
# If we can we can specify the file mode but by default is r
with open("simple.html") as html_file:
    soup = BeautifulSoup(html_file, "lxml") # lxml is a parcer. Parcer is used when the html has problems and it fixes the problems

# The soup variable has all the source code of our file
# .prettify() is the method that help us read the source code eazily
# print(soup.prettify())

# We can access the different part of the html file
# With .text we are accessing only the text not the <body> ...
# With this method we are getting only the first of what we want to search
site_title = soup.title.text
site_body = soup.body.text
site_div = soup.div.h2.a.text 
# print(site_title, site_body)
# print(site_div)

# To access a specific tag
# .soup.find("div") == soup.div
site_div = soup.find("div", class_="info").p.text
# print(site_div)

# Start accessing the site
article = soup.find("div", class_="article")
# print(article)
headline = article.h2.a.text
# print(headline)
summary = article.p.text
# print(summary)

# Now because we have the inforamtion of 1 article we can eazily have all the articles
# .find_all() returns a list
for article in soup.find_all("div", class_="article"):
    headline = article.h2.a.text
    summary = article.p.text
    
    print(f"  Title: {headline}")
    print(f"Content: {summary}")
    print()
    