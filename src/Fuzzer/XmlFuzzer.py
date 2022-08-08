from Fuzzer.MutationFuzzer import MutationFuzzer
from typing import Dict, Tuple, Union, List, Any
import xml.etree.ElementTree as ET
from random import *

class XmlFuzzer(MutationFuzzer):
    ''' The implementation of mutation when the input if of XML type'''

    def init(self, seed: List[str], min_mutations: int = 2, max_mutations: int = 10) -> None:
        super().__init__(self, seed, min_mutations, max_mutations)

    
    def mutate(self, inp:str) -> str:
        '''Mutate constructs a tree using XML etree, it finds its number of nodes then iterates through everything cand picks a random index, it will then do a bit flip on a random bit in that attribute (dictionaries) key pair value. Can miss '''


        root = ET.fromstring(inp)
        
        root = ET.fromstring(inp)
        node_list = []

        for idx, elem in enumerate(root.iter()):
            if len(elem.attrib) > 0:
                node_list.append(idx)

        index = randint(0, len(node_list) - 1)
        index = node_list[index]


        for idx, elem in enumerate(root.iter()):
            if idx == index:
                for key in elem.attrib:
                    print(elem.tag, elem.attrib)
                    elem.attrib[key] = self.bit_flip(elem.attrib[key])
                    print(elem.tag, elem.attrib)
        return ET.tostring(root).decode()
        
