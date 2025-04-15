from selenium import webdriver
from selenium.webdriver.common.by import By

# To keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to Wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Hone in on anchor tag using CSS selectors
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()
# print(article_count.text)

# Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" <input> by Name
search = driver.find_element(By.NAME, value="search")

# Sending keyboard input to Selenium
search.send_keys("Python")



# To close Chrome after program finishes
# driver.close()
# driver.quit()
