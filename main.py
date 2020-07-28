# Lib imports
import itertools

# Klassen Imports
from readFile import readFile
from parser.parseFile import parseFile
from parser.parseExport import parseExport
from projectinfo import Project_information
from Area import Areas

# msr Rec zu dict wandeln
def msr_rec_dict(data):
    msr_rec = {}
    for line in itertools.islice(data, len(data) + 1, len(data) - 1, 2):
        msr_rec.update({line.strip().split(";")[2]: line})
    return msr_rec


# Pdata zu dict umwandeln
def Pdata_dict(data):
    P_Data = {}
    for pdata in range(0, len(data)):
        if "[LAD:MSR_REF]" in data[pdata]:
            msr_name = data[pdata].strip().split(";")[1]
            P_Data.update({msr_name: data[pdata + 1]})
    return P_Data


filepath = (
    "/Users/peterschwarz/VS Code Projekte/readFile-Parse/elektrolyse_20200326.csv"
)
file = readFile(filepath)
parsing_file = parseExport()
parsing_file.parse(file.read())
print(Pdata_dict(parsing_file.getPData()))
