from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# # driver.get('https://www.amazon.com')
# driver.get(
#     url='https://www.amazon.com/Computer-Supports-Expansion-Portable-Notebook/dp/B0HK88DFX6/'
# )

# continue_shopping = driver.find_element(By.CLASS_NAME, value="a-button-text")
# continue_shopping.click()
# print(driver.current_url)

# price = driver.find_element(By.CLASS_NAME, value="a-price-whole")

# print(f'The price is {price.text}')

driver.get(url='https://python.org')
search_bar = driver.find_element(By.ID, value="id-search-field")
print(search_bar.get_attribute('placeholder'))

go_button = driver.find_element(By.ID, value="submit")
print(go_button.size)

documentation_link = driver.find_element(
    By.CSS_SELECTOR, value=".documentation-widget a"
)
print(documentation_link.text)

bug_link = driver.find_element(
    By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a'
)
print(bug_link.text)

foot_link = driver.find_elements(By.CLASS_NAME, value='tier-1')
for link in foot_link:
    print(link.text)

# driver.close()
driver.quit()
