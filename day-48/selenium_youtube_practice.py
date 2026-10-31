from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name='detach', value=True)

driver = webdriver.Chrome(chrome_options)
driver.get('https://www.youtube.com/')

side_bar = driver.find_element(By.CSS_SELECTOR, '.yt-icon-shape div')
side_bar.click()

music_tab = driver.find_element(
    By.XPATH, '//*[@id="endpoint"]/tp-yt-paper-item/yt-formatted-string')
music_tab.click()

driver.quit()
