'''
Created on 30.01.2018
@author: Vaddina Prakash Rao
'''

import platform as pf
detectPlatform = pf.system()

if detectPlatform == "Linux":
    class PrintStyle:
        RED     = '\u001b[31m'
        GREEN   = '\u001b[99m'
        MAGENTA = '\u001b[35m'
        WHITE   = '\033[37m'
        RESET   = '\033[0m'

    def lclPrint(s):
        print(s+PrintStyle.RESET)

    def lclPrintEnd(s):
        print(s+PrintStyle.RESET, end='')

elif detectPlatform == "Windows":
    from colorama import init, Fore, Back, Style
    init(autoreset=True) # The init function for Colorama

    class PrintStyle:
        WHITE   = Style.BRIGHT + Fore.WHITE
        MAGENTA = Style.BRIGHT + Fore.MAGENTA
        GREEN   = Style.BRIGHT + Fore.GREEN
        RED     = Style.BRIGHT + Fore.RED

    def lclPrint(s):
        print(s)

    def lclPrintEnd(s):
        print(s, end='')


def NormalPrint(s):
    lclPrint(PrintStyle.WHITE + s)

def HighPrint(s):
    lclPrint(PrintStyle.MAGENTA + s)

def OkPrint(s):
    lclPrint(PrintStyle.GREEN + s)

def ErrorPrint(s):
    lclPrint(PrintStyle.RED + s)

def GetUserInput(numMaxEntries):
    while(True):
        lclPrintEnd(PrintStyle.GREEN + "Please enter your choice or '-' to go up one level: ")
        userChoiceStr = input()
        if userChoiceStr != "-":
            try:
                userChoice = int(userChoiceStr)
                conversion = True;
            except:
                conversion = False
                
            if not conversion or (userChoice > numMaxEntries):
                pass
            else:
                print("") # Add a new line
                return userChoice, True
        else:
            break
            
    return 0, False
