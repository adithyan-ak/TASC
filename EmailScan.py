import requests
import json

def GetEmail(email):
    #email = input("Enter the Email : ")
    HaveIbeenPwned(email)
    print()
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print()

def HaveIbeenPwned(email):
    url = "https://haveibeenpwned.com/api/v3/breachedaccount/"+email
    header = {'hibp-api-key':'58779e4f5a4d427a9cb3175dcc3b3f58'}
    print('')
    print("Checking for Breached Data")
    print('')
    rqst = requests.get(url,headers=header,timeout=10)
    sc = rqst.status_code

    if sc == 200:
        print("The Email has been Breached")
        json_out = rqst.content.decode('utf-8', 'ignore')
        simple_out = json.loads(json_out)
        for item in simple_out:
            print('\n'
                  '[+] Breached From : ' + str(item['Name']))


    elif sc == 404:
        print('The Email is Not Breached')

    elif sc == 503:
        print('\n')
        print('[-] Error 503 : Request Blocked by Cloudflare DDoS Protection')
    elif sc == 403:
        print('\n')
        print('[-] Error 403 : Request Blocked by haveibeenpwned API')
        print(rqst.text)
    else:
        print('\n')
        print('[-] An Unknown Error Occurred')


        print(rqst.text)

