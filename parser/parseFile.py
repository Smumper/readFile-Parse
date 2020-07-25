from abc import ABCMeta, abstractmethod


class parseFile:
    __metaclass__ = ABCMeta

    @abstractmethod
    def parseMSR(self):
        pass
