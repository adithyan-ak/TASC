import requests, os, socket



def getDomain(host, port):
    host = host
    port = port
    Whois(host,port)
    nsLookup(host, port)
    SubDomain(host, port)
    CMSdetect(host, port)



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
    print("MX Records :")
    print()
    nslook = os.system("nslookup -query=mx %s"% host)
    print()
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print()

    print("Name Server Records : ")
    os.system("nslookup -query=ns %s"% host)
    print()
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print()

    print("Start of Authority Records : ")
    print()
    os.system("nslookup -query=soa %s" % host)
    print()
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print()


def Whois(host, port):
    print()
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print()
    print("WHOIS Details")
    print()
    os.system('whois %s'%host)
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


