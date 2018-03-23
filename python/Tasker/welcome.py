'''
Created on 20.01.2018
@author: Vaddina Prakash Rao
'''

import json 
import EnvVar
import utils 
import Interfaces
import importlib

from pprint import pprint


class Tasker(object):
    def __init__(self):
        self.__taskGroups = []
        with open('tasker.json') as json_data:
            self.__taskerConfig = json.load(json_data)

        depth = 1
        for value in self.__taskerConfig.values():
            o = TaskGroup(depth, value)
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
            

class TaskGroup(Interfaces.ITaskGroup):
    def __init__(self, depth, dictTaskGrpConfig):
        self.__Tasks = []
        self.__depth = str(depth)
        self.__taskDefs = dictTaskGrpConfig
        
        i = 1
        for singleTaskDef in self.__taskDefs["Args"].keys():
            taskDepth = self.__depth + "." + str(i) 
            val = self.__taskDefs["Args"].get(singleTaskDef, 'SHOULD NEVER HAPPEN')
            if "TaskGroup" in singleTaskDef:
                self.__Tasks.append(TaskGroup(taskDepth,val))
            else:
                modNameStr, cNameStr = (self.__taskDefs["Module"]).split(".")
                modName = importlib.import_module(modNameStr)
                className = getattr(modName, cNameStr)                
                self.__Tasks.append(className(taskDepth, val))
            i = i + 1
            
            
    def GetInteractiveName(self):
        return self.__taskDefs["Name"]
    
    
    def Interact(self):
        bContinue = True
        while bContinue:            
            print("")
            for i in range(0,len(self.__taskDefs)):
                print(str(self.__depth) + "." + str(i+1) + ". " + self.__Tasks[i].GetInteractiveName())
                
            userChoice, bContinue = utils.GetUserInput(len(self.__Tasks))
            if bContinue:
                self.__Tasks[userChoice-1].Execute()
                
         
    def Execute(self):
        self.Interact()

    
    def Print(self):
        for task in self.__Tasks:
            task.Print()
    

if __name__ == '__main__': 
    t = Tasker()
    #t.Print()
    
    t.Interact()    
    print ("Exiting ....")

