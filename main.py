from http import client
import webbrowser
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

with open('/home/ubuntu/Desktop/telegram_bot/files/groups.txt','r') as groupsList:
    groups = groupsList.readlines()

login_url = "https://web.telegram.org/?legacy=1#/login"
driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get(login_url)


users_list = groups


print("Connecting to Telegram Web, please wait")

phone_input_code = driver.find_element_by_name("phone_country")
phone_input_number = driver.find_element_by_name("phone_number")

phone_input_code.send_keys(Keys.BACK_SPACE, "32")
phone_input_number.send_keys("499136862")

time.sleep(3)

next_button = driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div/div[3]/div[1]/div/a")
next_button.click()

time.sleep(3)

my_number_button = driver.find_element_by_xpath("//*[@id='ng-app']/body/div[4]/div[2]/div/div/div[2]/button[2]")
my_number_button.click()

time.sleep(3)

enter_code_input = driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div/div[3]/div[2]/form/div[3]/input")
enter_code = input("Code: ")

time.sleep(25)

enter_code_input.send_keys(enter_code + Keys.ENTER)

time.sleep(3)

search_message = driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[2]/div/div[1]/div[1]/div/input")

time.sleep(3)

#search_message.send_keys("@drake")

text = "last seen a long time ago"

async def main():
    for i in range(len(groups)):

        search_message.send_keys(users_list[i] + Keys.ENTER)
        time.sleep(3)

        if text in driver.page_source:
            print(users_list[i])
        else:
            print("this doesn't work")
    
