'''
Created on 30.01.2018

@author: praka
'''
def GetUserInput(numMaxEntries):
    while(True):
        userChoiceStr = input("Please enter your choice or '-' to go up one level: ")
        if userChoiceStr != "-":
            try:
                userChoice = int(userChoiceStr)
                conversion = True;
            except:
                conversion = False
                
            if not conversion or (userChoice > numMaxEntries):
                print("You entered an invalid value. Please re-try.")
            else:
                return userChoice, True
        else:
            break
            
    return 0, False
