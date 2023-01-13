from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_wikipedia_data():
    url = "https://en.wikipedia.org/wiki/List_of_schemes_of_the_government_of_India"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all('table')
    df = pd.read_html(str(table))[2]
    df.rename(columns = {'Scheme[note 1]':'Scheme'}, inplace = True)
    return df