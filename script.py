from pyodide.http import pyfetch
from pyodide import create_proxy
import asyncio
from js import document, console

async def fetch_data(event):
    response = await pyfetch(url="https://jsonplaceholder.typicode.com/", method="GET")

    output = await response.string()
    # document.getElementById('request_output').innerHTML = output
    console.log(output)

document.getElementById('btn-test').addEventListener('click', create_proxy(fetch_data))