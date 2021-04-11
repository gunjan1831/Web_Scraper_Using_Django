from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def scraper(request):
    page= requests.get('https://www.google.com')
    soup=BeautifulSoup(page.text,'html.parser')

    list_address=[]
    for link in soup.find_all('a'):
        list_address.append(link.get('href'))

    return render(request,'SCRAPER/result.html',{'list_address': list_address})

