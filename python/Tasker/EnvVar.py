'''
Created on 20.01.2018
@author: Vaddina Prakash Rao
'''

from winreg import *
import win32gui, win32con  
import Interfaces
import utils

###############################################################################
#
# CEnvVar
#
###############################################################################

class CEnvVar(Interfaces.IExecutableTask): 
    def __init__(self, n): 
        try:
            self.regPath = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
            self.reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE) 
            self.key = OpenKey(self.reg, self.regPath, 0, KEY_ALL_ACCESS)    # Handle to the registry item

            self.__ValueName = n
            try: 
                self.__ValueData, self.__TypeId = QueryValueEx(self.key, n)
                self.__Exists = True 
            except: 
                self.__ValueData = "ERROR! The Environment variable with the ValueName \"%s\" does not exist" % (self.__ValueName)
                self.__TypeId = REG_SZ; # By default assign the typeid to a null-terminated string 
                self.__Exists = False          
        except:
            print("Problem opening/accessing the registry. Make sure you start the application with administrator rights")

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
    
#    def Print(self):
#        print("CEnvVar for ValueName=%s, and ValueData=%s" % (self.__ValueName, self.__ValueData))
        
    def GetInteractiveName(self):
        return "Set environment variable as \"" + self.ValueName + "\" ==> \"" + self.ValueData + "\""

    def Execute(self): 
        if self.Exists(): 
            SetValueEx(self.key, self.__ValueName, 0, self.__TypeId, self.__ValueData)
#            print("\"%s\" is currently set to \"%s\"" % (self.__ValueName, self.__ValueData))
#            userChoiceStr = input("Do you want to overwrite it (\'y\' for yes, \'n\' for no) ?")
#            if (userChoiceStr.upper() == "Y"):
#                SetValueEx(self.key, self.__ValueName, 0, self.__TypeId, self.__ValueData)
#            else:
#                print("Nothing changed")
        elif self.__TypeId: 
            print("Value does not exist. Setting %s=%s" % (self.__ValueName, self.__ValueData))
            SetValueEx(self.key, self.__ValueName, 0, self.__TypeId, self.__ValueData) 
        else:
            # Should never be here
            print("ERROR! TypeId is not defined !!")            

        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment') 

    def DummyExecute(self): 
        print("Dummy Command Execution")



###############################################################################
#
# CPathEnvVar
#
###############################################################################

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
    

###############################################################################
#
# EnvVarTask
#
###############################################################################

class EnvVarTask(Interfaces.ISingleTask):
    def __init__(self, dictTask):
        vName = dictTask["ValueName"]
        vData = dictTask["ValueData"]
        if (vName == "Path" or vName == "PATH"):
            self.__subTask = CPathEnvVar()
            self.__subTask.AppendValue(vData)
        else:
            self.__subTask = CEnvVar(vName)
            self.__subTask.ValueData = vData

    def GetInteractiveName(self):
        return self.__subTask.GetInteractiveName()

    def Execute(self):
        self.__subTask.Execute()
    
