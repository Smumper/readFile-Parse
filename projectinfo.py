class ProjektInformation:
    def __init__(self, data):
        self.data = data.split(";")

    def getName(self):
        pass

    def getComm(self):
        pass

    def getCreater(self):
        pass

    def getCompany(self):
        pass

    def getVersionDate(self):
        pass

    def getCreationDate(self):
        pass

    def output(self):
        out_dict = {
            "Name": self.getName(),
            "Kommentar": self.getComm(),
            "Ersteller": self.getCreater(),
            "Firma": self.getCompany(),
            "Version": self.getVersionDate(),
            "Erstellung": self.getCreationDate(),
        }
        return out_dict


class Freelance(ProjektInformation):
    def getName(self):
        return self.data[1]

    def getComm(self):
        return self.data[2]

    def getCreater(self):
        return self.data[3]

    def getCompany(self):
        return self.data[14]

    def getVersionDate(self):
        date = str(self.data[6] + "." + self.data[7] + "." + self.data[8])
        time = str(self.data[9] + "." + self.data[10] + "." + self.data[11])
        return date + ":" + time

    def getCreationDate(self):
        date = str(self.data[20] + "." + self.data[21] + "." + self.data[22])
        time = str(self.data[23] + "." + self.data[24] + "." + self.data[25])
        return date + ":" + time
