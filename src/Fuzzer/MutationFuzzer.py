from Fuzzer.Fuzzer import Fuzzer
from typing import Dict, Tuple, Union, List, Any

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

class MutationFuzzer(MutationFuzzer):
    def mutate(sel, inp:str) -> str:
        return mutate(inp)

class MutationFuzzer(MutationFuzzer):
    def create_candidate(self) -> str:
        """Create a new candidate by mutating a population member"""
        candidate = random.choice(self.population)
        trials = random.randint(self.min_mutations, self.max_mutations)
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
