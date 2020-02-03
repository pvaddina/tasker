'''
Created on 03.02.2020
@author: Vaddina Prakash Rao
'''

import interfaces
import utils

###############################################################################
#
# RepoBuild
#
###############################################################################

class RepoBuild(interfaces.ISingleTask):
    def __init__(self, dictTask, rtOptionHandler):
        self.__name= dictTask["Name"]
        rtOptionName = dictTask["RtOptions"]

    def GetInteractiveName(self):
        return self.__name

    def Execute(self):
        pass
