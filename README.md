# Web_Scraper_Using_Django

Step1:
Download pip install requests - requests is used to send requests to websites we will be scraping
and pip install beautifulsoup4 - beautifulsoup is a Python library that helps extract data from HTML and XML Codes.


Step2 : To check the working of BeautifulSoup and requests in interactive python shell in command prompt:
        1.import request                                #import the request library
        2.page=request.get('http://www.google.com')     #sends request to the google.com or the url given in the get function
        3.page.text

        from bs4  import beautifulsoup
        soup=Beautifulsoup(page.text,'htmlparser')      #get links from the url to which request is sent.
        soup
     
Step 3  : Formatting Or ways to extract links in a better/ readble manner or by attributes as parameters

         for link in soup.find_all('a'):                #prints links of 'a' tag
              print(link)
              
              
         #To print links of href 
         
         for link in soup.find_all('a'):
             print(link.get('href'))
Step 4: Now we makes views function where we request for links (web scraping) saves it in a list and connects the view function to urls.py (correct path) and templates like 
SCRAPER/result.html is used where the formatting is done .(The way in which links will be displayed.)

#Do not forget to add your app to setting.py otherwise templates will not be recognised.

Code 
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup   #BeautifulSoup imported


def scraper(request):
    page= requests.get('https://www.github.com')
    soup=BeautifulSoup(page.text,'html.parser')

    list_address=[]
    for link in soup.find_all('a'):
        list_address.append(link.get('href'))      #links are appended to list

    return render(request,'SCRAPER/result.html',{'list_address': list_address})
    
