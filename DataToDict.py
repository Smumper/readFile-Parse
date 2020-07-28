import itertools


class DataToDict:
    # Area in Dict wandeln
    def AreaToDict(self, data):
        area_dict = {}
        for count, line in enumerate(data[1:-1], start=-len(data) + 1,):
            area_dict.update({2 ** abs(count): line.strip().split(";")[-1]})
        return area_dict

    # msr Rec zu dict wandeln
    def MSRRecToDict(self, data):
        msr_rec = {}
        for line in itertools.islice(data, len(data) + 1, len(data) - 1, 2):
            msr_rec.update({line.strip().split(";")[2]: line})
        return msr_rec

    # Pdata zu dict umwandeln
    def PdataToDict(self, data):
        P_Data = {}
        for pdata in range(0, len(data)):
            if "[LAD:MSR_REF]" in data[pdata]:
                msr_name = data[pdata].strip().split(";")[1]
                P_Data.update({msr_name: data[pdata + 1]})
        return P_Data
