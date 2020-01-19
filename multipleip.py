import requests
import IP2Proxy, IP2Location
import gmplot
from src.api import ipstackapi
import webbrowser

api_key = ipstackapi()

def get_ip():
    """
    Returns a list of IP addresses from a file containing one IP per line.
    """
    print('''Choose
    1) Trace single IP 
    2) Trace Multiple IPs''')
    choice = input(">> ")

    if choice == '1':
        ip = input("Enter the IP : ")
        iptrace(ip)
    elif choice == '2':
        ip_file = input("Enter the IP File Location : ")
        read_multiple_ip(ip_file)
    else:
        print()
        print("Incorrect Option. Going back to Main Menu")
        print()
        print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
        print()
        return

    print()
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print()

def iptrace(ip):

    database = IP2Location.IP2Location()
    database.open("src/IP2LOCATION-LITE-DB11.BIN")
    loc = database.get_all(ip)
    print("IP : "+ip)
    print("City : " + loc.city)
    print("State : " + loc.region)
    print("Country : " + loc.country_long)

    proxy = IP2Proxy.IP2Proxy()

    # open IP2Proxy BIN database for proxy lookup
    proxy.open("src/IP2PROXY-LITE-PX8.BIN")

    record = proxy.get_all(ip)

    isproxy = str(record['is_proxy'])


    if isproxy=='1':

        print ('Proxy : Yes')
        if record['proxy_type'] == "PUB":
            print("Proxy Type : Public")
        else:
            print ('Proxy Type: ' + record['proxy_type'])

        print ('ISP : ' + record['isp'])
        print ('Domain : ' + record['domain'])
        print ('Usage Type : ' + record['usage_type'])
        print ('ASN : ' + record['asn'])
        print ('Company Name : ' + record['as_name'])

    else:
        pass

    lats = []
    lons = []
    r = requests.get("http://api.ipstack.com/" + ip + "?access_key=" + api_key)
    resp = r.json()
    print("Latitude : {longitude}".format(**resp))
    print("Longitude : {longitude}".format(**resp))
    if resp['latitude'] and resp['longitude']:
        lats = resp['latitude']
        lons = resp['longitude']

    maps_url = "https://maps.google.com/maps?q=%s,+%s" % (lats, lons)
    openWeb = input("Open GPS location in web broser? (Y/N) ")
    if openWeb.upper() == 'Y':
        webbrowser.open(maps_url, new=2)
    else:
        print()
        get_ip()

    proxy.close()
    database.close()



def read_multiple_ip(ip_file):
    lats = []
    lons = []
    f = open(ip_file, "r")
    f1 = f.readlines()
    for line in f1:
        r = requests.get("http://api.ipstack.com/" + line + "?access_key=" + api_key)
        resp = r.json()
        if resp['latitude'] and resp['longitude']:
            lats.append(resp['latitude'])
            lons.append(resp['longitude'])
    heat_map(lats,lons)

def heat_map(lats,lons):
    gmap3 = gmplot.GoogleMapPlotter(20.5937, 78.9629, 5)
    # Plot method Draw a line in
    # between given coordinates
    gmap3.heatmap(lats,lons)
    gmap3.scatter(lats,lons, '#FF0000', size=50, marker=False)

    gmap3.plot(lats,lons, 'cornflowerblue', edge_width = 3.0)
    gmap3.apikey = "AIzaSyDmpwQtMwmoWGHX2UBqnAldc8CFDus77RQ"
    save_location = input("Enter a location to save : ")
    location = save_location + "/heatmap.html"
    gmap3.draw(location)
    print("Heatmap saved at " + location)
    openWeb = input("Open Heatmap in web broser? (Y/N) : ")
    if openWeb.upper() == 'Y':
        webbrowser.open(url=("file:///"+location))
    else:
        print()
        print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
        print()
        get_ip()



