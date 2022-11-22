import asyncio
from playwright.async_api import async_playwright
import requests, os
from bs4 import BeautifulSoup
from inputs import *
 
alaska_dir = base_directory + 'Solicitation/tests/PDFs/Alaska'       
async def alaska1():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        # less that $200k
        await page.goto("https://dot.alaska.gov/rfpmgr/lg.cfm")
        html = await page.inner_html('body > div.container.p-0.pt-lg-2 > section')
        soup = BeautifulSoup(html, 'html.parser') 
        
        def contains_word(t):
            return t and 'pdf' in t and 'RFP' in t
        matches = soup.find_all('a', text=contains_word)
       
        pdf_links = []
        for match in matches:
            link = 'https://dot.alaska.gov' + match.get('href')
            pdf_links.append(link) 

        os.chdir(alaska_dir)
        for pdf_url in pdf_links: 
            name  = pdf_url.split("/")[-1]
            r = requests.get(pdf_url) 
            with open(name.split('pdf')[-2] + '.pdf' ,'wb') as f:
                f.write(r.content)
        print('Alaska is done')

        await browser.close()

            
            
        
