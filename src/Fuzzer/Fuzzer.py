from Runner.Runner import Runner
from typing import Dict, Tuple, Union, List, Any
import subprocess
from Runner.PrintRunner import PrintRunner


Outcome = str
inputs = str
class Fuzzer:
    ''' This is going to be our basecase for the fuzzer '''

    def __init__(self) -> None:
        '''Constructor'''
        pass
    
    def fuzz(self) -> str:
        '''Returns our fuzzy input'''
        return ""

    def run(self,rule: str, runner: Runner = Runner()) \
            -> Tuple[subprocess.CompletedProcess,inputs,Outcome]:
        ''' Runs a runner using our fuzzy input '''
        self.setCurrentRule(rule)
        return runner.run(self.fuzz())
    def runs(self, rule: str, runner: Runner = PrintRunner(), trials: int = 10) \
            -> List[Tuple[subprocess.CompletedProcess,inputs,Outcome]]:
        '''Runs runner with the fuzzy input for as many trials there are times'''
        return [self.run(rule, runner) for i in range(trials)]
    

    def getRule(self):
        return self.rules

    def setCurrentRule(self, rule: str):
        self.currentRule = rule

    def getCurrentRule(self) -> str:
        return self.currentRule
