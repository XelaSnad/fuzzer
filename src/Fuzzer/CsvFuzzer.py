from Fuzzer.MutationFuzzer import MutationFuzzer
from typing import Dict, Tuple, Union, List, Any


class CsvFuzzer(MutationFuzzer):
    def init(self, seed: List[str], min_mutations: int = 2, max_mutations: int = 10) -> None:
        super().__init__(self, seed, min_mutations, max_mutations)

    def deconstructCsv(inp: str) -> List:
        '''
        Deconstructs a CSV string into a list of those comma seperated values.
        '''
        CSVlist = []

        for idx, line in enumerate(string.split('\n')):
            if ((idx + 1) != len(string.split('\n')) or line != ""):
                CSVlist.append(line)

        return CSVlist

    def constructCsv(inp: List) -> str:
        ''' Reconstructs a CSV string list into a string that is comma seperated'''
        string = ""
        for idx, line in enumerate(stringList):
            string = string + line + "\n"
        return string
