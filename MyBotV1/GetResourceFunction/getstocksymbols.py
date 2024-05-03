from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

class StockSymbol:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def __init__(self) -> None:
        self.__industry_symbols = ['agro', 'consump', 'fincial', 'indus', 'propcon', 'resourc', 'service', 'tech']

    def getIndustrySymbols(self):
        return self.__industry_symbols

