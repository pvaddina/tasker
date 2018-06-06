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


###############################################################################
#
# WorkPackageHandler
#
###############################################################################
class WorkPackageHandler(object):
    def __init__(self):
        self.__workPackages = []
        with open('tasker.json') as json_data:
            self.__taskerConfig = json.load(json_data)

        depth = 1
        for value in self.__taskerConfig.values():
            o = WorkPackage(depth, value)
            self.__workPackages.append(o)
            depth = depth + 1

    
    def Print(self):
        for task in self.__workPackages:
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
            for value in self.__taskerConfig.values():
                print(str(i) + ". " + value["Name"])
                i = i + 1
                
            userChoice, bContinue = utils.GetUserInput(len(self.__workPackages))
            if bContinue:
                self.__workPackages[userChoice-1].Interact()

            print("")
            

###############################################################################
#
# WorkPackage 
#
###############################################################################
class WorkPackage(object):
    def __init__(self, depth, dictWorkPackageConfig):
        self.__Tasks = [] # Where a single task is either a "SingleTask" or "TaskGroup"
        self.__depth = str(depth)
        self.__taskDefs = dictWorkPackageConfig
        
        i = 1
        packageMod = self.__taskDefs["Module"]
        for singleTaskDefKey in self.__taskDefs["Args"].keys():
            taskDepth = self.__depth + "." + str(i) 
            singleTaskDefValue = self.__taskDefs["Args"].get(singleTaskDefKey, 'SHOULD NEVER HAPPEN')
            if "TaskGroup" in singleTaskDefKey:
                self.__Tasks.append(TaskGroup(taskDepth,singleTaskDefValue, packageMod))
            else:
                self.__Tasks.append(SingleTask(taskDepth,singleTaskDefValue, packageMod))
            i = i + 1
            
            
    def GetInteractiveName(self):
        return self.__taskDefs["Name"]
    
    
    def Interact(self):
        bContinue = True
        while bContinue:            
            for i in range(0,len(self.__Tasks)):
                print(self.__Tasks[i].GetInteractiveName())
                
            userChoice, bContinue = utils.GetUserInput(len(self.__Tasks))
            if bContinue:
                self.__Tasks[userChoice-1].Execute()

            print("")
                
         
    def Print(self):
        for task in self.__Tasks:
            task.Print()
    
###############################################################################
#
# TaskGroup
#
###############################################################################

class TaskGroup(object):
    def __init__(self, depth, dictTaskGrpConfig, mod):
        self.__tgTasks = []
        self.__depth = str(depth)
        self.__tgTaskDefs = dictTaskGrpConfig

        if "Module" in self.__tgTaskDefs:
            useModule = self.__tgTaskDefs["Module"]
        else:
            useModule = mod   # Module definition in a TaskGroup is optional, 
                              # in which case, the one defined at the package 
                              # level is used
        i = 1
        for singleTaskDefKey in self.__tgTaskDefs["Args"].keys():
            taskDepth = self.__depth + "." + str(i) 
            singleTaskDefValue = self.__tgTaskDefs["Args"].get(singleTaskDefKey, 'SHOULD NEVER HAPPEN')
            self.__tgTasks.append(SingleTask(taskDepth, singleTaskDefValue, useModule))

            i = i + 1
            
            
    def GetInteractiveName(self):
        p = self.__depth + " " + self.__tgTaskDefs["Name"]
        for i in range(0,len(self.__tgTasks)):
            p = p + "\n       " + self.__tgTasks[i].GetInteractiveName()
        return p
    

    def Execute(self):
        for i in range(0,len(self.__tgTasks)):
            self.__tgTasks[i].Execute()

    
    def Print(self):
        for task in self.__tgTasks:
            task.Print()
    

###############################################################################
#
# SigleTask 
#
###############################################################################

class SingleTask(object):
    def __init__(self, depth, dictTask, mod):
        self.__depth = str(depth)

        modNameStr, cNameStr = mod.split(".")
        modName = importlib.import_module(modNameStr)
        className = getattr(modName, cNameStr)                
        self.__singleTask = className(dictTask)

    def GetInteractiveName(self):
        return self.__depth + "." + self.__singleTask.GetInteractiveName();

    def Execute(self):
        self.__singleTask.Execute();


###############################################################################
#
# __main__
#
###############################################################################
if __name__ == '__main__': 
    t = WorkPackageHandler()
    #t.Print()
    
    t.Interact()    
    print ("Exiting ....")

