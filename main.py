import os



def uidCheck():
    #check that the user has root capabilities
    uid = os.getuid()
    
    if uid == 0:
        pass
    else:
        print("\nThis program must be executed as root or with sudo.")
        print("Quiting...")
        exit()
    
    print("Running with this UID: " + str(uid))


def Aggressive(target):
    pass


def Beast(target):
    pass


def Silent(target):
    pass


def FastPorts(target):
    pass


def Custom(target):
    pass


def GodScan(target):
    pass
# nmap -sS --min-rate 5000 <ip> -n -Pn


def main():
    uidCheck()

    target = input("Write the target to scan:")    
    print("The target is: " + target)
    
    print("\n")
    print("\n")
    print("Scan Modes:\n(1)Agressive (2)Beast (3)Silent ")
    print("(4)Fazt all ports (5)Custom Automation (6)The GodScan (scans 4+2) ")
    print("(0) Exit ")
    print("\n")
    
    mode = input("Enter the selected mode/option: ")

    try:
        mode = int(mode)
    except ValueError:
        print("\nYou must enter a number to select an option.")
        print("Quitting...")
        exit()
    except Exception:
        print("\nAn unexpected error has happened.")
        print("Quitting...")
        exit()

    if mode == 0:
        print("Selected mode: " + str(mode) + ", Exit.")    
        print("\nTy For checking out, cya ;P")
        exit()

    elif mode == 1:
        print("Selected mode: " + str(mode) + ", Aggressive Scan.")    
        Aggressive(target)
        
    elif mode == 2:
        print("Selected mode: " + str(mode) + ", Beast Scan.")    
        Beast(target)

    elif mode == 3:
        print("Selected mode: " + str(mode) + ", Silent Scan.")    
        Silent(target)

    elif mode == 4:
        print("Selected mode: " + str(mode) + ", All ports fast way.")    
        print("Not faster than Rustscan tho...")
        FastPorts(target)

    elif mode == 5:
        print("Selected mode: " + str(mode) + ", Your awesome custom scan ;) sheesh.")    
        Custom(target)

    elif mode == 6:
        print("Selected mode: " + str(mode) + ", GodScan, please only use this at ctf's")    
        print("or to make an \"accidental\" DoS.")
        GodScan(target)
    

if __name__ == '__main__':
    # Print Banneh :P
    print(
        "________________________________________________________________\n" +
        "     __                       ____                               \n"+
        "    / |                      /    )   /                      /  \n"+
        "---/__|---------_/_----__----\-------/__----__----__---__---/__-\n"+
        "  /   |  /   /  /    /   )    \     /   ) /___) /___) (_ ` /   )\n"+
        "_/____|_(___(__(_ __(___/_(____/___/___/_(___ _(___ _(__)_/___/_\n" +
        "________________________________________________________________\n"
    )

    #start the program
    try:
        print("𝙿𝚛𝚎𝚜𝚜 𝙲𝚝𝚛𝚕+𝙲 𝚝𝚘 𝚎𝚡𝚒𝚝 𝚊𝚝 𝚊𝚗𝚢 𝚖𝚘𝚖𝚎𝚗𝚝\n")
        main()
    except KeyboardInterrupt:
        print("\n\nCyaa :P")
        exit()