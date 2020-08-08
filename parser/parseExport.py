from parser.parseFile import parseFile


class parseExport(parseFile):
    # Auto parsing bei True dann muss daten file direkt angegeben werden
    def __init__(self, data=[], parsing=None):
        self.key_worte = [
            "[BEGIN_PROJECTHEADER]",
            "[BEGIN_AREADEFINITION]",
            "[END_AREADEFINITION]",
            "[BEGIN_EAMSECTION]",
            "[END_EAMSECTION]",
            "[BEGIN_MSRSECTION]",
            "[END_MSRSECTION]",
            "[BEGIN_PBAUMSECTION]",
            "[END_PBAUMSECTION]",
            "[BEGIN_HARDWAREMANAGER]",
            "[END_HARDWAREMANAGER]",
            "[BEGIN_RESOURCEASSOCIATIONSECTION]",
            "[END_RESOURCEASSOCIATIONSECTION]",
            "[PBV:OBJPATH]",
            "FGRBLT",
            "Pool",
        ]

        if parsing is None:
            self.parse(data)

    def parse(self, data):
        self.data = data
        self.fgr_row = []
        for count, row in enumerate(data):
            if self.key_worte[0] in row:
                self.Projekt_c = count
            if self.key_worte[1] in row:
                self.area_a = count
            if self.key_worte[2] in row:
                self.area_e = count
            if self.key_worte[3] in row:
                self.var_a = count
            if self.key_worte[4] in row:
                self.var_e = count
            if self.key_worte[5] in row:
                self.msr_a = count
            if self.key_worte[6] in row:
                self.msr_e = count
            if self.key_worte[7] in row:
                self.data_msr_a = count
            if self.key_worte[8] in row:
                self.data_msr_e = count
            if self.key_worte[9] in row:
                self.hwm_a = count
            if self.key_worte[10] in row:
                self.hwm_e = count
            if self.key_worte[11] in row:
                self.eam_a = count
            if self.key_worte[12] in row:
                self.eam_e = count
            if (
                self.key_worte[13] in row
                and self.key_worte[14] in row
                and not self.key_worte[15] in row
            ):
                self.fgr_row.append(count)

    def getProject(self):
        return self.data[self.Projekt_c]

    def getArea(self):
        return self.data[self.area_a : self.area_e]

    def getVar(self):
        return self.data[self.var_a : self.area_e]

    def getMSR(self):
        return self.data[self.msr_a : self.msr_e]

    def getPData(self):
        return self.data[self.data_msr_a : self.data_msr_e]

    def getHWM(self):
        return self.data[self.hwm_a : self.hwm_e]

    def getEAM(self):
        return self.data[self.eam_a : self.eam_e]

    def getFGR(self):
        return self.fgr_row
