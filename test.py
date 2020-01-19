from username import NameUser,Facebook,ScrapTweets,Instgram
from EmailScan import GetEmail
from phonenum import carrierlookup
from torrenttracker import tracktorrent
#from web import Web
from metadata import gps_analyzer
from reverseimg import reverseImg
from multipleip import read_multiple_ip
from iplookup import iptrace, tracktorrent
from maclookup import macLookup
#from sentiment import GetTweet
from fbkeyword import FacebookScrapper
from newweb import Web

def MainMenu():
        username = input("Enter the Username : ")
        print()
        if username != '':
                print("Facebook Information : ")
                Facebook(username)
                print("Twitter Information : ")
                ScrapTweets(username)
                print("Instagram Information : ")
                Instgram(username)
                return
        phonenum = input("Enter the Phone Number with country code : ")
        print()
        if phonenum != '':
                print()
                print("Phone Number Information : ")
                carrierlookup(phonenum)
        email = input("Enter the Email : ")
        print()
        if email != '':
                GetEmail(email)
        ip = input("Enter the IP : ")
        print()
        if ip != '':
                iptrace(ip)
                tracktorrent(ip)
        domain = input("Enter the Domain : ")
        print()
        if domain != '':
                port = int(input("Enter the port : "))
                Web(domain, port)
        keyword = input("Enter the Keyword to scrap : ")
        print()
        if keyword !='':
                FacebookScrapper(keyword)
        return





MainFunctions = {
    1: gps_analyzer,
    2: reverseImg,
    3: read_multiple_ip,
    4: macLookup
  #  11: GetTweet
}

banner = '''
                ████████╗ █████╗ ███████╗ ██████╗
                ╚══██╔══╝██╔══██╗██╔════╝██╔════╝
                   ██║   ███████║███████╗██║     
                   ██║   ██╔══██║╚════██║██║     
                   ██║   ██║  ██║███████║╚██████╗
                   ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝

                Threat Analysis & Surveillance Cell'''

print(banner)

try:
    def Menu():
        Selection = 1
        while True:

            MainMenu()

         #   print("1. Username")
          #  print("2. Phone Number")
          #  print("3. Email")
          #  print("4. Torrent Tracker")
          #  print("5. Facebook Keyword Analyzer")
           # print("6. Domain")
            print("1. Metadata Analyzer")
            print("2. Reverse Image Search")
            print("3. IP Heatmap")
            print("4. Mac Address Lookup")
         #   print("5. Sentiment Analysis")
            print("5. Exit")
            print('')
            Selection = int(input(">> "))
            print('')
            if (Selection == 1):
                MainFunctions[Selection]()
            elif (Selection == 2):
                MainFunctions[Selection]()
            elif (Selection == 3):
                ip_file = input("Enter the location of the IP file : ")
                MainFunctions[Selection](ip_file)
            elif (Selection == 4):
                MainFunctions[Selection]()
            elif Selection == 5:
                exit()
            else:
                print("Please choose an Appropriate option")


    if __name__ == "__main__":
        Menu()

except KeyboardInterrupt as e:
    print()
    print("User Exitted")