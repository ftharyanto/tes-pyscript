from pyodide.http import pyfetch
from pyodide.ffi import create_proxy
import asyncio
from js import document, console
from bs4 import BeautifulSoup as bs

result = document.getElementById('result')
date1 = document.getElementById('date1')


async def get_status(event):
    # load the projectpro webpage content
    d = date1.value.split('-')
    tanggal, bulan, tahun = d[0], d[1], d[2]
    link = f'http://172.19.3.52/sta22/tabularmp.php?tgl={tanggal}&bln={bulan}&thn={tahun}&waktucek=Pagi&id=bmkg&session_id=NwqZNXSC'
    response = await pyfetch(url=link, method="GET", mode='no-cors')
    output = await response.string()

    convert to beautiful soup 
    soup = bs(output, 'html.parser') 
    log_station = soup.find_all('table')
    console.log(log_station)
    result.value = log_station

document.getElementById('btn1').addEventListener('click', create_proxy(get_status))