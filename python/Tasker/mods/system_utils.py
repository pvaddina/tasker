'''
Created on 10.06.2018
@author: Vaddina Prakash Rao
'''

import interfaces

from subprocess import call
import subprocess

###############################################################################
#
# SysExec 
#
###############################################################################

class SysExec(interfaces.ISingleTask):
    def __init__(self, dictTask):
        self.__cmd = dictTask["Cmd"]
        self.__args = ""
        if "Args" in dictTask:
          self.__args = dictTask["Args"]
        self.__name = dictTask["Name"]

    def GetInteractiveName(self):
        return self.__name

    def Execute(self):
        finalCommand = self.__cmd + " " + self.__args
        cmdList = finalCommand.split(" ")
        cmdList = [idx for idx in cmdList if len(idx)>0]
        print("Running the command: " + finalCommand)
        console_op = subprocess.run(cmdList)
    
