from seleniumbase import BaseCase
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Caminho do diretório para user_data_dir
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

# Criar instância do driver
driver = BaseCase().create_driver(chrome_options=options)

# Navegar para a URL desejada
driver.get("chrome://version/")

# Capturar uma screenshot
driver.save_screenshot("valeuveiogarcon2.png")

# Fechar o driver
driver.quit()
