from Fuzzer.Fuzzer import Fuzzer
from typing import Dict, Tuple, Union, List, Any
from random import *


class MutationFuzzer(Fuzzer):
    def __init__(self, seed: List[str],
                min_mutations: int = 2,
                max_mutations: int = 10) -> None:
        '''
        Constructor 
        seed - a list of input strings to mutate
        min_mutations - the minimum number of mutations to apply
        max_mutations - the maximum number of mutations to apply
        '''
        self.seed = seed
        self.min_mutations = min_mutations
        self.max_mutations = max_mutations
        self.reset()

    def reset(self) -> None:
        '''Set population to intial seed
        to be overloaded in subclasses'''
        self.population = self.seed
        self.seed_index = 0

    def byte_flip(self, inp: str) -> str:
        bytes_obj = inp.encode('ISO-8859-1')
        index_len = len(bytes_obj) - 1
        index = randint(0, index_len)
        bytes_obj = list(bytes_obj)
        bytes_obj[index] = bytes_obj[index] ^ 0xff
        bytes_obj = bytes(bytes_obj)
        return bytes_obj.decode('ISO-8859-1')

    def bit_flip(self, inp: str) -> str:
        bytes_obj = inp.encode('ISO-8859-1')
        index_len = len(bytes_obj) - 1
        index = randint(0, index_len)
        byte = bytes_obj[index]
        randbitindex = randint(0, 7)
        byte = format(byte, '08b')
        byte = list(byte)

        if byte[randbitindex] == '0':
            byte[randbitindex] = 1
        else:
            byte[randbitindex] = 0
        
        byte = int("".join(str(x) for x in byte), 2)
        
        bytes_obj = list(bytes_obj)
        bytes_obj[index] = byte
        bytes_obj = bytes(bytes_obj)

        return bytes_obj.decode('ISO-8859-1')

class MutationFuzzer(MutationFuzzer):
    def mutate(self, inp:str) -> str:
        return self.byte_flip(inp)

class MutationFuzzer(MutationFuzzer):
    def create_candidate(self) -> str:
        """Create a new candidate by mutating a population member"""
        candidate = choice(self.population)
        trials = randint(self.min_mutations, self.max_mutations)
        for i in range(trials):
            candidate = self.mutate(candidate)
        return candidate

class MutationFuzzer(MutationFuzzer):
    def fuzz(self) -> str:
        if self.seed_index < len(self.seed):
            # Still seeding
            self.inp = self.seed[self.seed_index]
            self.seed_index += 1
        else:
            # Mutating
            self.inp = self.create_candidate()
        return self.inp
