from Fuzzer.MutationFuzzer import MutationFuzzer
from typing import Dict, Tuple, Union, List, Any


class JpgFuzzer(MutationFuzzer):
    def init(self, seed: List[str],rules:List[str],  min_mutations: int = 2, max_mutations: int = 10) -> None:
        super().__init__(self, seed, rules, min_mutations, max_mutations)

