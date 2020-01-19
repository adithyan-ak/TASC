from src.api import phoneapis
import requests

def carrierlookup(phonenum):
    #phonenum = input("Enter Mobile Number with country code : ")
    api_key = phoneapis()
    url1 = ("http://apilayer.net/api/validate?access_key="+api_key+"&number="+phonenum)
    resp = requests.get(url1)
    details = resp.json()
    print('')
    # PWD = "uTb5-CYC%-WTqm-MBaY-!aAT-ApSq"
    # devansh76-api-3874a453262b

    Full_url = 'https://www.hlr-lookups.com/api?action=submitSyncLookupRequest&msisdn=' + phonenum + '&username=kirannk22&password=lokiNK854'

    response = requests.get(url=Full_url)

    dict = response.json()

    results = dict['results']

    Finalresults = results[0]

    if Finalresults['isvalid'] == 'Yes':
        print("Valid : Yes")

    subscriber_status = Finalresults['subscriberstatus']

    if subscriber_status == "SUBSCRIBERSTATUS_CONNECTED":
        print("Subscriber Status : Connected")

    else:
        print("Subscriber Status : Error")
        exit()

    IMSI = Finalresults['imsi']
    print("IMSI : " + IMSI)

    MCCMNC = Finalresults['mccmnc']
    print("MCCMNC : " + MCCMNC)

    originalnetwork = Finalresults['originalnetworkname']
    print("Original Network : " + originalnetwork)

    print("State : "+ details['location'])

    originalcountry = Finalresults['originalcountryname']
    print("Country : " + originalcountry)

    roaming = Finalresults['isroaming']
    print("Roaming : " + roaming)

    if roaming == "Yes":
        roamingnetwork = Finalresults['roamingnetworkname']
        print("Roaming Network : " + roamingnetwork)

        roamingcountry = Finalresults['roamingcountryname']
        print("Roaming Country : " + roamingcountry)

    else:
        print("Roaming Country : None")

    ported = Finalresults['isported']
    print("Ported : " + ported)

    if ported == 'Yes':
        portednetworkname = Finalresults['portednetworkname']
        print("Ported Network : " + portednetworkname)

    print()
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print()