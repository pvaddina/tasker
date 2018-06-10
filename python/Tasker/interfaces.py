'''
Created on 21.01.2018
@author: Vaddina Prakash Rao
'''

from abc import ABCMeta, abstractmethod

class ISingleTask(metaclass=ABCMeta):
    __name = "DummyName"
    
    @abstractmethod
    def GetInteractiveName(self):
        pass
    
    @abstractmethod
    def Execute(self):
        pass


'''
class IWorkPackage(metaclass=ABCMeta):
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
    
class IExecutableTask(metaclass=ABCMeta):
    __name = "DummyName"
    
    @abstractmethod
    def Execute(self):
        pass
    
    @abstractmethod
    def DummyExecute(self):
        pass
'''



