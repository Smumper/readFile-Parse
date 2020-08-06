class MSR:
    def Information(self, t1):
        if t1 == "":
            print("HALLO")
        else:
            pass

    def Alarme(self, t2):
        pass

    def Parameter(self, t2):
        pass

    def Tack(self):
        pass

    def analyse(self, t1, t2):
        self.Information(t1)
        self.Alarme(t2)
        self.Parameter(t2)
        self.Tack()


class Mbin(MSR):
    def Alarme(self, t2):
        pass


t1 = ""
t2 = "1"
msr = MSR()
test = Mbin()
print(test.analyse(t1, t2))
