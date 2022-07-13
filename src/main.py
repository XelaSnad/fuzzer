from fileTypes import *
import sys

if len(sys.argv) != 3: 
    print("Number of arguments incorrect, this program requires sample input and a binary.")

binary = sys.argv[1] 
binaryInput = sys.argv[2]

with open(binaryInput, "r", encoding="ISO-8859-1") as file:
    input = file.read()

inputType = findInputType(input)

#We need to get jpg working and pdf and elf ability by the end of the project.

print(inputType)