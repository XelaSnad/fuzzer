from Fuzzer.MutationFuzzer import MutationFuzzer
from typing import Dict, Tuple, Union, List, Any


class CsvFuzzer(MutationFuzzer):
    def init(self, seed: List[str], min_mutations: int = 2, max_mutations: int = 10) -> None:
        super().__init__(self, seed, min_mutations, max_mutations)

