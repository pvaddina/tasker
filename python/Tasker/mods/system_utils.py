'''
Created on 10.06.2018
@author: Vaddina Prakash Rao
'''

import interfaces

from subprocess import call
import subprocess
import sys
import os

###############################################################################
#
# SysExec 
#
###############################################################################

class SysExec(interfaces.ISingleTask):
    def __init__(self, dictTask):
        self.__cmds = dictTask["AllCmds"]
        self.__name = dictTask["Name"]

    def GetInteractiveName(self):
        return self.__name

    def Execute(self):
        execCmd = ""
        for cmd in self.__cmds:
          execCmd += cmd
          execCmd += "; "
        print("Running the command: " + execCmd )

        ret = subprocess.call(execCmd, shell=True)
'''
        ####################################################################
        # Works but not recommended
        ####################################################################
        ret = os.system(execCmd)
'''

'''
        ####################################################################
        # Returns output only after the process has completed !!!
        ####################################################################
        process = subprocess.Popen(execCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
        stdout, stderr = process.communicate()
        return stdout.strip()
'''
'''
        ####################################################################
        # Blocks (nearly 100% of the time) when no output to read
        ####################################################################
        process = subprocess.Popen(execCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
        while True:
          line = process.stdout.readline()
          if not line: break
          else:
            print(line)
'''
'''
        ####################################################################
        # Blocks (nearly 100% of the time) when no output to read
        ####################################################################
        process = subprocess.Popen(execCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
        cmdList = execCmd.split(" ")
        cmdList = [idx for idx in cmdList if len(idx)>0]
        print(cmdList)
        console_op = subprocess.run(cmdList)
'''
