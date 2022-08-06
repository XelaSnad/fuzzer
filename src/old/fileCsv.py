#from fileRun import fileExecuteText
import random

'''
Deconstructs a CSV string into a list of comma seperated values 
'''
def deconstructCsv(string):
    CSVlist = []

    for idx, line in enumerate(string.split('\n')):
        if ((idx + 1) != len(string.split('\n')) or line != ""):
            CSVlist.append(line)

    return CSVlist

'''
Reconstructs a CSV string list into a string that is comma seperated
'''
def constructCsv(stringList):
    string = ""
    for idx, line in enumerate(stringList):
        string = string + line + "\n"
    return string

#selects a random value in the comma seperated value, picks a row and column and then makes that string a random amount of "A" characters"
def randomValueChange(sample):
    strings = deconstructCsv(sample)
    row = 0
    col = 0
    result = ""
    row = random.randint(0, (len(strings) - 1))
    for idx1, string in enumerate(strings):
        if idx1 == row:
            values = string.split(",")
            col = random.randint(0, (len(values) - 1))
            for idx2, value in enumerate(values):
                if idx2 == col:
                    values[col] = "A" * random.randint(20, 100)
                    result = ",".join(values)
                    break
    strings[row] = result
    return constructCsv(strings)


# The fuzzer style is that it is run through twice in random value and then the string is appended to itself a number of times
if __name__ == '__main__':
    string = "header,must,stay,intact\na,b,c,S\ne,f,g,ecr\ni,j,k,et"
    value = randomValueChange((randomValueChange(string)))

    #print(fileExecuteText("../binaries/csv1", value * random.randint(1,20)))
