from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import ui
import time

def acessaURL(driver, url, element_xPath):
    wait = ui.WebDriverWait(driver, 10)
    try:
        driver.get(url)
        wait.until(lambda driver: driver.find_element_by_xpath(element_xPath))
    except Exception:
        print("Não foi possível acessar a página.")

def clicaHyperlink(driver, element_xPath):
    wait = ui.WebDriverWait(driver, 10)
    try:
        wait.until(lambda driver: driver.find_element_by_xpath(element_xPath))
        driver.find_element_by_xpath(element_xPath).click()
    except NoSuchElementException:
        print("Hyperlink não encontrado.")


def fechaDriver(driver):
    time.sleep(10)
    driver.quit()