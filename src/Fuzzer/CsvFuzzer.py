from Fuzzer.MutationFuzzer import MutationFuzzer
from typing import Dict, Tuple, Union, List, Any
import random

class CsvFuzzer(MutationFuzzer): 
    def init(self, seed: List[str], rules: List[str], min_mutations: int = 1, max_mutations: int = 5) -> None:
        super().__init__(self, seed, rules, min_mutations, max_mutations)
    
    def mutate(self, inp:str) -> str:
        
        strings = self.deconstructCsv(inp)
        
        match self.getCurrentRule():
            case "overflow_rows":
                strings = self.handleRows(strings)
                strings = self.constructCsv(strings)*3
                strings = self.deconstructCsv(strings)
            case "overflow_values":
                strings = self.handleMutate(strings, "A"*10000)
            case "zero":
                strings = self.handleMutate(strings, "0")
            case "positive":
                strings = self.handleMutate(strings, "1")
            case "negative":
                strings = self.handleMutate(strings, "-1")
            case "large_negative":
                strings = self.handleMutate(strings, f"{-10**55}")
            case "large_positive":
                strings = self.handleMutate(strings, f"{10**55}")
            case "null_terminator":
                strings = self.handleMutate(strings, "\0")
            case "format":
                strings = self.handleMutate(strings, "%x%n")
        
        strings = self.constructCsv(strings)
        return strings

    def handleMutate(self, strings, payload): 
        for idx1, row in enumerate(strings):
            values = strings[idx1].split(",")
            for idx2, value in enumerate(values):
                values[idx2] = payload 
            strings[idx1] = ",".join(values)
        return strings

    def handleRows(self, strings) -> List[str]:
        chosen_row = random.randint(0, len(strings) - 1)
        for idx1, row in enumerate(strings):
            if idx1 == chosen_row:
                values = strings[idx1].split(",")
                for idx2, value in enumerate(values):
                    values[idx2] = "A" * 100
                strings[idx1] = ",".join(values)
        return strings

        
    def deconstructCsv(self, string: str) -> List:
        '''
        Deconstructs a CSV string into a list of those comma seperated values.
        '''
        CSVlist = []

        for idx, line in enumerate(string.split('\n')):
            if ((idx + 1) != len(string.split('\n')) or line != ""):
                CSVlist.append(line)

        return CSVlist

    def constructCsv(self, stringList: List) -> str:
        ''' Reconstructs a CSV string list into a string that is comma seperated'''
        string = ""
        for idx, line in enumerate(stringList):
            string = string + line + "\n"
        return string
