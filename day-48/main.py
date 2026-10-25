from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.amazon.com')
driver.get(
    url='https://www.amazon.com/Computer-Supports-Expansion-Portable-Notebook/dp/B0HK88DFX6/'
)

price = driver.find_element(By.CLASS_NAME, value="a-price-whole")

print(f'The price is {price.text}')

# driver.close()
driver.quit()
