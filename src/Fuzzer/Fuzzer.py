from Runner.Runner import Runner
from typing import Dict, Tuple, Union, List, Any
import subprocess
from Runner.PrintRunner import PrintRunner


Outcome = str

class Fuzzer:
    ''' This is going to be our basecase for the fuzzer '''

    def __init__(self) -> None:
        '''Constructor'''
        pass
    
    def fuzz(self) -> str:
        '''Returns our fuzzy input'''
        return ""

    def run(self, runner: Runner = Runner()) \
            -> Tuple[subprocess.CompletedProcess, Outcome]:
        ''' Runs a runner using our fuzzy input '''
        return runner.run(self.fuzz())
    def runs(self, runner: Runner = PrintRunner(), trials: int = 10) \
            -> List[Tuple[subprocess.CompletedProcess, Outcome]]:
        '''Runs runner with the fuzzy input for as many trials there are times'''
        return [self.run(runner) for i in range(trials)]
