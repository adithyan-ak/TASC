import cfscrape
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

scraper = cfscrape.create_scraper()
response = scraper.get("https://iknowwhatyoudownload.com/en/peer/?ip=49.205.106.222")

soup = BeautifulSoup(response.text, 'html.parser')

downloads =soup.find(attrs={"class":"table table-condensed table-striped"})
print(downloads)
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
