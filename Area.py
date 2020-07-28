# Es werden Areas als dict augegeben eingabe ist eine liste von Zeilen aus File.


class Areas:
    def __init__(self, data):
        self.data = data[1:-1]
        self.area_dict = {}
        self.areasize = str(data[0]).strip().split(";")
        self.evaluation()

    def evaluation(self):
        for count, line in enumerate(self.data, start=-len(self.data) + 1,):
            self.area_dict.update({2 ** abs(count): line.strip().split(";")[-1]})

    def getSystem(self):
        return self.area_dict[65536]

    def getKeinB(self):
        return self.area_dict[32768]

    def getA(self):
        return self.area_dict[16384]

    def getB(self):
        return self.area_dict[8192]

    def getC(self):
        return self.area_dict[4096]

    def getD(self):
        return self.area_dict[2048]

    def getE(self):
        return self.area_dict[1024]

    def getF(self):
        return self.area_dict[512]

    def getG(self):
        return self.area_dict[256]

    def getH(self):
        return self.area_dict[128]

    def getI(self):
        return self.area_dict[64]

    def getJ(self):
        return self.area_dict[32]

    def getK(self):
        return self.area_dict[16]

    def getL(self):
        return self.area_dict[8]

    def getM(self):
        return self.area_dict[4]

    def getN(self):
        return self.area_dict[2]

    def getO(self):
        return self.area_dict[1]
