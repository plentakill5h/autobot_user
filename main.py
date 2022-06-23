import webbrowser
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

phone_number = "+32499136862"
login_url = "https://web.telegram.org/"
driver = webdriver.Chrome("/usr/bin/chromedriver")

driver.get(login_url)

login = driver.find_element_by_xpath("//*[@id='auth-pages']/div/div[2]/div[2]/div/div[2]/button/div")
login.click()

#driver.close()