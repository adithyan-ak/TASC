
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup


def tracktorrent():

    headers = {
        '$Host': 'iknowwhatyoudownload.com',
        '$User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15',
        '$Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        '$Accept-Language': 'en-US,en;q=0.5',
        '$Accept-Encoding': 'gzip, deflate',
        '$Connection': 'close',
        '$Referer': 'https://iknowwhatyoudownload.com/en/peer/',
        '$Upgrade-Insecure-Requests': '1',
    }

    ip = input("Enter IP to track torrents : ")

    params = (
        ('ip', ip),
    )

    response = requests.get('http://iknowwhatyoudownload.com/en/peer/', headers=headers, params=params, verify=False)

    soup = BeautifulSoup(response.text, 'html.parser')

    downloads =soup.find(attrs={"class":"table table-condensed table-striped"})

    final = downloads.find_all(attrs={"class":"name-column"})
    size = downloads.find_all(attrs={"class":"size-column"})
    date = downloads.find_all(attrs={"class":"date-column"})
    categ = downloads.find_all(attrs={"class":"category-column"})

    print("")
    if final == []:
        print("No Download data found")
    else:
        print("Downloaded Files : ")
        print("")

        i = 0

        for z in final:

            name = z.get_text()
            siz = size[i].get_text()
            dates = date[i].get_text()
            category = categ[i].get_text()
            file_name = name.strip()
            print(i+1,end='. ')
            print("Title : "+file_name)
            print("   Category : "+category)
            print("   Size : "+siz)
            print("   Date : "+dates)

            print()
            i = i+1

        print()
        print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
        print()
