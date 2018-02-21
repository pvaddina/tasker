'''
Created on 30.01.2018

@author: praka
'''
def GetUserInput(numEntries):
    while(True):
        userChoiceStr = input("Enter your choice: ")
        if userChoiceStr != "-":
            userChoice = int(userChoiceStr)
            if userChoice > numEntries:
                print("You entered an invalid value")
                
