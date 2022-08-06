from Fuzzer.MutationFuzzer import MutationFuzzer
from typing import Dict, Tuple, Union, List, Any
from random import randint
import json

class JsonFuzzer(MutationFuzzer):
    def init(self, seed: List[str], min_mutations: int = 2, max_mutations: int = 10) -> None:
        super().__init__(self, seed, min_mutations, max_mutations)
    
    def mutate(self, inp:str) -> str:




