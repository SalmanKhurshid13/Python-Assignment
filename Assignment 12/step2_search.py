from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python tutorial")
search_box.send_keys(Keys.RETURN)
