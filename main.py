#!/usr/bin/python3

import os


def saveScans():
    print("Would you like to save the scan?")
    print("(The scan will be saved to your current directory)")
    opt = input("(1)Yes (0) No: ")


    if opt == "1":
        add = (" -oN " + os.getcwd() + "AutoSheeshScan.txt") 
        return(add)
    elif opt == "0":
        return('')
    else:
        print("That option does not exist, proceding with save.")



def uidCheck():
    #check that the user has root capabilities
    uid = os.getuid()
    
    if uid == 0:
        pass
    else:
        print("\nThis program must be executed as root or with sudo.")
        print("Quiting...")
        exit()
    
    print("UID: " + str(uid) + ". all good")


def Aggressive(target):
    save = saveScans()
    command = "nmap -A --min-rate 5000 -v -n -Pn " + target + save


def Beast(target):
    save = saveScans()
    command = "nmap -sT -sC -O -sV --min-rate 5000 -v -R -Pn " + target + save
    os.system(command)


def Silent(target):
    save = saveScans()
    command = "nmap -sS -v" + target + " -n -Pn" + save
    os.system(command)


def FastPorts(target):
    save = saveScans()
    command = "nmap -sS -p- --open -v --min-rate 5000 " + target + " -n -Pn" + save
    os.system(command)


def Custom(target):
    input("Enter your own nmap commands \n:")

    print("Why do u use this option, just write your own nmap in the terminal.\n pfff")
    exit()


def CrazyScan(target):
    save = saveScans()
    commandA = "nmap -sT -sC -sV -O --script vuln --min-rate 5000 -Pn -n " + target + save
    commandB = "nmap -sU -sC -sV -O --script vuln --min-rate 5000 -Pn -n " + target + save

    print("This scan will execute the following:")
    print(commandA)
    print(commandB)

    crazy = input("\nAre you sure that you want to execute this command?\n(1)Yes (2)No: ")
    
    try:
        int(crazy)
    except TypeError:
        print("You must enter \"1\" for yes, or \"2\" for No.")
        CrazyScan()
    except ValueError:
        print("You must enter \"1\" for yes, or \"2\" for No.")
        CrazyScan(target)

    if int(crazy) == 1:
        print("\nO_o!, you are crazy!!! aaaaagghh *runs away* \n")
        os.system(commandA)
        os.system(commandB)

    elif int(crazy) == 2:
        print("I though that you were Crazy!! Fiuf, cya :P")
    else:
        print("That option does not exist, \nplease enter \"1\" for Yes or \"2\" for no")
        CrazyScan(target)


def main():
    uidCheck()

    target = input("Write the target to scan:")    
    print("The target is: " + target)
    
    print("\n")
    print("\n")
    print("Scan Modes:\n(1)Agressive\n(2)Beast\n(3)Silent\n")
    print("(4)Fazt all open ports\n(5)Custom Automation\n(6)The CrazyScan (scans 4+2)\n")
    print("(0) Exit ")
    print("\n")
    
    mode = input("Enter the selected mode/option: ")


    try:
        mode = int(mode)
    except ValueError:
        print("You entered: " + str(mode))
        print("\nYou must enter a number to select an option.")
        print("Quitting...")
        exit()
    except Exception:
        print("\nAn unexpected error has happened.")
        print("Quitting...")
        exit()

    if mode == 0:
        print("\nSelected option: " + str(mode) + ", Exit.")    
        print("\nTy For checking out, cya ;P")
        exit()

    elif mode == 1:
        print("\nSelected mode: " + str(mode) + ", Aggressive Scan.\n")    
        Aggressive(target)
        
    elif mode == 2:
        print("\nSelected mode: " + str(mode) + ", Beast Scan.\n")    
        Beast(target)

    elif mode == 3:
        print("\nSelected mode: " + str(mode) + ", Silent Scan.\n")    
        Silent(target)

    elif mode == 4:
        print("\nSelected mode: " + str(mode) + ", All open ports fast way.\n")    
        print("Not faster than Rustscan tho...")
        FastPorts(target)

    elif mode == 5:
        print("\nSelected mode: " + str(mode) + ", Your awesome custom scan ;) sheesh.\n")    
        Custom(target)

    elif mode == 6:
        print("\nSelected mode: " + str(mode) + ", CrazyScan, please only use this at ctf's")    
        print("or to make an \"accidental\" DoS. \n")
        CrazyScan(target)
    else:
        print("\n#!! That is Not a valid option, you must enter a number !!# \n")
        main()

    
    

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