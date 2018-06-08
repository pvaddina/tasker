'''
Created on 30.01.2018

@author: Vaddina Prakash Rao
'''

from colorama import init, Fore, Back, Style
init(autoreset=True) # The init function for Colorama


def GetUserInput(numMaxEntries):
    while(True):
        print(Style.BRIGHT + Fore.GREEN + "Please enter your choice or '-' to go up one level: ", end='')
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


