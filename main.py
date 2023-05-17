from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

url = "https://linkedin.com/login"

driver.get(url=url)
login_password = input("What is your linked in password ?")
username = driver.find_element(By.NAME, "session_key")
username.send_keys("yaitsmethiyagu@gmail.com")
username.send_keys(Keys.TAB)

password = driver.find_element(By.NAME, "session_password")
password.send_keys(login_password)
password.send_keys(Keys.ENTER)

driver.get("https://www.linkedin.com/jobs/collections/recommended/")
apply = driver.find_element(By.XPATH, '//*[@id="ember174"]')
apply.click()

