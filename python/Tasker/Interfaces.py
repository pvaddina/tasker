'''
Created on 21.01.2018
@author: vaddina
'''

from abc import ABCMeta, abstractmethod

class ITaskGroup:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def Print(self):
        pass
    
    @abstractmethod
    def Interact(self):
        pass
    
    
class ISingleTask:
    __metaclass__ = ABCMeta
    __name = "DummyName"
    
    @abstractmethod
    def Print(self):
        pass
    
    @abstractmethod
    def Interact(self):
        pass
    
    @abstractmethod
    def GetInteractiveName(self):
        pass
    
    @abstractmethod
    def Execute(self):
        pass


class IExecutableTask:
    __metaclass__ = ABCMeta
    __name = "DummyName"
    
    @abstractmethod
    def Execute(self):
        pass
    
    @abstractmethod
    def DummyExecute(self):
        pass



