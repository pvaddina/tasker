'''
Created on 10.06.2018
@author: Vaddina Prakash Rao
'''

import interfaces
import subprocess
import sys
import os
import utils

import platform as pf

detectPlatform = pf.system()
seperator = " ; "
launchCmd = "konsole -e \"bash -c \\\"{CMD1}; exec bash\\\"\""

if detectPlatform == "Windows":
  seperator = " & "
  launchCmd = "start cmd /k \"{CMD1}\""

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
        global launchCmd
        execCmd = ""
        for cmd in self.__cmds:
          execCmd += cmd
          execCmd += seperator

        execCmd = execCmd.rsplit(seperator, 1)[0]
        subprocess.call(execCmd, shell=True)

        #finalCmd = launchCmd.replace('{CMD1}', execCmd, 1)
        #subprocess.Popen(finalCmd, shell=True)
