from Fuzzer.MutationFuzzer import MutationFuzzer
from typing import Dict, Tuple, Union, List, Any
from random import randint, getrandbits
import json

class JsonFuzzer(MutationFuzzer):
    def init(self, seed: List[str], min_mutations: int = 2, max_mutations: int = 10) -> None:
        super().__init__(self, seed, min_mutations, max_mutations)

    def handleReccursion(self, data: Any) -> Any:
        '''The recurrsion function that will allow us to touch the entire json file and act upon it.'''


        for idx, i in enumerate(data):
            byte_or_repeat = bool(random.getrandbits(1)) #choses if we will byte flip or repeat

            if type(data) == dict:
                elem = data[i]
            else:
                elem = i

            if type(elem) == int or type(elem) == float:
                if byte_or_repeat:
                    elem = byte_flip(elem)
                else:
                    elem = repeated_parts(elem)

            elif type(elem) == dict or type(elem) == list:
                elem = handleReccursion(elem)
            elif type(elem) == str:
                if byte_or_repeat:
                    elem = byte_flip(elem)
                else:
                    elem = repeated_parts(elem)

            if type(data) == dict:
                data[i] = elem
            else:
                data[idx] = elem

        return data

class JsonFuzzer(MutationFuzzer):
    def mutate(self, inp:str) -> str:
        
        jsonobject = json.loads(inp)

        for idx, data in enumerate(jsonobject):             
            if type(jsonobject) == dict:
                jsonobject[data] = self.handleReccursion(data)
            else:
                jsonobject[idx] = self.handleReccursion(data)

        return json.dumps(jsonobject)
   
