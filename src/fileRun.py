from subprocess import *
from sys import stdout
from tempfile import NamedTemporaryFile, tempdir
import os
import json

from fileCsv import randomValueChange
from fileJson import generate_samples_byte_flips, generate_samples_repeated_parts

# repeatedly generates inputs and tests them until one is found that crashes the given binary
def findInputs(binary, input, inputType):

    # set an upper limit of 20 runs for now
    max_runs = 20
    bad_input = ""

    if inputType == "json":

        # generate inputs
        #gen_input = generate_samples_byte_flips(json.loads(input), max_runs)
        gen_input = generate_samples_repeated_parts(json.loads(input), max_runs)
        for i in range(max_runs):
            # create a temporary file with the generated input
            temp = NamedTemporaryFile()
            temp.write(json.dumps(gen_input[i]).encode("utf-8"))
            temp.seek(0)
            print(temp.name)
            print(f"trying: \n {gen_input[i]}")
            try:
                # test to see if input causes an error. currently all errors, including non memory errors will pass
                check_call("cat " + temp.name + " | ./" + binary, stdout=DEVNULL, shell=True)
            except CalledProcessError as e:
                print(f"bad input found, produces the following error:\n {e}")
                bad_input = json.dumps(gen_input[i])
                break

    elif inputType == "csv":
        print("generating inputs")
        for i in range(max_runs):
            # generate an input
            print(f"attempt {i}")
            gen_input = randomValueChange((randomValueChange(input)))

            # create a temporary file with the generated input
            temp = NamedTemporaryFile()
            temp.write(gen_input.encode("ISO-8859-1"))
            temp.seek(0)
            print(temp.name)
            print(f"trying: \n {gen_input}")

            try:
                # test to see if input causes an error. currently all errors, including non memory errors will pass
                check_call("cat " + temp.name + " | ./" + binary, shell=True)
                temp.close()
            except CalledProcessError as e:
                print(f"bad input found, produces the following error:\n {e}")
                bad_input = gen_input
                temp.close()
                break

    return bad_input
    
# tests the generated file against the binary
def try_input(temp, binary):
    try:
        print("hi")
        # test to see if input causes an error. currently all errors, including non memory errors will pass
        check_call("cat " + temp.name + " | ./" + binary, shell=True)
        temp.close()
    except CalledProcessError as e:
        print(f"bad input found, produces the following error:\n {e}")
        temp.close()


# def fileExecuteText(program, text) :
#     text = text.encode('utf-8')
    
#     p = Popen([program], stdout = PIPE, stdin = PIPE)
#     out = p.communicate(input=text)
#     return (out, p, text)

# '''
# This function runs a list of inputs into a binary and returns a list of the resulting output
# '''
# def runTrials(binary, textList):
#     returnList = []
#     for idx, text in enumerate(textList):
#         result = fileExecuteText(binary, text)
#         returnList.append(result)
#     return returnList


if __name__ == '__main__':
    gen_input = "header,must,stay,inasdtact\na,b,c,S\ne,f,g,ecr\ni,j,k,et"
    temp = NamedTemporaryFile()
    temp.write(gen_input.encode("ISO-8859-1"))
    temp.seek(0)
    try_input(temp, "csv1")

    

