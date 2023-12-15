from seleniumbase import Driver

DIR = "/home/paulofernando1992/chromedata"
driver = Driver(uc=True, headless=False, user_data_dir=DIR, undetectable=True)
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

elem_username.send_keys(username)
elem_password.send_keys(password)
elem_login_button.click()

driver.save_screenshot("login.png")
driver.close()
