from seleniumbase import Driver
from seleniumbase.config import settings
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc

options = uc.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--disable-application-cache")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-zoom=25")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
driver = uc.Chrome(use_subprocess=True, options=options)

# Navegar para a URL desejada
driver.get("chrome://version/")

# Capturar uma screenshot
driver.save_screenshot("valeuveiogarcon2.png")

# Fechar o driver
driver.quit()
