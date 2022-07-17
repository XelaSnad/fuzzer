# COMP6447 Major Project
## Group Name

### About
Fuzzing is a system testing process with the goal of checking a program for bugs that can be exploited by user input. This is done by automatically feeding semi-random data into the program's input and running it repeatedly with added variations to the input data until an error is found; alerting the user to the error as well as the data that caused it. If no errors are found, the fuzzer returns with an empty result.

Our project consists of a basic implementation of a fuzzer, with the intention of using the fuzzer's output to exploit the data ourselves, rather than repairing the faulty program. 


### Constraints
There are several limitations that must be placed on our fuzzer in order to gain maximal marks within the course. These constraints are as follows:

1. The fuzzer is a black-box tester: it has no knowledge of the programs' source code and we, the developers, will have no insight to the source code to guide our implementation of the function.
2. The fuzzer is only fed the binary file of the program it is checking, as well as a base `input.txt` file to be mutated and fed as input to the program.
3. The fuzzer is to be implemented using our own methods and functions and no external programs will be used to assist us.
4. The fuzzer's goal is to search for a change of expected state of the program. Some examples of unexpected states are:
   - Program crash
   - Invalid memory access or write
   - Heap Use-After-Free (UAF)


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
Once the fuzzer has determined the validity of its arguments, it will verify the file type of the text file. This is done through `src/fileTypes.py`, which parses the binary file into each specified format; if any format returns a valid result, the file type will be returned to `main.py`. If no valid result is returned, the text file will be treated as plaintext.

#### Data Mutation
The fuzzer then begins to formulate its data inputs to be used for testing. These consist of different methods for each file type.

##### JSON
There are currently two steps taken to mutate the input data. First is through byte flipping, second is through repeated parts. Each fuzzer call will generate 10 input strings for each method and append them to an array to be parsed to the binary file. 

For each method, the fuzzer must consider the basic input data in the text file. It will take each element of the text file, which could be in the format of a list or simply each byte of the file, then determine its type. If the elements are strings, integers, floats or any basic data type, it will mutate each element and add them to the output array. If the element is a dict type or an element of an array, it will recursively mutate each of these sub-elements in the same manner before adding them to the output string.

Byte-flipping is a recursive process that repeats either for every element of a string, or 7 times for a number type. For numbers, it will create an array of 254 elements with each element being a variation of the original number, the number with its bytes flipped, or None. For strings, the byte-flipper will return an array with the original string first, before returning variations of byte flips for each character in the string. All array elements are different, and some also equate to None.

The repeated parts method invokes larger mutations over strings. It will add to the output array a large list of variations of the string by using pointers variables to take subsets of one or more chars and repeating them a number of times (between 0 and 10) and appending them to the subset. For a number type, the repeated parts will add this number multiplied by a random integer between 1 and 10 to the output array.

Following these steps, the fuzzer will create an output array of every potential mutation of the data given to it. Obviously, this array will be much too large to run our fuzzer in the appropriate time limitations; so to prevent the program from taking a lengthy execution time, the fuzzer will randomly select a sample of the output array to be passed to the binary file. 

##### CSV
Due to the unique formatting of the `csv*.txt` files, there is a deviation from the above steps.

The fuzzer will first desconstruct the sample data into an array of comma-separated values. From there, the fuzzer will select a random element from the array, then in turn select a random column. For whichever string exists in that element, the fuzzer will change it to a char 'A' repeated several times (between 20 and 100), in order to attempt a buffer overflow. The fuzzer will then convert the array back into csv and return it for the binary to test.

#### Run File
With the sample output generated, the fuzzer can begin testing the binary files for an error. 

The fuzzer will take each array element of the sample output and use it as input for the binaries, running it each time. Each time that the fuzzer is ran, it will add the outcome of each binary execution as well as the data parsed to it to its own array.

This array will then be checked for any program outcomes that do not contain a 0, that is, any time the binary does not complete execution in its expected state. If any such error is found, the fuzzer will return to the user the error that was given at the time of execution, as well as the data which caused it. If no such error existed, the fuzzer will inform the user of this before it completes execution. 

### Planned Improvements
As of currently, the fuzzer is solely used to test on csv and json filetypes. The project members will continue their implementation of the fuzzer to run for all planned filetypes for the project's release. Additionally, the current mutations implementation only causes a binary crash resulting from the Repeated Parts, not from Byte Flipping. This is also planned to be improved upon for final release.

Whilst the methods of data mutation are quite thorough, the project acknowledges the time complexity of mutation, particularly for larger data text files. The project members will explore ways to both cut down on the time complexity as well as focus the data mutation's methods towards an output with a higher chance of finding binary errors. 
