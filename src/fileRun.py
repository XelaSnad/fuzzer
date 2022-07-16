import os 
import subprocess
import tempfile

def fileExecuteText(program, text) :
    text = text.encode('utf-8')
    
    p = subprocess.Popen([program], stdout = subprocess.PIPE, stdin = subprocess.PIPE)
    out = p.communicate(input=text)
    return (out, p, text)

'''
This function runs a list of inputs into a binary and returns a list of the resulting output
'''
def runTrials(binary, textList):
    returnList = []
    for idx, text in enumerate(textList):
        result = fileExecuteText(binary, text)
        returnList.append(result)
    return returnList


if __name__ == '__main__':
    print(fileExecuteText("../binaries/csv1", "headermust,stay,intact\na,b,c,S\ne,f,g,ecr\ni,j,k,et"))

    

