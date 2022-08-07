from Runner.Runner import Runner
import subprocess
from typing import Dict, Tuple, Union, List, Any

Outcome = str

class ProgramRunner(Runner):
    '''tests a program with inputs'''

    def __init__(self, program:Union[str, list[str]]) -> None: 
        '''intialize
        'program is a program spec passed to subprocess.run?'''
        self.program = program

    def run_process(self, inp: str = "") -> subprocess.CompletedProcess:
        '''Run the program with inp as input, return result of subprocess.run()'''
        return subprocess.run(  self.program, 
                                input=inp,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                universal_newlines=True)

    def run(self, inp: str = "") -> Tuple[subprocess.CompletedProcess, Outcome]:
        '''Run the program with inp as input 
        Return test outcome based on result of 'subprocess.run()'''
        result = self.run_process(inp)

        if result.returncode == 0:
            outcome = self.PASS
        elif result.returncode < 0: 
            outcome = self.FAIL
        else: 
            outcome = self.UNRESOLVED

        return (result, outcome)
