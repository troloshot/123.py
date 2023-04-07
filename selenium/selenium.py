"""
Напишите программу которая автоматически зайдет на https://store.steampowered.com/ в поле поиска отправит стратегии
и соберет названия всех стратегий на 1 странице.
"""
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import lxml
options=Options()
driver=webdriver.Firefox(options=options)
driver.get("https://store.steampowered.com/?l=russian")
search=driver.find_element(By.XPATH, '//*[@id="store_nav_search_term"]')
search.send_keys("Стратегии")
search.send_keys(Keys.ENTER)
time.sleep(3)
page=driver.page_source
soup=BeautifulSoup(page, 'lxml')
container=soup.find('div','search_results')
names=container.find_all('span', 'title')
for i in names:
    print(i.text)