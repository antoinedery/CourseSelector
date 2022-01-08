from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = 'https://www.polymtl.ca/public/Horaire/fermes.csv'

req = Request(url, headers={'User-Agent':'Chrome'})
webpage = urlopen(req).read()

page = BeautifulSoup(webpage, "html.parser")
print(page)