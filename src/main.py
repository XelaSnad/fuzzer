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
print(fuzzer.runs(runner))

