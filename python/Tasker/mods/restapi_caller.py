'''
Created on 22.10.2018
@author: Vaddina Prakash Rao
'''

import interfaces

import requests
import sys
import pprint
import json


###############################################################################
#
# RestApiCaller
#
###############################################################################

class RestApiCaller(interfaces.ISingleTask):
    def __init__(self, dictTask):
        self.__url = dictTask["url"]
        self.__apiKey = dictTask["apiKey"]
        self.__name = dictTask["Name"]

    def GetInteractiveName(self):
        return self.__name

    def Execute(self):
        url = self.GetUrl()
        print("URL = %s" % (url))
        try:
            r = requests.get(url)
            print("Result code = %d" % (r.status_code))
            pprint.pprint(r.json())
        except:
            print("Something did not work !!!")

    def GetUrl(self):
        if self.__url == "":
            return input("Enter the complete URL along with apiKey:")
        self.__url = self.__url.replace("__API_KEY__", self.__apiKey)
        return self.__url


