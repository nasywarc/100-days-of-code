from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name='detach', value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url='https://github.com/')
email_field = driver.find_element(
    By.XPATH,
    '//*[@id="_R_9j8l_"]',
)
email_field.click()
email_field.clear()
email_field.send_keys(os.getenv('github_email'))

signUp_button = driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div[5]/main/react-app/div/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div[2]/form/button'
)
signUp_button.click()
