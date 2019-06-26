'''
Created on 20.01.2018
@author: Vaddina Prakash Rao
'''

import platform as pf

detectPlatform = pf.system()

if detectPlatform == "Linux":
    pass
elif detectPlatrform == "Windows":
    from winreg import *
    import win32gui, win32con  
    import interfaces
    import utils

    ###############################################################################
    #
    # CEnvVar
    #
    ###############################################################################

    class CEnvVar(object): 
        def __init__(self, n, userVarTyp): 
            if userVarTyp:
                self.regPath = r'Environment'
                rootRegistry = HKEY_CURRENT_USER
                self.envVarType = "User type"
            else:
                self.regPath = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
                rootRegistry = HKEY_LOCAL_MACHINE
                self.envVarType = "System type"

            try:
                self.reg = ConnectRegistry(None, rootRegistry) 
                self.key = OpenKey(self.reg, self.regPath, 0, KEY_ALL_ACCESS)    # Handle to the registry item
                self.__ValueName = n
                if len(n) != 0:
                    self.TryRead()
            except:
                utils.ErrorPrint("Problem opening/accessing the registry. Make sure you start the application with administrator rights")

        def TryRead(self): 
            try: 
                self.__existingValueData, self.__TypeId = QueryValueEx(self.key, self.__ValueName)
                self.__Exists = True 
            except: 
                self.__TypeId = REG_SZ # By default assign the typeid to a null-terminated string 
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
            self.__TypeId = REG_MULTI_SZ

        def Exists(self): 
            return self.__Exists    
        
        def GetInteractiveName(self):
            s = "Set environment variable(" + self.envVarType + ") as \"" + self.ValueName + "\" ==> \"" + self.ValueData + "\""
            if len(self.ValueName) == 0 or len(self.ValueData) == 0:
                s = "Interactively set environment variable (" + self.envVarType + ") ValueName:ValueData pair to the system environment variables"
            return s

        def Execute(self): 
            utils.HighPrint(self.GetInteractiveName())
            if len(self.__ValueName) == 0:
                self.__ValueName = input("Key=")
                self.__ValueData = input("Value=")
                if len(self.__ValueName) == 0 or len(self.__ValueData) == 0:
                    utils.ErrorPrint("ERROR !! Invalid entries")
                    return
                else:
                    self.TryRead()
            else:
                pass

            if self.Exists(): 
                utils.HighPrint("Value (" + self.envVarType + ") already exists and is set as: %s=%s" % (self.__ValueName, self.__existingValueData))
                utils.HighPrint("Nevertheless, updating it to: %s=%s" % (self.__ValueName, self.__ValueData))
                SetValueEx(self.key, self.__ValueName, 0, self.__TypeId, self.__ValueData)
            elif self.__TypeId: 
                utils.HighPrint("Value (" + self.envVarType + ") does not exist. Setting %s=%s" % (self.__ValueName, self.__ValueData))
                SetValueEx(self.key, self.__ValueName, 0, self.__TypeId, self.__ValueData) 
            else:
                # Should never be here
                utils.ErrorPrint("ERROR! TypeId is not defined !!")            

            win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment') 

        def DummyExecute(self): 
            utils.OkPrint("Dummy Command Execution")



    ###############################################################################
    #
    # CPathEnvVar
    #
    ###############################################################################

    class CPathEnvVar(CEnvVar):
        def __init__(self, userEnvVar):
            super().__init__("PATH", userEnvVar)
            self.__valueToAppend = ""
               
        def CheckAndAppendData(self, s): 
            if s not in self.ValueData:
                seq = ((self.ValueData), s)
                self.ValueData = ';'.join(seq)
                SetValueEx(self.key, self.ValueName, 0, self.TypeId, self.ValueData)
                win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment') 
            else:
                utils.ErrorPrint("The specified string is already part of \'PATH\'. Did nothing.")

        def Execute(self):
            utils.HighPrint(self.GetInteractiveName())
            if len(self.__valueToAppend) == 0:
                self.__valueToAppend = input("Enter the Value to append to PATH:")
                if len(self.__valueToAppend) == 0:
                    utils.ErrorPrint("ERROR !! Invalid entries")
                    return
            else:
                pass

            self.CheckAndAppendData(self.__valueToAppend) 

        def ValueExists(self, s):
            return s in self.ValueData
        
        def AppendValue(self, s):
            self.__valueToAppend = str(s) 

        def GetInteractiveName(self):
            s = "Add \"" + self.__valueToAppend + "\" in PATH environment variable(" + self.envVarType + ")"
            if len(self.__valueToAppend) == 0:
                s = "Append a value to the PATH environment variable"
            return s;

        def Exists(self):
            return True
        

    ###############################################################################
    #
    # EnvVarTask
    #
    ###############################################################################

    class EnvVarTask(interfaces.ISingleTask):
        def __init__(self, dictTask):
            vName = dictTask["ValueName"]
            vData = dictTask["ValueData"]
            userEnvVariable = False
            if "UserEnvVar" in dictTask and bool(int(dictTask["UserEnvVar"])):
                userEnvVariable = True

            if (vName == "Path" or vName == "PATH"):
                self.__subTask = CPathEnvVar(userEnvVariable)
                self.__subTask.AppendValue(vData)
            else:
                self.__subTask = CEnvVar(vName, userEnvVariable)
                self.__subTask.ValueData = vData

        def GetInteractiveName(self):
            return self.__subTask.GetInteractiveName()

        def Execute(self):
            self.__subTask.Execute()
else:
    pass
