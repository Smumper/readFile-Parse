# Programmiert in Python 3.7.3
# Aus geschwindigkeits gründen wird das file mit lambda ausgelesen und als liste ausgegeben


class readFile:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, "r", newline="", encoding="utf-16") as file:
            return list(map(lambda x: x, file))

