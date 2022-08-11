from Fuzzer.MutationFuzzer import MutationFuzzer
from typing import Dict, Tuple, Union, List, Any
from random import randint
import json

class JsonFuzzer(MutationFuzzer):   
    def init(self, seed: List[str], rules:List[str], min_mutations: int = 2, max_mutations: int = 10) -> None:
        super().__init__(self, seed, rules, min_mutations, max_mutations)


    def mutate(self, inp:str) -> str:

        jsonobject = json.loads(inp)
        for idx, data in enumerate(jsonobject):
            match self.getCurrentRule():
                case "overflow":
                    if type(jsonobject) == dict:
                        jsonobject[data] = self.handleReccursion(data, "A"*10000)
                    else:
                        jsonobject[idx] = self.handleReccursion(data, "A"*10000)
                case "zero":
                    if type(jsonobject) == dict:
                        jsonobject[data] = self.handleReccursion(data, 0)
                    else:
                        jsonobject[idx] = self.handleReccursion(data, 0)
                case "positive":
                    if type(jsonobject) == dict:
                        jsonobject[data] = self.handleReccursion(data, 1)
                    else:
                        jsonobject[idx] = self.handleReccursion(data, 1)
                case "negative":
                    if type(jsonobject) == dict:
                        jsonobject[data] = self.handleReccursion(data, -1)
                    else:
                        jsonobject[idx] = self.handleReccursion(data, -1)
                case "large_postive":
                    if type(jsonobject) == dict:
                        jsonobject[data] = self.handleReccursion(data, 10**55)
                    else:
                        jsonobject[idx] = self.handleReccursion(data, 10**55)
                case "large_negative":
                    if type(jsonobject) == dict:
                        jsonobject[data] = self.handleReccursion(data, -10**55)
                    else:
                        jsonobject[idx] = self.handleReccursion(data, -10**55)
                case "format":
                    if type(jsonobject) == dict:
                        jsonobject[data] = self.handleReccursion(data, "%n")
                    else:
                        jsonobject[idx] = self.handleReccursion(data, "%n")
        return json.dumps(jsonobject)


    def handleReccursion(self, data: Any, payload) -> Any:
        '''The recurrsion function that will allow us to touch the entire json file and act upon it.'''

        if type(data) == str or type(data) == int or type(data) == float:
            return payload

        for idx, i in enumerate(data):
            if type(data) == dict:
                data[i] = self.handleRecurrsion(data, payload)
            elif type(data) == List:
                data[idx] = self.handleRecurrsion(data, payload)
        
        return data


