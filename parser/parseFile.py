from abc import ABCMeta, abstractmethod


class parseFile:
    __metaclass__ = ABCMeta

    def __init__(self, data=[], parsing=False):
        pass

    @abstractmethod
    def parse(self, data):
        pass

    @abstractmethod
    def parsedMSR(self):
        pass
