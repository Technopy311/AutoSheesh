import os



def uidCheck():
    #check that the user has root capabilities
    uid = os.getuid()
    
    """
    if uid == 0:
        pass
    else:
        print("\nThis program must be executed as root or with sudo.")
        print("Quiting...")
        exit()
    """
    
    print("UID: " + str(uid))


# nmap -sS --min-rate 5000 <ip> -n -Pn


def main():
    uidCheck()

    target = input("Write the target to scan:")    
    print("The target is: " + target)
    
    print("Scan Modes: (1)Agressive (2)Beast (3)Silent (4)Fazt all ports (5)Custom Automation")
    mode = input("Enter the selected mode: ")
    





if __name__ == '__main__':
    main()
