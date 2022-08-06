class BinaryProgramRunner(ProgramRunner):
    def run_process(self, inp: str= "") -> subprocess.CompletedProcess:
        ''' runs the program with 'inp as input return result of subprocess.run() '''
        return subprocess.run(  self.program,
                                input=inp.encode(),
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
