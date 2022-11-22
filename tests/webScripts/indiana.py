from cgitb import text
from playwright.async_api import async_playwright
import requests, os
from bs4 import BeautifulSoup 
from inputs import *

indiana_dir = base_directory + 'Solicitation/tests/PDFs/Indiana'
async def indiana1():
    async with async_playwright() as p:
        browser = await p.firefox.launch()
        page = await browser.new_page()
        await page.goto("https://www.in.gov/ifa/requests-for-proposalsqualificationsinformation/")
        html = await page.inner_html('#container_main > main')
        soup = BeautifulSoup(html, 'html.parser') 
        

        def contains_words(t):
            return t and 'RFP' in t
        matches = soup.find_all('a', text=contains_words)

        pdf_links = []
        for match in matches:
            link = match.get('href')
            link = 'https://www.in.gov/ifa/files/' + link.split('/')[-1]
            pdf_links.append(link)

        for pdf_url in pdf_links: 
            name  = pdf_url.split("/")[-1]
            if pdf_url.split('.')[-1] == 'pdf':
                r = requests.get(pdf_url) 
                os.chdir(indiana_dir)
                with open(name,'wb') as f:
                    f.write(r.content) 

        print('Indiana is done')

        await browser.close()
       