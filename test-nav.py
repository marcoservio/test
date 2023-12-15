from seleniumbase import Driver

DIR = "/home/paulofernando1992/chromedata"
driver = Driver(
    uc=True, headless=False, user_data_dir=DIR, undetectable=True, disable_csp=True
)
driver.get("chrome://version/")
driver.save_screenshot("valeuveiogarcon2.png")
driver.close()
