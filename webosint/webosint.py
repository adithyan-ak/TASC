import  socket
import dns.resolver
from bs4 import BeautifulSoup
import requests, urllib,re
from PIL import Image, ImageTk
import tkinter as tk

def getDomain(host, port):
    host = host
    port = port
    GetWhois(host)
    DomainRecon(host,port)
    nsLookup(host, port)
    SubDomain(host, port)
    CMSdetect(host, port)
    DomainMap(host)

def GetWhois(host):
    url = "https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=at_zAh8wGadGEvLZQE9pTi1KWGLkL1oX&domainName="+host
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="lxml")
    data = soup.find('strippedtext').text
    print("WHOIS Data : ")
    print()
    print(data)
    print()
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print()

def DomainRecon(domain,port):

    if port == 80:
          port = 'http://'
    elif port == 443:
          port = 'https://'
    else:
         print("Could'nt fetch data for the given PORT")
    print("Domain : "+domain)
    DomainRecords(domain)
    getHeaders(port+domain)
    print()
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print()


def getHeaders(domain):
    print()
    headers = requests.get(domain).headers
    server = ''
    print('[-] HTTP-response header:\n---')
    for key,value in headers.items():
        print('\t' + key + ': ' + value)

        if key == 'Server':
            server = value

    if server:
        print('---\n[-] Webserver detected: ' + server)
    else:
        print('---\n[!] No "Server"-header')

def DomainRecords(domain):
    domain = str(domain)
    ip = []
    ipr = dns.resolver.query(domain, 'A')
    for rdata in ipr:
        ip.append(rdata.to_text())
    try:
        for ip in ip:
            print("IP : "+ip)
            getIPwhois(ip)
    except:
        pass

    mxrecords = []
    mxr = dns.resolver.query(domain, 'MX')
    for rdata in mxr:
        mxrecords.append(rdata.to_text())
    print("MX Records : ")
    for mx in mxrecords:
        print(mx)

    cname = []
    cnamer = dns.resolver.query(domain, 'CNAME')
    for rdata in cnamer:
        cname.append(rdata.to_text())
    for cname in cname:
        print("CNAME : " + cname)

def getIPwhois(ip):
    print("IP Whois Details : ")
    response = requests.get("https://ipapi.co/"+ip+"/json")
    resp = response.json()
    org = resp['org']
    print("Organization : " + org)
    city = resp['city']
    print("City : "+city)
    region = resp['region']
    print("Region : "+region)
    country_name = resp['country_name']
    print("Country : "+country_name)
    postal = resp['postal']
    print("Postal Code : "+postal)


def nsLookup(host, port):
    reversed_dns = socket.gethostbyaddr(host)
    print("Reverse IP :")
    print()
    i = 1
    for z in reversed_dns:
        print(i, end='. ')
        print(z)
        i = i+1
    print()
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print()




def CMSdetect(domain, port):
    payload = {'key': '1641c3b9f2b1c8676ceaba95d00f7cf2e3531830c5fa9a6cc5e2d922b2ed7165dcce66', 'url': domain}
    cms_url = "https://whatcms.org/APIEndpoint/Detect"
    response = requests.get(cms_url, params=payload)
    cms_data = response.json()
    cms_info = cms_data['result']
    print("CMS Detection Results : ")
    print()
    if cms_info['code'] == 200:
        print('Detected CMS     : %s' % cms_info['name'])
        print('Detected Version : %s' % cms_info['version'])
        print('Confidence       : %s' % cms_info['confidence'])
    else:
        print(cms_info['msg'])
        print('Detected CMS : %s' % cms_info['name'])
        print('Detected Version : %s' % cms_info['version'])

    print()
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print()


def SubDomain(host, port):

    url = 'https://www.virustotal.com/vtapi/v2/domain/report'

    params = {'apikey':'1af37bfeb7b1628ba10695fb187987a6651793e37df006a5cdf8786b0e4f6453','domain':host}

    response = requests.get(url, params=params)

    subdomains = response.json()
    print("Subdomains : ")
    print()
    i = 1
    for x in subdomains['domain_siblings']:
        print(i,end='. ')
        print(x)
        i = i+1

    print()
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print()

def DomainMap(host):

    try :

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
        print("Domain Map has been saved as Map.png")
        print()
        print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
        print()

        #image_window = tk.Tk()
        # img = ImageTk.PhotoImage(Image.open('map.png'))
        #panel = tk.Label(image_window, image=img)
        #panel.pack(side="bottom", fill="both", expand="yes")
        #image_window.mainloop()

    except:
        pass

