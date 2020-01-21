import socket

from webosint.webosint import getDomain
from webvuln.WebVuln import getHost
from webosint.portscan import DefaultPort,Customrange
from webvuln.bruteforce import ssh,ftp


host = None
port = None


# Checking whether the target host is alive or dead
def CheckTarget():

    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((host, port))

    if  result == 0:
        return True
    else:
        return False

# Main Method
def Web(host1, port1):
    global host
    host = host1
    global port
    port = port1
    print('')
    print("Starting WAVES \n")
    print("Checking whether the Target is reachable \n")
    # calling CheckTarget method
    if CheckTarget()==True:
        print("Target Alive \n")
        print("Host : " + host)
        print("Port : %s" % port)
        Menu()
    else:
        print("The Host is Unreachable \n")
        exit()


NmapFunctions = {
    1: DefaultPort,
    2: Customrange,
}


def nmaprec(host,port):

    Choice = 1
    while True:
        print("1. Scan Default Ports (22-443)")
        print("2. Enter Custom Range")
        print("3. Back to Main Menu")
        print('')
        Choice = int(input(">> "))
        if (Choice >= 0) and (Choice < 3):
            NmapFunctions[Choice](host, port)
        elif Choice == 3:
            Menu()
        else:
            print("Please choose an Appropriate option")

BruteFunctions = {
        1: ssh,
        2: ftp
    }

def BruteForce(host, port):
    Selection = 1
    while True:
        print("1. SSH")
        print("2. FTP")
        print("3. Main Menu")
        print('')
        Selection = int(input(">> "))
        print('')
        if (Selection >= 0) and (Selection < 3):
            BruteFunctions[Selection](host, port)
        elif Selection == 3:
            Menu()
        else:
            print("Please choose an Appropriate option")

def Mainmenu():
    print()
    print("Web OSINT Report : ")
    print()
    getDomain(host, port)
    print("Web Vulnerability Report : ")
    print()
    getHost(host, port)
    return

MainFunctions = {
 1: nmaprec,
 2: BruteForce
}

try:

    def Menu():
        Selection = 1
        while True:
            Mainmenu()
            print('')
            print("1. PortScan")
            print("2. Bruteforce")
            print("3. Exit")
            print('')
            Selection = int(input(">> "))
            print('')
            if (Selection >= 0) and (Selection < 3):
                MainFunctions[Selection](host, port)
            elif Selection == 3:
                exit()
                return
            else:
                print("Incorrect Option. Returning to Main Menu")
                print()
                print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
                print()
                return

except KeyboardInterrupt as e:
    print()
    print("User Exitted")