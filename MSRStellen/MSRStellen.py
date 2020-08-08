# Input sind zwei Dicts einmal record und einmal para data
# Output kann einzeln oder über eine For schleife o.Ä. abgefragt werden.
class MSR:
    def Information(self, record):
        if record == "":
            print("HALLO")
        else:
            pass

    def Alarme(self, para_data):
        pass

    def Parameter(self, para_data):
        pass

    def analyse(self, record, para_data):
        self.Information(record)
        self.Alarme(para_data)
        self.Parameter(para_data)


class Mbin(MSR):
    def Alarme(self, para_data):
        pass

    def Parameter(self, para_data):
        pass


class Mana(MSR):
    def Alarme(self, para_data):
        pass

    def Parameter(self, para_data):
        pass


class C_C(MSR):
    def Alarme(self, para_data):
        pass

    def Parameter(self, para_data):
        pass

