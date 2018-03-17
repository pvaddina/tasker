'''
Created on 20.01.2018
@author: Vaddina Prakash Rao
'''

from winreg import *
import win32gui, win32con  
import Interfaces
import utils
#from pip._vendor.html5lib.treewalkers import pprint

class CEnvVar(Interfaces.IExecutableTask): 
    regPath = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
    reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE) 
    key = OpenKey(reg, regPath, 0, KEY_ALL_ACCESS)    # Handle to the registry item

    def __init__(self, n): 
        self.__ValueName = n
        try: 
            self.__ValueData, self.__TypeId = QueryValueEx(self.key, n)
            self.__Exists = True 
        except: 
            self.__ValueData = "ERROR! The Environment variable with the ValueName \"%s\" does not exist" % (self.__ValueName)
            self.__TypeId = REG_SZ; # By default assign the typeid to a null-terminated string 
            self.__Exists = False          

    def __del__(self): 
        CloseKey(self.key)
        CloseKey(self.reg)

    @property 
    def ValueName(self): 
        return self.__ValueName     

    @ValueName.setter 
    def ValueName(self, n): 
        self.__ValueName = n          

    @property 
    def ValueData(self):
        return self.__ValueData     

    @property 
    def TypeId(self):
        return self.__TypeId

    @ValueData.setter 
    def ValueData(self, v): 
        self.__ValueData = str(v)        

    def SetTypeIdToRegMultiSz(self):
        self.__TypeId = REG_MULTI_SZ;

    def Exists(self): 
        return self.__Exists;    
    
    def Print(self):
        print("CEnvVar for ValueName=%s, and ValueData=%s" % (self.__ValueName, self.__ValueData))
        
    def GetInteractiveName(self):
        return "Set \"" + self.ValueName + "\" to the value \"" + self.ValueData + "\""

    def Execute(self): 
        if self.Exists(): 
            print("\"%s\" is currently set to \"%s\"" % (self.__ValueName, self.__ValueData))
            userChoiceStr = input("Do you want to overwrite it (\'y\' for yes, \'n\' for no) ?")
            if (userChoiceStr.upper() == "Y"):
                SetValueEx(self.key, self.__ValueName, 0, self.__TypeId, self.__ValueData)
            else:
                print("Nothing changed")
        elif self.__TypeId: 
            print("Value does not exist. Setting %s=%s" % (self.__ValueName, self.__ValueData))
            SetValueEx(self.key, self.__ValueName, 0, self.__TypeId, self.__ValueData) 
        else:
            # Should never be here
            print("ERROR! TypeId is not defined !!")            

        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment') 

    def DummyExecute(self): 
        print("Dummy Command Execution")


class CPathEnvVar(CEnvVar):
    def __init__(self):
        super().__init__("PATH")
        self.__valueToAppend = "";
           
    def CheckAndAppendData(self, s): 
        if s not in self.ValueData:
            seq = ((self.ValueData), s)
            self.ValueData = ';'.join(seq)
            SetValueEx(self.key, self.ValueName, 0, self.TypeId, self.ValueData)
            win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment') 
        else:
            print("The specified string is already part of \'PATH\'. Did nothing.")

    def Execute(self):
        self.CheckAndAppendData(self.__valueToAppend) 

    def ValueExists(self, s):
        return s in self.ValueData
    
    def AppendValue(self, s):
        self.__valueToAppend = str(s) 

    def GetInteractiveName(self):
        return "Add \"" + self.__valueToAppend + "\" in PATH environment variable"

    def Exists(self):
        return True
    

class EnvVarTask(Interfaces.ISingleTask):
    def __init__(self, depth, dictTaskConfig):
        #pprint(dictTaskConfig)
        self.__taskConfig = dictTaskConfig
        self.__depth = str(depth)
        self.__subTasks = []
        self.IterateAndCreateTasks(dictTaskConfig)
              
    def IterateAndCreateTasks(self, dictTask):
        for key in dictTask.keys():
            keyval = dictTask[key]
            # print("Key=%s and KeyVal=%s" % (key, keyval))
            if key == "ValueName":
                valuename = keyval
                valuedata = dictTask["ValueData"]
                self.CreateSingleTask(valuename, valuedata)
            elif type(keyval) is dict:
                self.IterateAndCreateTasks(keyval)
        
    def CreateSingleTask(self, valuename, valuedata):
        #print("ValueName=%s, ValueData=%s" % (valuename, valuedata))
        if (valuename == "Path" or valuename == "PATH"):
            p = CPathEnvVar()
            p.AppendValue(valuedata)
            self.__subTasks.append(p);
        else:
            p = CEnvVar(valuename)
            p.ValueData = valuedata
            self.__subTasks.append(p)    
    
    def Interact(self):
        while(True):
            i = 1
            for key in self.__taskConfig.keys():
                print(self.__depth + "." + str(i) + ": " + key)
                i = i + 1
        
            if utils.GetUserInput(self.__Tasks) == "-":
                break


    def GetInteractiveName(self):
        ret = "Group of tasks executed in the following order:"
        if ( len(self.__subTasks) > 1 ):
            for task in self.__subTasks:
                ret = ret + "\n        " + task.GetInteractiveName()
        else:
            ret = self.__subTasks[0].GetInteractiveName()
        return ret

    def Print(self):
        for subTask in self.__subTasks:
            subTask.Print()
            
    def Execute(self):
        for subTask in self.__subTasks:
            subTask.DummyExecute()
