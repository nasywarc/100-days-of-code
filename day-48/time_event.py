from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url='https://www.python.org')

time_date = driver.find_elements(
    By.XPATH,
    value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time'
)

time_year = driver.find_elements(
    By.XPATH,
    value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time/span'
)

event_name = driver.find_elements(
    By.XPATH,
    value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a'
)

data = {}
for i in range(len(time_year)):
    data[i] = {
        'time': time_year[i].get_attribute('textContent') + time_date[i].text,
        'name': event_name[i].text
    }
print(data)

driver.quit()
