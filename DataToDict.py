import types
import itertools

# Aufruf funktion in dem DataToDict(Angabe der Aufgerufenen funktion)
# durch .data muss daten zuerst übergeben werden.
# Durch .execute wird Funktion ausgeführt und zurück gegeben.
class DataToDict:
    def __init__(self, func=None):
        self.data = []
        self.__data_dict = {}
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        return self.__data_dict


# Area in Dict wandeln
def Area(self):
    for count, line in enumerate(self.data[1:-1], start=-len(self.data) + 1,):
        self.__data_dict.update({2 ** abs(count): line.strip().split(";")[-1]})
    return self.__data_dict


# msr Rec zu dict wandeln
def MSRRec(self):
    for line in itertools.islice(self.data, len(self.data) + 1, len(self.data) - 1, 2):
        self.__data_dict.update({line.strip().split(";")[2]: line})
    return self.__data_dict


# Pdata zu dict umwandeln
def Pdata(self):
    for pdata in range(0, len(self.data)):
        if "[LAD:MSR_REF]" in self.data[pdata]:
            msr_name = self.data[pdata].strip().split(";")[1]
            self.__data_dict.update({msr_name: self.data[pdata + 1]})
    return self.__data_dict

