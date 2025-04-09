from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")
# print(soup.title.string)
# print(soup.a)
# print(soup.p)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)