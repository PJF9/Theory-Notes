import requests
from bs4 import BeautifulSoup
import logging


# Output the code in a log file
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(message)s")

file_handler = logging.FileHandler("output.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# To work with a real web site we need to get the source code first
# This request method return a respond object that why we need .text for getting the sourcr code
source = requests.get("https://coreyms.com/").text

# Creating the soup object
soup = BeautifulSoup(source, "lxml")
# print(soup.prettify())

article = soup.find("article")
# print(article.prettify())

headline = article.h2.a.text
# print(headline)
content = article.find("div", class_="entry-content").p.text
# print(content)
video = article.find("iframe", class_="youtube-player")["src"]
video = video.split("?")[0]
video = video.split("/")[-1]

video = f"https://www.youtube.com/watch?v={video}"
# print(video)

# Get all the informations we need
for article in soup.find_all("article"):
    # Managing eceptions
    try:
        headline = article.h2.a.text
    except:
        headline = "None"

    try:
        content = article.find("div", class_="entry-content").p.text
    except:
        content = "None"

    try:
        video = article.find("iframe", class_="youtube-player")["src"]
        video = video.split("?")[0]
        video = video.split("/")[-1]
        video = f"https://www.youtube.com/watch?v={video}"
    except:
        video = "None"


    logger.info(f"----> Article Title: {headline}")
    logger.info(f"----> Article Summary: {content}")
    logger.info(f"----> Article Youtube Video Link: {video}")
    logger.info("")
