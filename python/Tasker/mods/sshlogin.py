'''
Created on 10.06.2018
@author: Vaddina Prakash Rao
'''

import interfaces

import os
import colorama
from colorama import Fore, Style

###############################################################################
#
# SshLogin
#
###############################################################################

COMMAND = "sshpass -p iluvr0hde ssh -o \"StrictHostKeyChecking no\" "
DISPLAY_DEV_STR = "{:>6} {:>17} {:>25} {:>13}"

class SshLogin(interfaces.ISingleTask):
    def __init__(self, dictTask):
        self.__targets= dictTask["Targets"]
        self.__name = dictTask["Name"]

    def GetInteractiveName(self):
        return self.__name

    def Execute(self):
        n = len(self.__targets)
        print(Fore.RED + DISPLAY_DEV_STR.format("number", "name", "dev_name", "description"))
        for devIdx in range(0, n):
          print(Fore.BLUE + DISPLAY_DEV_STR.format(devIdx, self.__targets[devIdx]["name"],self.__targets[devIdx]["devname"], self.__targets[devIdx]["desc"]) + Fore.GREEN)

        userip = int(input("\nEnter the number of the device to login? " ))

        print (Style.RESET_ALL)

        if (userip >= 0 and userip <=n-1):
          cmd = COMMAND + self.__targets[userip]["devname"]
          print("Using the command: {}".format(cmd))
          os.system(cmd)

