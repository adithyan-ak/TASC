from bs4 import BeautifulSoup
import requests, urllib,re
from PIL import Image, ImageTk
import tkinter as tk

def DomainMap(host):

    if 'www' in host:
        host = str(host)
        host = host.replace("www",'')

    r = requests.get("https://dnsdumpster.com/")
    c = r.content

    soup = BeautifulSoup(c, 'lxml')

    csrf = soup.find('input').get('value')
    csrf.strip()

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Origin': 'https://dnsdumpster.com',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://dnsdumpster.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    data = {
      'csrfmiddlewaretoken': csrf,
      'targetip': host
    }

    cookies = {
        'csrftoken': csrf,
    }

    response = requests.post('https://dnsdumpster.com/', headers=headers, cookies=cookies, data=data)

    soup = BeautifulSoup(response.text, 'html.parser')

    dom_map = soup.find(attrs={"class": "img-responsive"})

    dom_map = str(dom_map)

    map_link = re.findall(r'src="(.*?)"', dom_map)

    for i in map_link:

        map_link = "https://dnsdumpster.com"+i

    urllib.request.urlretrieve(map_link, "Map.png")

    #image_window = tk.Tk()
    #img = ImageTk.PhotoImage(Image.open('map.png'))
    #panel = tk.Label(image_window, image=img)
    #panel.pack(side="bottom", fill="both", expand="yes")
    #image_window.mainloop()

DomainMap("www.skcet.ac.in")