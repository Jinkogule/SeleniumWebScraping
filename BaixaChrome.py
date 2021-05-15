#baixa o Chrome (Windows) pelo Firefox
from selenium import webdriver
from SeleniumWebScraping import acessaURL, clicaHyperlink, fechaDriver

urlChrome = "https://www.google.com/intl/pt-BR/chrome/"
xPathChrome = "/html/body/div[3]/section[1]/div/div/div/div/button" #full xPath do hyperlink do download

driverFirefox = webdriver.Firefox()

try:
    acessaURL(driverFirefox, urlChrome, xPathChrome)
    clicaHyperlink(driverFirefox, xPathChrome)
    fechaDriver(driverFirefox)
except Exception:
    driverFirefox.quit()
    print("Erro na tentativa de download.")

