from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

DIR = "/home/paulofernando1992/chromedata"
driver = Driver(uc=True, headless=False, user_data_dir=DIR, undetectable=True)

driver.get("chrome://settings/")
driver.execute_script("chrome.settingsPrivate.setDefaultZoom(1);")


def login_google():
    driver.get("https://accounts.google.com/")

    time.sleep(5)

    email_field = driver.find_element(By.ID, "identifierId")
    email_field.send_keys("jiskoloviske@gmail.com")

    time.sleep(3)

    botao_avancar = driver.find_element(
        By.CSS_SELECTOR,
        "button[class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']",
    )
    botao_avancar.click()

    time.sleep(5)

    password_field = driver.find_element(
        By.CSS_SELECTOR, "input[class='whsOnd zHQkBf']"
    )
    password_field.send_keys("Marco@007")

    time.sleep(3)

    botao_avancar2 = driver.find_element(
        By.CSS_SELECTOR,
        "button[class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']",
    )
    botao_avancar2.click()

    time.sleep(3)

    driver.save_screenshot("login_google.png")


def fechar_cliente():
    driver.close()


def find_element_load(driver, by, elem):
    try:
        return WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((by, elem))
        )
    except:
        print("Could not find element within 30 seconds")
        fechar_cliente()


def login():
    # driver.get("chrome://settings/")
    # driver.execute_script("chrome.settingsPrivate.setDefaultZoom(0.25);")
    driver.get("https://canal360i.cloud.itau.com.br/login/iparceiros")

    ELEM_USERNAME_ID = "voxel-input-0"
    ELEM_PASSWORD_ID = "voxel-input-1"
    ELEM_LOGIN_BUTTON_XPATH = '//*[@id="btn-entrar"]'
    elem_username = find_element_load(driver, By.ID, ELEM_USERNAME_ID)
    elem_password = find_element_load(driver, By.ID, ELEM_PASSWORD_ID)
    elem_login_button = find_element_load(driver, By.XPATH, ELEM_LOGIN_BUTTON_XPATH)

    username = "FRIBEI.OP01"
    password = "252829"

    time.sleep(1)
    elem_username.send_keys(username)
    time.sleep(1)
    elem_password.send_keys(password)
    time.sleep(1)
    elem_login_button.click()

    ERRO_LOGIN = find_element_load(
        driver,
        By.CSS_SELECTOR,
        "div[class='ng-tns-c113-0 toast-message ng-star-inserted']",
    )

    if ERRO_LOGIN.is_displayed():
        time.sleep(10)
        fechar_cliente()
        raise Exception(
            "Falha ao Logar. Erro mostrado no site do itau: Não foi possível concluir seu pedido. Tente de novo mais tarde."
        )

    driver.save_screenshot("login.png")


try:
    login_google()
except:
    print("Você ja esta logado na conta do Google")

login()

time.sleep(1)
driver.save_screenshot("final.png")
