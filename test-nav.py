DIR = "/home/paulofernando1992/chromedata"
driver = Driver(uc=True, headless=False, user_data_dir=DIR)
driver.get("chrome://version/")
driver.save_screenshot("valeuveiogarcon2.png")
driver.close()
