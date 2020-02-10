'''
Created on 30.01.2018
@author: Vaddina Prakash Rao
'''

import platform as pf
detectPlatform = pf.system()

if detectPlatform == "Linux":
    class PrintStyle: 
        # For all the following color codes, replace the ';1m' with 'm' to get corresponding non-Bold color codes
        RED     = '\u001b[31;1m'
        GREEN   = '\u001b[32;1m'
        MAGENTA = '\u001b[35;1m'
        WHITE   = '\033[37;1m'
        YELLOW  = '\u001b[33;1m'
        BLUE    = '\u001b[34;1m'
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
        YELLOW  = Style.BRIGHT + Fore.YELLOW
        BLUE    = Style.BRIGHT + Fore.BLUE

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

def CustomPrint(style, s):
    lclPrint(style + s)

def GetUserInput(acceptedVaues):
    while(True):
        lclPrintEnd(PrintStyle.GREEN + "Please enter your choice {}: ".format(acceptedVaues))
        usrChoice = input()
        if usrChoice != "-":
            if usrChoice in acceptedVaues:
                print("") # Add a new line
                return usrChoice, True
        else:
            break
            
    return 0, False


def GetNewOption():
    lclPrintEnd(PrintStyle.GREEN + "Enter a new value:")
    userValue = input()
    return userValue


