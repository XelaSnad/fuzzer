import sys
import subprocess

from fileTypes import *

from fileRun import findInputs


if len(sys.argv) != 3: 
    print("Number of arguments incorrect, this program requires sample input and a binary.")
    sys.exit(0)

binaryInput = sys.argv[1]
binary = sys.argv[2] 

with open(binaryInput, "r", encoding="ISO-8859-1") as file:
    input = file.read()

inputType = findInputType(input)
print(f"{inputType} file detected")

#We need to get jpg working and pdf and elf ability by the end of the project.

# for now just looks for the first input that will crash
mutated_input = ""

mutated_input = findInputs(binary, input, inputType)

if mutated_input == "":
    print("no input found")
    exit()

f = open("bad.txt", "w")

f.write(mutated_input)

f.close()
print("bad.txt updated with bad input")