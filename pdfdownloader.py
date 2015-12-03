__author__ = 'Shashi'
import requests
import bs4
import urllib



def pdfdownloader(url):
    header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}

    response = requests.get(url,headers=header)

    #print response.text
    download=False
    soup = bs4.BeautifulSoup(response.text)
    for link in soup.find_all('a'):

        if '.pdf' in (link.get('href')):
            print "Saving now: " + link.get('href').split('/')[-1]
            testfile = urllib.URLopener()
            testfile.retrieve("http://www.tutorialspoint.com"+link.get('href'), link.get('href').split('/')[-1])
            download=True
        if download:
            pdfdownloader("http://www.tutorialspoint.com"+link.get('href'))


start=raw_input("Enter the starting URL for the tutorial: ") #Enter the url of starting tutorial
pdfdownloader(start)