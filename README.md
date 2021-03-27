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
