from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os

DIR = "C:\\Users\Marco Sérvio\\AppData\\Local\\Google\\Chrome\\User Data"
driver = Driver(uc=True, headless=False, user_data_dir=DIR, undetectable=True)

driver.get("chrome://settings/")
driver.execute_script("chrome.settingsPrivate.setDefaultZoom(1);")
driver.get("chrome://version/")
driver.save_screenshot("valeuveiogarcon2.png")

driver.get("chrome://settings/")
driver.execute_script("chrome.settingsPrivate.setDefaultZoom(0.25);")

caminho_absoluto = os.path.abspath("site.html")

driver.get("file:///" + caminho_absoluto)
botao = driver.find_element(By.ID, "botao-down")

janela_principal = driver.current_window_handle

botao.click()

time.sleep(5)

janelas = driver.window_handles

nova_janela = None
for janela in janelas:
    if janela != janela_principal:
        nova_janela = janela
        break

driver.switch_to.window(nova_janela)

url_nova_guia = driver.current_url
driver.get("chrome://settings/")
driver.execute_script("chrome.settingsPrivate.setDefaultZoom(0.85);")
driver.get(url_nova_guia)
driver.save_screenshot("valeuveiogarcon.png")
driver.switch_to.window(janela_principal)
driver.save_screenshot("teste.png")
