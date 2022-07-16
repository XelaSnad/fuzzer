def constructCsvList(string):
    CSVlist = [] 

    for idx, line in enumerate(string.split('\n')):
        if ((idx + 1) != len(string.split('\n')) or line != ""):
            CSVlist.append(line)

    return CSVlist
    

if __name__ == '__main__':
    string = "0, 1, 0\n0, 1, 0\n6, 9, 6\n"

    print(constructCsvList(string))
