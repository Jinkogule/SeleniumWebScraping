#baixa o Firefox (Windows) pelo Microsoft Edge
from selenium import webdriver
from SeleniumWebScraping import acessaURL, clicaHyperlink, fechaDriver

urlFirefox = "https://www.mozilla.org/pt-BR/firefox/new/"
xPathFirefox = "/html/body/div[3]/main/section[1]/div/div[1]/div/div[1]/a" #full xPath do hyperlink do download

driverEdge = webdriver.Edge(executable_path="D:\\EdgeDriver\\msedgedriver.exe")

try:
    acessaURL(driverEdge, urlFirefox, xPathFirefox)
    clicaHyperlink(driverEdge, xPathFirefox)
    fechaDriver(driverEdge)
except Exception:
    driverEdge.quit()
    print("Erro na tentativa de download.")