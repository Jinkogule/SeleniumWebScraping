#baixa o Opera (Windows) pelo Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from SeleniumWebScraping import acessaURL, clicaHyperlink, fechaDriver

urlOpera = "https://www.opera.com/pt-br/download"
xPathOpera = "/html/body/main/section[1]/div/div/div[1]/div/span/a/span" #full xPath do hyperlink do download

driverChrome = webdriver.Chrome(ChromeDriverManager().install())

try:
    acessaURL(driverChrome, urlOpera, xPathOpera)
    clicaHyperlink(driverChrome, xPathOpera)
    fechaDriver(driverChrome)
except Exception:
    driverChrome.quit()
    print("Erro na tentativa de download.")