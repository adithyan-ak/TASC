from urllib.request import urlopen
import requests

header1 = None
domain2 = None
header2 = None
domain3 = None
header3 = None


def getHost(host, port):
    host = host
    port = port
    ClickJacking(host, port)
    Cors(host, port)
    HostHeader(host, port)


def ClickJacking(host, port):
    print("Scanning for Clickjacking Vulnerability ....")
    print()
    if port == 80:
          port = 'http://'
    elif port == 443:
          port = 'https://'
    else:
         print("Could'nt fetch data for the given PORT")


    url = (port+host)

    data = urlopen(url)
    headers = data.info()

    if not "X-Frame-Options" in headers:
          print("Website is vulnerable to ClickJacking")
          print()
          print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
          print()

    else:
        print("Website is not Vulnerable to ClickJacking")
        print()
        print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
        print()

def Cors(host, port):
    print("Scanning for Cross Origin Resource Sharing ....")
    print()
    if port == 80:
        port = 'http://'
    elif port == 443:
        port = 'https://'
    else:
        print("Could'nt fetch data for the given PORT")
        exit()
    print("1. CORS check in Default Host")
    print("2. CORS check in Host's Custom Endpoint")
    print('')
    choice = int(input('>> '))
    print('')
    cookies = input("Paste the Cookies (If None,then hit enter) : ")
    print()
    global header1
    global domain2
    global header2
    global domain3
    global header3
    if cookies == '':

        header1 = {'Origin': 'http://evil.com'}

        domain2 = host + '.evil.com'

        header2 = {'Origin': port + domain2}

        domain3 = host + '%60cdl.evil.com'

        header3 = {'Origin': port + domain3}

        Choices(host, port, choice)
    else:

        header1 = {'Origin': 'http://evil.com', 'Cookie': cookies}

        domain2 = host + '.evil.com'

        header2 = {'Origin': port + domain2,'Cookie': cookies}

        domain3 = host + '%60cdl.evil.com'

        header3 = {'Origin': port + domain3,'Cookie': cookies}

        Choices(host, port, choice)


def Choices(host, port, choice):
    if choice == 2:
        endpoint = input("Enter the Custom Endpoint : ")
        host = endpoint
        WrongChoice(host, port)

    elif choice == 1:
        print("Checking Default Host ")
        print()
        url = (port + host)
        print("Testing with Payload %s" % header1)
        response = requests.get(url, headers=header1)
        if 'evil.com' in response.headers:
            print("Vulnerable to Cross Origin Resource Sharing")
        else:
            print("Not Vulnerable to Cross Origin Resource Sharing")
        print('')

        print("Testing with Payload %s" % header2)
        response = requests.get(url, headers=header2)

        if domain2 in response.headers:
            print("Vulnerable to Cross Origin Resource Sharing")
        else:
            print("Not Vulnerable to Cross Origin Resource Sharing")
        print('')

        print("Testing with Payload %s" % header3)
        response = requests.get(url, headers=header3)
        if domain2 in response.headers:
            print("Vulnerable to Cross Origin Resource Sharing")
        else:
            print("Not Vulnerable to Cross Origin Resource Sharing")
        print('')


    else:
        print("Wrong Choice")
        print("Checking Default Host")
        WrongChoice(host, port)

    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print()

def WrongChoice(host, port):
    url = (port + host)
    print("Testing with Payload %s" % header1)
    response = requests.get(url, headers=header1)
    if 'evil.com' in response.headers:
        print("Vulnerable to Cross Origin Resource Sharing")
    else:
        print("Not Vulnerable to Cross Origin Resource Sharing")
    print('')

    print("Testing with Payload %s" % header2)
    response = requests.get(url, headers=header2)

    if domain2 in response.headers:
        print("Vulnerable to Cross Origin Resource Sharing")
    else:
        print("Not Vulnerable to Cross Origin Resource Sharing")
    print('')

    print("Testing with Payload %s" % header3)
    response = requests.get(url, headers=header3)
    if domain2 in response.headers:
        print("Vulnerable to Cross Origin Resource Sharing")
    else:
        print("Not Vulnerable to Cross Origin Resource Sharing")

    print('')
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print()


def HostHeader(host, port):

    print("Scanning for Host Header Injection ....")
    print()
    if port == 80:
        port = 'http://'
    elif port == 443:
        port = 'https://'
    else:
        print("Could'nt fetch data for the given PORT")
    url = (port + host)
    headers = {'Host': 'http://evil.com'}
    response = requests.get(url, headers=headers)
    if 'evil.com' in response.headers:
        print("Vulnerable to Host Header Injection")
    else:
        print("Not Vulnerable to Host header injection")

    print('')
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print()
