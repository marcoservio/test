from seleniumbase import Driver
from seleniumbase.config import settings
from selenium.webdriver.chrome.options import Options

DIR = "/home/paulofernando1992/chromedata"

# Opções do navegador
options = Options()
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
options.add_argument("--no-first-run")
options.add_argument("--no-service-autorun")
options.add_argument("--password-store=basic")
options.add_argument(f"--user-data-dir={DIR}")

# Configurações específicas do seleniumbase
self.settings.USER_DATA_DIR = DIR

# Configurar as opções do Chrome
self.set_chrome_options(options)

# Inicializar o driver
self.create_driver()

# Acesse o objeto driver diretamente, se necessário
driver = self.driver

# Navegar para a URL desejada
self.open("chrome://version/")

# Capturar uma screenshot
self.save_screenshot("valeuveiogarcon2.png")

# Fechar o driver
driver.close()
