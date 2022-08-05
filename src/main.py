#!/usr/bin/env python
from fileTypes import *
import fileJson
import sys
import subprocess

if len(sys.argv) != 3: 
    print("Number of arguments incorrect, this program requires sample input and a binary.")
    sys.exit(0)

binary = sys.argv[1] 
binaryInput = sys.argv[2]

with open(binaryInput, "r", encoding="ISO-8859-1") as file:
    input = file.read()

inputType = findInputType(input)

#We need to get jpg working and pdf and elf ability by the end of the project.


mutated_inputs = []




if inputType == "json":
    input = json.loads(input)
    mutated_inputs.append(fileJson.generate_samples_byte_flips(input, 10))
    mutated_inputs.append(fileJson.generate_samples_repeated_parts(input, 10))

    f = open("bad.txt", "w")

    for i in mutated_inputs:
        for j in i:

            f.write("\n")
            try:

                p = subprocess.run([binary], stdout = subprocess.PIPE,input = json.dumps(j).encode('utf-8'), check = True)
            except subprocess.CalledProcessError as e:
                f.write(str(j))
                f.write(str(e))