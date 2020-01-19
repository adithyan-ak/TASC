
from username import NameUser
from EmailScan import GetEmail
from phonenum import carrierlookup
from torrenttracker import tracktorrent
from web import Web
from metadata import gps_analyzer
from reverseimg import reverseImg
from multipleip import get_ip
from maclookup import macLookup
from sentiment import GetTweet
from fbkeyword import FacebookScrapper

MainFunctions={
 1: NameUser,
 2: carrierlookup,
 3: GetEmail,
 4: tracktorrent,
 5: FacebookScrapper,
 6: Web,
 7: gps_analyzer,
 8: reverseImg,
 9: get_ip,
 10: macLookup,
 11: GetTweet
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

            print("1. Username")
            print("2. Phone Number")
            print("3. Email")
            print("4. Torrent Tracker")
            print("5. Facebook Keyword Analyzer")
            print("6. Domain")
            print("7. Metadata Analyzer")
            print("8. Reverse Image Search")
            print("9. IP Heatmap")
            print("10. Mac Address Lookup")
            print("11. Sentiment Analysis")
            print("12. Exit")
            print('')
            Selection = int(input(">> "))
            print('')
            if (Selection == 1):
                MainFunctions[Selection]()
            elif (Selection == 2):
                MainFunctions[Selection]()
            elif (Selection == 3):
                MainFunctions[Selection]()
            elif (Selection == 4):
                MainFunctions[Selection]()
            elif (Selection == 5):
                MainFunctions[Selection]()
            elif Selection == 6:
                MainFunctions[Selection]()
            elif Selection == 7:
                MainFunctions[Selection]()
            elif Selection == 8:
                MainFunctions[Selection]()
            elif Selection == 9:
                MainFunctions[Selection]()
            elif Selection == 10:
                MainFunctions[Selection]()
            elif Selection == 11:
                MainFunctions[Selection]()
            elif Selection == 12:
                exit()
            else:
                print("Please choose an Appropriate option")


    if __name__ == "__main__":
        Menu()

except KeyboardInterrupt as e:
    print()
    print("User Exitted")