from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name='detach', value=True)

driver = webdriver.Chrome(chrome_options)
driver.get('https://maganghub.kemnaker.go.id/magang-nasional/lowongan')

search_location = driver.find_element(
    By.XPATH,
    '/html/body/div[3]/div[3]/div[2]/div[1]/aside/div/div/div[4]/div[1]/div/input'
)

id_list = ["2d3c10c2-bf3c-4bd0-af28-6674be8542a2-0",
           "ea34d5f7-2838-41de-88e6-02986bb074ce-1",
           "73c670c2-bd42-491a-a76b-f17c2edb6680-2",
           "6c3810bf-6036-42a7-9643-386f71e6a464-3",
           "fdff22bf-5244-411d-ab76-075b96a41643-4"
           ]

for id in range(len(id_list)):
    search_location.click()
    search_location.clear()
    search_location.send_keys('jakarta')
    if id == 0:
        checklist = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.ID, id_list[id]))
        )
    else:
        checklist = driver.find_element(By.ID, id_list[id])
    checklist.click()
