import requests
import re,json
import dns.resolver

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


DomainRecon("www.skcet.ac.in",80)

