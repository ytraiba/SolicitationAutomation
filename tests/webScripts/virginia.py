from playwright.async_api import async_playwright
import requests, os, asyncio
from bs4 import BeautifulSoup 
from inputs import *
import warnings
warnings.filterwarnings("ignore")
 
virginia_dir = base_directory + 'Solicitation/tests/PDFs/Virginia'

async def virginia1():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.virginiadot.org/business/rfps.asp")
        html = await page.inner_html('#topCopy')
        soup = BeautifulSoup(html, 'html.parser') 
        
        def contains_scope(t):
            return t and 'Scope' in t 
        Scopes = soup.find_all('a', text=contains_scope)
        

        matches = Scopes 
        pdf_links = []
        for match in matches:
            # print(match.get('href'))
            link = 'https://www.virginiadot.org' + match.get('href')
            pdf_links.append(link) 

        os.chdir(virginia_dir)
        for pdf_url in pdf_links: 
            try:
                name  = pdf_url.split("/")[-1]
                r = requests.get(pdf_url, verify=False) 
                with open(name,'wb') as f:
                    f.write(r.content)
            except:
                print('')
        print('Virginia is done')
        
        await browser.close()