from readFile import readFile
from parser.parseFile import parseFile
from parser.parseExport import parseExport

filepath = (
    "/Users/peterschwarz/VS Code Projekte/readFile-Parse/elektrolyse_20200326.csv"
)
file = readFile(filepath)
parsing_file = parseExport()
parsing_file.parse(file.read())
