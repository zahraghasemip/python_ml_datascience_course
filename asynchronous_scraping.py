import aiohttp 
import asyncio
from bs4 import BeautifulSoup
import csv 
import re
import nest_asyncio 
nest_asyncio.apply()

async def scrape_and_save_links(text):
    soup = BeautifulSoup(text , 'html.parser')
    file = open('csv_file' , 'a' , newline='')
    writer = csv.writer(file, delimiter=',')
    for link in soup.find_all('a' , href=True):
        href = link.get('href')
        if href and re.match('^http', href):
            writer.writerow([href])
    file.close()

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            text = await response.text()
            task = asyncio.create_task(scrape_and_save_links(text))
            await task
    except Exception as e:
        print(str(e))

async def scrap(urls):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session,url))
        await asyncio.gather(*tasks)
urls = ['https://www.python.org/','https://www.wikipedia.org/','https://www.google.com/']
asyncio.run(scrap(urls=urls))