from readFile import readFile
from parser.parseFile import parseFile
from parser.parseExport import parseExport

filepath = (
    "/Users/peterschwarz/VS Code Projekte/readFile-Parse/elektrolyse_20200326.csv"
)
data = readFile(filepath)
test = parseExport()
print(test.parseMSR())
