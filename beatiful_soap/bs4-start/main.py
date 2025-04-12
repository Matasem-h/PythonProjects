from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
article_tag = soup.find(name="a", class_="sitebit comhead")
print(article_tag.getText())










