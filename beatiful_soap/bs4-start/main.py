from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "lxml")
# print(soup.title.string)
# print(soup.a)
# print(soup.p)
