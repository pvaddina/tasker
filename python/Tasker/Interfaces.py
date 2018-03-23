'''
Created on 21.01.2018
@author: vaddina
'''

from abc import ABCMeta, abstractmethod

class ITaskGroup(metaclass=ABCMeta):
    @abstractmethod
    def Print(self):
        pass
    
    @abstractmethod
    def GetInteractiveName(self):
        pass
    
    @abstractmethod
    def Interact(self):
        pass
    
    @abstractmethod
    def Execute(self):
        pass
    
    
class ISingleTask(metaclass=ABCMeta):
    __name = "DummyName"
    
    @abstractmethod
    def Print(self):
        pass
    
    @abstractmethod
    def GetInteractiveName(self):
        pass
    
    @abstractmethod
    def Interact(self):
        pass
    
    @abstractmethod
    def Execute(self):
        pass
    
    @abstractmethod
    def GetTask(self):
        pass


class IExecutableTask(metaclass=ABCMeta):
    __name = "DummyName"
    
    @abstractmethod
    def Execute(self):
        pass
    
    @abstractmethod
    def DummyExecute(self):
        pass



