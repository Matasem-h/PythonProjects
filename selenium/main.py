from selenium import webdriver
from selenium.webdriver.common.by import By

# To keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# By.CSS_SELECTOR
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# By.XPath
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# Finding many elements
# driver.find_elements(By.CSS_SELECTOR)


event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
for time in event_times:
    print(time.text)

event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
for name in event_names:
    print(name.text)


# Close Chrome
# driver.close()
driver.quit()