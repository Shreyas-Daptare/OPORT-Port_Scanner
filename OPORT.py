#!/bin/python3
import sys
import socket
from datetime import datetime
def banner():
    print("-" * 50)
    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("Please be patient......")
    print("-" * 50)

def scanner(target,start_port,end_port):
    print("-" * 50)
    print("Results: ")
    ports_found = 0
    for port in range(start_port, end_port):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} is open".format(port))
            ports_found=ports_found + 1
        s.close()
    if ports_found == 0:
        print("No Open port found !!")
    print("")
    print("Scanning Completed :)")
    print("-" * 50)
    print("\n Thank you for using Port Scanner")
def live_scanner(target,start_port,end_port):
    print("-" * 50)
    print("Live Results: ")
    ports_found = 0
    for port in range(start_port, end_port):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print("** Port {} is open".format(port))
            ports_found=ports_found + 1
        else:
            print("-- Port {} is not open".format(port))
        s.close()
    if ports_found == 0:
        print("No Open port found !!")
    print("")
    print("Scanning Completed :)")
    print("-" * 50)
    print("\n Thank you for using Port Scanner")
def invalidport():
    print("Invalid port, Enter a port between 1 and 65535 and try again")
    sys.exit()
def live_choice():
    usr_choice=input("Do you want to see live scanning? (y/n): ")
    if usr_choice == "y" or usr_choice == "Y":
        return "y"
    elif usr_choice == "n" or usr_choice== "N":
        return "n"
    else:
        print("Invalid Choice!!, Try again")
        sys.exit()
print("-" * 50)
print("              Welcome to Port Scanner")
print("-" * 50)
target = socket.gethostbyname(input("Enter an IP address or host name: "))
print("Select option for preferred scan")
print("1: Normal scan, note this process will be slow, as it'll find open ports from 1 to 65535")
print("2: Specified scan, note this process requires the start port and end port for the scan")
print("3: To check a single port, note this process requires a specified host")
print("4: Exit")
choice=int(input("Chosen option: "))

try:
    if choice==1:
        start_port=1
        end_port=65535
        usr_choice=live_choice()
        if usr_choice=="y":
            banner()
            live_scanner(target,start_port,end_port)
        elif usr_choice=="n":
            banner()
            scanner(target,start_port,end_port)
    elif choice==2:
        start_port=int(input("Enter start port: "))
        if ((start_port>=1 and start_port<=65535)==False):
            invalidport()
        end_port=int(input("Enter end port: "))
        if ((end_port>=2 and end_port<=65536)==False):
            invalidport()
        usr_choice = live_choice()
        if usr_choice == "y":
            banner()
            live_scanner(target, start_port, end_port + 1)
        elif usr_choice == "n":
            banner()
            scanner(target, start_port, end_port + 1)

    elif choice==3:
        start_port=int(input("Enter port: "))
        if start_port>=1 and start_port<=65535:
            end_port=start_port + 1
            banner()
            live_scanner(target,start_port,end_port)
        else:
            invalidport()
    elif choice==4:
        print("Exiting Program !!!!")
        sys.exit()
    else:
        print("Invalid choice! || Rerun the program and choose the right option!")
except KeyboardInterrupt:
    print("\n Exiting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("\ Server not responding !!!!")
    sys.exit()
