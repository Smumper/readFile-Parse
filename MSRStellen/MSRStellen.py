class MSR:
    __Alarme = {}
    __Info = {}

    def Information(self, record):
        if record == "":
            print("HALLO")
        else:
            pass

    def Alarme(self, t2):
        pass

    def Parameter(self, t2):
        pass

    def Tack(self):
        pass

    def analyse(self, record, para_data):
        self.Information(record)
        self.Alarme(para_data)
        self.Parameter(para_data)
        self.Tack()


class Mbin(MSR):
    __Alarme = {}
    __Info = {}

    def Alarme(self, para_data):
        pass

    def Parameter(self, para_data):
        pass


class Mana(MSR):
    __Alarme = {}
    __Info = {}

    def Alarme(self, para_data):
        pass

    def Parameter(self, para_data):
        pass


class C_C(MSR):
    __Alarme = {}
    __Info = {}

    def Alarme(self, para_data):
        pass

    def Parameter(self, para_data):
        pass


t1 = ""
t2 = "1"
msr = MSR()
test = Mbin()
print(test.analyse(t1, t2))
