from Fuzzer.MutationFuzzer import MutationFuzzer
from typing import Dict, Tuple, Union, List, Any
import random

class PlaintextFuzzer(MutationFuzzer):
    def init(self, seed: List[str], rules: List[str], min_mutations: int = 2, max_mutations: int = 10) -> None:
        super().__init__(self, seed, rules,  min_mutations, max_mutations)
    
    def mutate(self, inp:str) -> str:
        match self.getCurrentRule():
            case "nothing":
                return ""
            case "newline":
                return inp+"\n"*random.randint(0, 30)
            case "zero":
                return "0"
            case "positive":
                return "1"
            case "negative":
                return "-1"
            case "large_positive":
                return f"{10**55}"
            case "large_negative":
                return f"{-10**55}"
            case "null_terminator":
                return "\0"
            case "format": 
                return "%x%n"
