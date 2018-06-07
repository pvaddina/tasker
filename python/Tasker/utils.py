'''
Created on 30.01.2018

@author: Vaddina Prakash Rao
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
                pass
            else:
                print("") # Add a new line
                return userChoice, True
        else:
            break
            
    return 0, False

        
                
        
