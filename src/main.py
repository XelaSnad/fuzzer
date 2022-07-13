from fileTypes import *
import sys

if len(sys.argv) != 3: 
    print("Number of arguments incorrect, this program requires sample input and a binary.")

binary = sys.argv[1] 
binaryInput = sys.argv[2]

with open(binaryInput, "r") as file:
    input = file.read()

inputType = ""

if validateJSON(input):
    inputType = "json"
elif validateCSV(input):
    inputType = "csv"
elif validateJpg(input):
    inputType = "jpg"
elif validateXml(input):
    inputType = "xml"
elif input == "":
    inputType = "empty"
else:
    inputType = "plaintext"

#We need to get jpg working and pdf and elf ability by the end of the project.

print(inputType)