'''
Created on 20.01.2018
@author: Vaddina Prakash Rao
'''

import json 
import utils 
import importlib
import sys
import os.path

import pprint

RT_OPTIONS_FILE = ".opt.json"
DEFAULT_CONFIG_FILE = "config.json"

###############################################################################
#
# WorkPackageHandler
#
###############################################################################
class WorkPackageHandler(object):
    def __init__(self, configFile, rtOptions):
        self.__workPackages = []
        with open(configFile) as json_data:
            self.__taskerConfig = json.load(json_data)
        self.__rtOptHandler = rtOptions
        self.CreateWPS()


    def CreateWPS(self):
        depth = 1
        refPackages = {}
        try:
            refPackages = self.__taskerConfig.pop('GenericWorkPackages')
        except:
            pass

        for value in self.__taskerConfig.values():
            o = WorkPackage(depth, value, refPackages, self.__rtOptHandler)
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
            
    def DirectExecute(self, liExecOpts):
        idx = int(liExecOpts[0]) - 1
        if idx < len(self.__workPackages):
            del liExecOpts[0]
            if len(liExecOpts) > 0:
                self.__workPackages[idx].DirectExecute(liExecOpts)
            else:
                self.__workPackages[idx].Interact()
        else:
            utils.ErrorPrint("Error!! Incorrect option. Nothing done.")

            
    def Interact(self):
        bContinue = True
        while bContinue:
            i = 1
            for value in self.__workPackages:
                utils.NormalPrint(str(i) + ". " + self.__workPackages[i-1].GetInteractiveName())
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
    def __init__(self, depth, dictWorkPackageConfig, genericWPs, rtOptHandler):
        self.__rtOptHandler = rtOptHandler
        self.__Tasks = [] # Where a single task is either a "SingleTask" or "TaskGroup"
        self.__depth = str(depth)

        if "@GenericWorkPackages:" in dictWorkPackageConfig:
            refWP = dictWorkPackageConfig.replace('@GenericWorkPackages: ','').strip()
            dictWorkPackageConfig = genericWPs[refWP]
        
        # Assign the values of the variables to the strings of the key "Consts"
        if "Consts" in dictWorkPackageConfig:
          v = {}
          # Check if 'Vars' key is present
          if "Vars" in dictWorkPackageConfig:
            v = dictWorkPackageConfig['Vars']

          # Now iterate through all the values of 'Consts' and replace the variables with their corresponding values
          # as defined in the 'Vars' value dictionary
          for k in dictWorkPackageConfig["Consts"].keys():
            dictWorkPackageConfig['Consts'][k] = dictWorkPackageConfig['Consts'][k].format(**v)
          
        # Finally assign the modified dictionary locally
        self.__taskDefs = dictWorkPackageConfig
        
        i = 1
        packageMod = self.__taskDefs["Module"]
        for singleTaskDefKey in self.__taskDefs["Args"].keys():
            taskDepth = self.__depth + "." + str(i) 
            singleTaskDefValue = self.__taskDefs["Args"].get(singleTaskDefKey, 'SHOULD NEVER HAPPEN')
            constsDict = {}
            if  "Consts" in self.__taskDefs:
                constsDict = self.__taskDefs["Consts"]

            if "TaskContainer" in singleTaskDefKey:
                self.__Tasks.append(TaskContainer(taskDepth,constsDict,singleTaskDefValue, packageMod))
            elif "TaskGroup" in singleTaskDefKey:
                self.__Tasks.append(TaskGroup(taskDepth,constsDict,singleTaskDefValue, packageMod))
            else:
                self.__Tasks.append(SingleTask(taskDepth,constsDict,singleTaskDefValue, packageMod))
            i = i + 1

            
    def GetInteractiveName(self):
        return self.__taskDefs["Name"]
    
    
    def DirectExecute(self, liExecOpts):
        idx = int(liExecOpts[0]) - 1
        if idx < len(self.__Tasks):
            del liExecOpts[0]
            if len(liExecOpts) > 0:
                self.__Tasks[idx].DirectExecute(liExecOpts)
            else:
                self.__Tasks[idx].Execute()
        else:
            utils.ErrorPrint("Error!! Incorrect option. Nothing done.")

            
    def Interact(self):
        bContinue = True
        while bContinue:            
            for i in range(0,len(self.__Tasks)):
                utils.NormalPrint(self.__Tasks[i].GetInteractiveName())
                
            userChoice, bContinue = utils.GetUserInput(len(self.__Tasks))
            if bContinue:
                self.__Tasks[userChoice-1].Execute()

            print("")
                
         
    def Print(self):
        for task in self.__Tasks:
            task.Print()
    
###############################################################################
#
# TaskContainer
#
###############################################################################

class TaskContainer(object):
    def __init__(self, depth, constsDict, dictTaskContainer, mod):
        self.__tcTasks = []
        self.__depth = str(depth)
        self.__tcTaskDefs = dictTaskContainer

        if "Module" in self.__tcTaskDefs:
            containerMod = self.__tcTaskDefs["Module"]
        else:
            containerMod = mod   # Module definition in a TaskContainer is optional, 
                              # in which case, the one defined at the package 
                              # level is used
        i = 1
        for singleTaskDefKey in self.__tcTaskDefs["Args"].keys():
            taskDepth = self.__depth + "." + str(i) 
            singleTaskDefValue = self.__tcTaskDefs["Args"].get(singleTaskDefKey, 'SHOULD NEVER HAPPEN')
            if "TaskContainer" in singleTaskDefKey:
                self.__tcTasks.append(TaskContainer(taskDepth, constsDict, singleTaskDefValue, containerMod))
            elif "TaskGroup" in singleTaskDefKey:
                self.__tcTasks.append(TaskGroup(taskDepth, constsDict, singleTaskDefValue, containerMod))
            else:
                self.__tcTasks.append(SingleTask(taskDepth, constsDict, singleTaskDefValue, containerMod))
            i = i + 1
            
            
    def DirectExecute(self, liExecOpts):
        idx = int(liExecOpts[0]) - 1
        if idx < len(self.__tcTasks):
            del liExecOpts[0]
            if len(liExecOpts) > 0:
                self.__tcTasks[idx].DirectExecute(liExecOpts)
            else:
                self.__tcTasks[idx].Execute()
        else:
            utils.ErrorPrint("Error!! Incorrect option. Nothing done.")

            
    def GetInteractiveName(self):
        p = self.__depth + ". [CONTAINER] " + self.__tcTaskDefs["Name"]
