'''
Created on 20.01.2018
@author: Vaddina Prakash Rao
'''

import json 
import sys 
import EnvVar
import utils 

from pprint import pprint


class Tasker(object):
    def __init__(self):
        self.__taskGroups = []
        with open('tasker.json') as json_data:
            self.__taskerConfig = json.load(json_data)

        depth = 1
        for value in self.__taskerConfig.values():
            o = EnvVar.EnvVarTaskGroup(depth, value["Args"])
            self.__taskGroups.append(o)
            depth = depth + 1    

    
    def Print(self):
        for task in self.__taskGroups:
            task.Print()
    
    
    def RawConfigFilePrint(self):
        with open('tasker.json') as json_data:
            taskerVals = json.load(json_data)
        
        numEntries = len(taskerVals)
        
        for i in range(numEntries):
            print("Printing %d" % (i+1))
            pprint(taskerVals[str(i+1)])
            
            
    def Interact(self):
        bContinue = True
        while bContinue:
            i = 1
            print("")
            for value in self.__taskerConfig.values():
                print(str(i) + ". " + value["Name"])
                i = i + 1
                
            userChoice, bContinue = utils.GetUserInput(len(self.__taskGroups))
            if bContinue:
                self.__taskGroups[userChoice-1].Interact()
            

if __name__ == '__main__': 
    t = Tasker()
    #t.Print()
    
    t.Interact()
    
    print ("Exiting ....")

