import os
import csv

def setup():
    file = open('addressList.csv')
    addresses = list(csv.reader(file))
    return addresses

def addConnection():
    try:
        os.system('clear')
        hostname = input("Username: ")
        ip = input("Address: ")
        display = input("Display Name (max length 15): ")
        while(len(display) > 15):
            print("Display name too long")
            display = input("Display Name (max length 15): ")
        addresses.append([display, hostname, ip])
        with open('addressList.csv', 'wt') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows([[display, hostname, ip]])
    except KeyboardInterrupt:
        return None

def removeConnection():
    try:
        os.system('clear')
        displayConnections()
        index = input("Type index of connection you would like to remove: ")
        if(index != ""):
            print("Removed "+addresses[int(index)][0])
            addresses.pop(int(index))
        else:
            print("Invalid index")
        input("Press ENTER to continue...")
    except KeyboardInterrupt:
        return None

def connectToHost():
    try:
        os.system('clear')
        displayConnections()
        index = int(input("Connect to: "))
        command = 'ssh '+addresses[index][1]+'@'+addresses[index][2]
        try:
            os.system(command)
        except OSError:
            print("Command incorrect!")
            input("Press ENTER to continue...")
    except KeyboardInterrupt:
        return None

def displayConnections():
    try:
        os.system('clear')
        print("Address List:")
        for i in range(len(addresses)):
            gap = 20 - len(addresses[i][0])
            print(str(i)+": "+addresses[i][0]+" "*gap+addresses[i][1]+"@"+addresses[i][2])
        print("")
    except KeyboardInterrupt:
        return None

while True:
    try:
        addresses = setup()
        os.system('clear')
        print("/////////////////////")
        print("//     EasySSH     //")
        print("// By Walker Davis //")
        print("/////////////////////")
        print("")
        print("0: Connect To Host")
        print("1: Add Connection")
        print("2: Remove Connection")
        print("3: Display Connections")
        choice = input(">>> ")
        if(choice == "0"):
            connectToHost()
        elif(choice == "1"):
            addConnection()
        elif(choice == "2"):
            removeConnection()
        elif(choice == "3"):
            displayConnections()
            input("Press ENTER to continue...")
        elif(choice == "!quit"):
            print("\nQuitting...")
            break
    except KeyboardInterrupt:
        print("\nQuitting...")
        break
