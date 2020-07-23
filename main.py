from readFile import readFile

filepath = (
    "/Users/peterschwarz/VS Code Projekte/readFile-Parse/elektrolyse_20200326.csv"
)
data = readFile(filepath)
print(data.read())
