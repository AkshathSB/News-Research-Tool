from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s= Service('C:/Users/Akshath/Chromedriver')

driver = webdriver.Chrome(service=s)
driver.get("https://chat.openai.com/c/112ea0b7-a0a8-4930-94e4-4baedd3b1177")

the_url = driver.find_element(by=By.XPATH)

chromeDriverLocation = driver.service.path
print(chromeDriverLocation)

driver.quit()