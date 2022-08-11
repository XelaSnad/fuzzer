'''
    This is the main function nice
'''
#!/usr/bin/env python3
import sys
from FileIdentifier import FileIdentifier
from Runner.ProgramRunner import ProgramRunner
from Fuzzer.FuzzerFactory import FuzzerFactory

INPUT_TYPE = "?"

if len(sys.argv) != 3:
    print("Number of arguments incorrect, this program requires sample input and a binary.")
    sys.exit(0)

binaryInput = sys.argv[1]
binary = sys.argv[2]

with open(binaryInput, "r", encoding="ISO-8859-1") as file:
    input = file.read()

typeFinder = FileIdentifier(input)
INPUT_TYPE = typeFinder.identify_type()



runner = ProgramRunner(binary)
factory = FuzzerFactory()
fuzzer = factory.get_fuzzer(INPUT_TYPE, [input]*3, 1, 4)

mutated_input = ""

for rule in fuzzer.getRule():
    for triple in fuzzer.runs(rule, runner):
        (results, inputs, outcome) = triple
        if outcome == "FAIL":
            mutated_input = inputs 
        
    if mutated_input != "":
        break
    fuzzer.reset()



if mutated_input == "":
    print("no input found")
    exit()

f = open("bad.txt", "w")

f.write(mutated_input)

f.close()
print("bad.txt updated with bad input")

