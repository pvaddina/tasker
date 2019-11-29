'''
Created on 10.06.2018
@author: Vaddina Prakash Rao
'''

import interfaces

from subprocess import call
import subprocess
import sys
import os
import utils

import platform as pf

detectPlatform = pf.system()
seperator = " ; "

if detectPlatform == "Windows":
  seperator = " & "

###############################################################################
#
# SysExec 
#
###############################################################################

class SysExec(interfaces.ISingleTask):
    def __init__(self, dictTask):
        self.__cmds = dictTask["AllCmds"]
        # Check if a 'Consts' dictionary is available
        consts = {}
        if 'Consts' in dictTask:
            consts = dictTask['Consts']
        # Iterate through all the commands and try to replace the values using the consts dictionary
        # Note: If any of the mapping value is not present, the execution will stop here
        ignoreAllCmds = False
        for idx in range(len(self.__cmds)):
            try:
                self.__cmds[idx] = self.__cmds[idx].format(**consts)
            except:
                utils.ErrorPrint("Error while parsing the config file. Irregular commands description for {}.".format(dictTask["Name"]))
                ignoreAllCmds = True
        if ignoreAllCmds:
            self.__cmds.clear()

        self.__name = dictTask["Name"]

    def GetInteractiveName(self):
        return self.__name

    def Execute(self):
        execCmd = ""
        for cmd in self.__cmds:
          execCmd += cmd
          execCmd += seperator
        execCmd = execCmd.rsplit(seperator, 1)[0]
        
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
