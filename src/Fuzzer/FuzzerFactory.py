from Fuzzer.JpgFuzzer import JpgFuzzer
from Fuzzer.JsonFuzzer import JsonFuzzer
from Fuzzer.XmlFuzzer import XmlFuzzer
from Fuzzer.CsvFuzzer import CsvFuzzer
from Fuzzer.PlaintextFuzzer import PlaintextFuzzer

class FuzzerFactory:
    def get_fuzzer(self, input_type, input):
        if input_type == 'jpg':
            return JpgFuzzer(input)
        elif input_type == 'json':
            return JsonFuzzer(input)
        elif input_type == 'xml':
            return XmlFuzzer(input)
        elif input_type == 'csv':
            return CsvFuzzer(input)
        else:
            return PlaintextFuzzer(input) 
        

