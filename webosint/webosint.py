import requests, socket
import dns.resolver

def getDomain(host, port):
    host = host
    port = port
    DomainRecon(host,port)
    nsLookup(host, port)
    SubDomain(host, port)
    CMSdetect(host, port)

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


