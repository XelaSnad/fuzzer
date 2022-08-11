# COMP6447 Major Project
## FuzzYourSocks OFF

### About
In this last huddle we have only had Yukon and I(Alex) working on the project, the rest of the team has been pretty unresponsive in chat and have made little effort, even Yukon hasn't done too much.

The new fuzzer has been completely re-designed with an object oriented style using a factory to figure out which file fuzzer to use depending on the file type, each fuzzer has a set of vulnerability type it looks for and then iterates through them until it reaches a crash.

### Constraints
There are several limitations that must be placed on our fuzzer in order to gain maximal marks within the course. These constraints are as follows:

1. The fuzzer is a black-box tester: it has no knowledge of the programs' source code and we, the developers, will have no insight to the source code to guide our implementation of the function.
2. The fuzzer is only fed the binary file of the program it is checking, as well as a base `input.txt` file to be mutated and fed as input to the program.
3. The fuzzer is to be implemented using our own methods and functions and no external programs will be used to assist us.
4. The fuzzer's goal is to search for a change of expected state of the program. Some examples of unexpected states are:
   - Program crash
   - Invalid memory access or write



### Assumptions
Several assumptions have been provided to us regarding how the programs we are testing will operate. These assumptions are as follows:

1. All binaries have a vulnerability.
2. All binaries function normally when their relevant `input.txt` file is passed to them, that is: 
   - they will return 0, 
   - they will not crah or throw errors from the base `input.txt` file.
3. All binaries will expect an input in the following format: 
   - Multiline plaintext, 
   - JSON, 
   - XML, 
   - CSV, 
   - JPEG, 
   - ELF, 
   - PDF.
4. The `input.txt` provided will be a valid form of one of the above text formats.
5. The fuzzer has a *maximum of 180 seconds* per binary to find the vulnerability. If the fuzzer takes longer to find said vulnerability, **it will not count as a solution**.
6. All binaries will be 32bit Linux ELF's (except for xml3).
7. All vulnerabilities will result in memory corruption.

### Current Implementation

#### Fuzzer Start
The fuzzer is ran from the command line and requires 2 arguments:
1. The binary file to be tested
2. The base binary input file to be manipulated and ran as input for the binary file specified in argument 1

The fuzzer will throw an error if any of the following cases occur on program start:
1. The fuzzer does not receive the correct number of arguments
2. The arguments are provided in incorrect order
3. Argument 1 is not a valid binary
4. Argument 2 is not a valid text file or cannot be read

#### Preliminary Testing
Once the fuzzer has determined the validity of its arguments, it will verify the file type of the text file. This is done through `src/FileIdentifier.py`, which parses the binary file into each specified format; if any format returns a valid result, the file type will be returned to `main.py` to then be sent through the Fuzzer Factory to produce a fuzzer.

#### Data Mutation
The fuzzer then begins to formulate its data inputs to be used for testing.

Since last time we have removed the basic methodology of bit and byte flipping all though you could configure the project to re-enable such features but now our rules determine what goes on, the basic rules for csv for example are 

- overflow_rows
	Where a random row is chosen to be overflown with 100 or so A's
- Overflow_values all values are overflown with 10000 A's
- zero all values set to zero
- positive all values set to 1
- negative all values set to -1
- large_postiive all values set to 1 * 10^55
- Null Term all values set to null terminators
- format all values set to %x%s
- large_negative all values set to -1*10^55

###

### Run File
With the sample output generated, the fuzzer can begin testing the binary files for an error. 

The fuzzer will take each array element of the sample output and use it as input for the binaries, running it each time. Each time that the fuzzer is ran, it will add the outcome of each binary execution as well as the data parsed to it to its own array.

This array will then be checked for any program outcomes that do not contain a 0, that is, any time the binary does not complete execution in its expected state. If any such error is found, the fuzzer will return to the user the error that was given at the time of execution, as well as the data which caused it. If no such error existed, the fuzzer will inform the user of this before it completes execution. 

### Proudness
I am definitely proud of the simplicity of this project enabled by the various classes used, it allowed me to limit redundancy that I feel could occur with such a project and although not related to course outlines definitely aided me in understnading oop concepts in general.

### Improvements
There are the obvious improvements being able to hit all the vulns in the files, having all file types completed but alas this was too much for pretty much one team member to do. 

If I were to have more time I would of focused on firstly re-enabling bit manipulations so that the test cases would hit that and also I wold want to add perhaps being able to choose your favoured method of fuzzing. 

I would of liked to add harness functionality we currently tell you which rule caused the crash which can be helpful but it doesn't make it obvious if you don't understand the rules. 

Another thing i'd of liked to have done better would of been to making the interaction between fuzzing and binary better being able to detect changes in the programs state i.e. code coverage knowing we are hitting a different part of the program than last time. 

All though there is tones of areas for improvement I am pretty proud of the amount of code I got to build on my own.  
