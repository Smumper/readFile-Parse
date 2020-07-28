from abc import ABCMeta, abstractmethod


class MSRStelle:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getAlarm(self):
        pass
