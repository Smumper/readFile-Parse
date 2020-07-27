from abc import ABCMeta, abstractmethod


class parseFile:
    __metaclass__ = ABCMeta

    def __init__(self, data=[], parsing=False):
        pass

    @abstractmethod
    def parse(self, data):
        pass

    @abstractmethod
    def getProject(self):
        pass

    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getVar(self):
        pass

    @abstractmethod
    def getMSR(self):
        pass

    @abstractmethod
    def getPData(self):
        pass

    @abstractmethod
    def getHWM(self):
        pass

    @abstractmethod
    def getEAM(self):
        pass

    @abstractmethod
    def getFGR(self):
        pass
