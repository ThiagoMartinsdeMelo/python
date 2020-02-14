# -*- encoding: utf-8 -*-
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

# Pegar conteúdo html a partir da url
url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"
top10ranking = {}
rankings = {
    '3points': {'field': 'FG3M', 'label': '3PM'},
    'points': {'field': 'PTS', 'label': 'PTS'},
    'assistants': {'field': 'AST', 'label': 'AST'},
    'rebounds': {'field': 'REB', 'label': 'REB'},
    'steals': {'field': 'STL', 'label': 'STL'},
    'blocks': {'field': 'BLK', 'label': 'BLK'},
}

def buildrank(type):
    field = rankings[type]['field']
    label = rankings[type]['label']

    driver.find_element_by_xpath(
        f"//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='{field}']").click()

    element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
    html_content = element.get_attribute('outerHTML')

    # Parsear o conteúdo html - BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')

    # Estruturar conteúdo em um data frame - Pandas
    df_full = pd.read_html(str(table))[0].head(10)
    df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', label]]
    df.columns = ['pos', 'player', 'team', 'total']

    # Transformar os dados em um dicionário de dados próprios
    return df.to_dict('records')

# Renderizar o firefox
option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)
driver.get(url)
driver.implicitly_wait(10)  # in seconds

for k in rankings:
    top10ranking[k] = buildrank(k)

driver.quit()
# Converter e salvar em um arquivo json
with open('ranking.json', 'w', encoding='utf-8') as jp:
    js = json.dumps(top10ranking, indent=4)
    jp.write(js)