#        for i in range(0,len(self.__tcTasks)):
#            p = p + "\n       " + self.__tcTasks[i].GetInteractiveName()
        return p
    

    def Execute(self):
#        for i in range(0,len(self.__tcTasks)):
#            self.__tcTasks[i].Execute()
        bContinue = True
        while bContinue:            
            for i in range(0,len(self.__tcTasks)):
                utils.NormalPrint(self.__tcTasks[i].GetInteractiveName())
                
            userChoice, bContinue = utils.GetUserInput(len(self.__tcTasks))
            if bContinue:
                self.__tcTasks[userChoice-1].Execute()

            print("")
                

    
    def Print(self):
        for tc in self.__tcTasks:
            tc.Print()
    

###############################################################################
#
# TaskGroup
#
###############################################################################

class TaskGroup(object):
    def __init__(self, depth, constsDict, dictTaskGrpConfig, mod):
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
            self.__tgTasks.append(SingleTask(taskDepth, constsDict, singleTaskDefValue, useModule))

            i = i + 1
            
            
    def DirectExecute(self, liExecOpts):
        if len(liExecOpts) > 0:
            utils.ErrorPrint("Error!! Incorrect option. Nothing done.")
        else:
            self.Execute()

    def GetInteractiveName(self):
        p = self.__depth + ". [GROUP] " + self.__tgTaskDefs["Name"]
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
    def __init__(self, depth, constsDict, dictTask, mod):
        self.__depth = str(depth)

        # NOTE: 
        # The dictTask will be modified here
        dictTask["Consts"] = constsDict

        modParts = mod.split(".")
        modNameStr = modParts[0] + "." + modParts[1]
        cNameStr = modParts[len(modParts)-1]
        #print("modNameStr=" + modNameStr + ", cNameStr=" + cNameStr)
        #modNameStr, cNameStr = mod.split(".")
        modName = importlib.import_module(modNameStr)
        className = getattr(modName, cNameStr)                
        self.__singleTask = className(dictTask)


    def DirectExecute(self, liExecOpts):
        if len(liExecOpts) > 0:
            utils.ErrorPrint("Incorrect option. Nothing done.")
        else:
            self.__singleTask.Execute();


    def GetInteractiveName(self):
        return self.__depth + ". " + self.__singleTask.GetInteractiveName();

    def Execute(self):
        self.__singleTask.Execute();


###############################################################################
#
# RtoptHandler
#
###############################################################################

class RtoptHandler(object):
    def __init__(self):
        self.opt = {}
        self.pp = pprint.PrettyPrinter(indent=4)
        try:
          with open(RT_OPTIONS_FILE, 'r') as f:
              self.rtopt = json.load(f)
        except:
          pass # Do nothing

    def Printout(key):
        if key:
            self.pp.pprint(self.opt['key'])
        else:
            self.pp.pprint(self.opt)

    def DumpToFile():
        with open(RT_OPTIONS_FILE, 'w+') as f:
            json.dump(self.rtopt, f, indent=4, sort_keys=True)

    def Getoptions(key):
        if self.opt and key in self.opt:
            return self.opt[key]
        return None

    def Addoptions(key, values):
        self.opt[key] = values
        


###############################################################################
#
# __main__
#
###############################################################################
def ReadIp():
    result = None
    options = {}
    h = False
    if len(sys.argv) > 1:
        if "--help" in sys.argv or "--Help" in sys.argv or "--HELP" in sys.argv:
            utils.OkPrint("Usage:")
            utils.OkPrint("      tasker.py [--configfile=<config-file-name>] [--exec=<option>] [--wait=<True/False>]")
            h = True
        else:
            for i in range(1,len(sys.argv)):
                opts = sys.argv[i].split("=")
                if len(opts) == 2:
                    #print(opts[0]+ "--" + opts[1])
                    options[opts[0][2:]] = opts[1]

    if not h:
        if "configfile" in options:
            cf = options["configfile"]
        else:
            cf = DEFAULT_CONFIG_FILE
            options["configfile"] = cf
            utils.HighPrint("Using the default configuration file \"" + cf + "\"\n")

        if (os.path.isfile(cf) == True):
            result = True
        else:
            utils.ErrorPrint("The configuration file " + cf + " is not found. I cannot continue.")

    return result, options





if __name__ == '__main__': 
    cont, options = ReadIp()
    rtoptions = RtoptHandler()

    if cont == True:
        t = WorkPackageHandler(options["configfile"], rtoptions)
        if "exec" in options:
            execOpts = options["exec"]
            liExecOpts = execOpts.split(".")
            t.DirectExecute(liExecOpts)
            bWait = True
        else:
            t.Interact()
    elif cont == False:
        utils.OkPrint("Exiting ....")

    if "wait" in options and bool(int(options["wait"])) == True:
        input("")
