import numpy as np
import os
import subprocess

addresses = [['macbook air','walkerdavis', '10.199.11.32'],
             ['test', 'username', 'hostname']]

def addConnection():
    hostname = input("Username: ")
    ip = input("Address: ")
    display = input("Display Name (max length 15): ")
    if(len(display) > 15):
        print("Display name too long")
        input("Press ENTER to continue...")
        return None
    addresses.append([display, hostname, ip])

def connectToHost():
    index = int(input("Connect to: "))
    command = 'ssh '+addresses[index][1]+'@'+addresses[index][2]
    try:
        os.system(command)
    except OSError:
        print("Command incorrect!")
        input("Press ENTER to continue...")

def displayConnections():
    os.system('clear')
    print("Address List:")
    for i in range(len(addresses)):
        gap = 20 - len(addresses[i][0])
        print(str(i)+": "+addresses[i][0]+" "*gap+addresses[i][1]+"@"+addresses[i][2])
    print("")

while True:
    try:
        os.system('clear')
        print("0: Connect To Host")
        print("1: Add Connection")
        print("2: Display Connections")
        choice = input(">>> ")
        if(choice == "0"):
            displayConnections()
            connectToHost()
        elif(choice == "1"):
            addConnection()
        elif(choice == "2"):
            displayConnections()
            input("Press ENTER to continue...")
    except KeyboardInterrupt:
        print("\nQuitting...")
        break
