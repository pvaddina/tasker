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
        self.__args = dictTask["Args"]
        self.__name = dictTask["Name"]

    def GetInteractiveName(self):
        return self.__name

    def Execute(self):
        finalCommand = self.__cmd + " " + self.__args
        print("Running the command: " + finalCommand)
        console_op = subprocess.run(finalCommand, stdout=subprocess.PIPE)
    
