import pandas as pd
from bs4 import BeautifulSoup as bs
from js import document

clutters = ['List of real', '......']

with open('index3.txt') as data:
    for line in data:
        document.getElementById('tulisan').innerHTML = line