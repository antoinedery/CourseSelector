from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def createCoursesDictionary():
    url = 'https://www.polymtl.ca/public/Horaire/horsage.csv'
    req = Request(url, headers={'User-Agent':'Chrome'})
    webpage = urlopen(req).read()
    tempArray = {}
    createCoursesDictionary.courses = {}
    page = str(BeautifulSoup(webpage, "html.parser")).splitlines()
    for i in range(1, len(page)):
        page[i] = page[i][3:]
        tempArray = page[i].split(';')
        createCoursesDictionary.courses[tempArray[0]] = int((float(tempArray[2].replace(',','.'))))