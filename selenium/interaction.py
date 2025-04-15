from selenium import webdriver

# To keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Navigate to Wikipedia









# To close Chrome after program finishes
# driver.close()
# driver.quit()