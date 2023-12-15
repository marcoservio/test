from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from seleniumbase import Driver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException

import time

DIR = "/home/paulofernando1992/chromedata"
driver = Driver(uc=True, headless=False, user_data_dir=DIR, undetectable=True)

driver.get("chrome://version/")
driver.save_screenshot("valeuveiogarcon2.png")

driver.get("chrome://settings/")
driver.execute_script("chrome.settingsPrivate.setDefaultZoom(0.25);")
driver.get("https://canal360i.cloud.itau.com.br/login/iparceiros")

def find_element_load(driver, by, elem):
    try:
        return WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((by, elem))
        )
    except:
        print("Could not find element within 30 seconds")
        fechar_cliente()

ELEM_USERNAME_ID = "voxel-input-0"
ELEM_PASSWORD_ID = "voxel-input-1"
ELEM_LOGIN_BUTTON_XPATH = '//*[@id="btn-entrar"]'
elem_username = find_element_load(driver, By.ID, ELEM_USERNAME_ID)
elem_password = find_element_load(driver, By.ID, ELEM_PASSWORD_ID)
elem_login_button = find_element_load(driver, By.XPATH, ELEM_LOGIN_BUTTON_XPATH)

username = "C2BCONS.OP02"
password = "861590"

elem_username.send_keys(username)
elem_password.send_keys(password)
elem_login_button.click()

time.sleep(3)

driver.save_screenshot("login.png")
driver.close()
