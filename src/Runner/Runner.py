Outcome = str
from typing import Dict, Tuple, Union, List, Any

class Runner:
    '''Base Class for testing inputs'''

    # These will be the outcomes of our test

    PASS = "PASS"
    FAIL = "FAIL"
    UNRESOLVED = "UNRESOLVED"

    def __init__(self) -> None:
        '''initalize'''
        pass

    def run(self, inp:str) -> Any:
        '''Run the runner with given input'''
        return(inp, Runner.UNRESOLVED)
