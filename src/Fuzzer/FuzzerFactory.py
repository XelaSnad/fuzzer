from Fuzzer.JpgFuzzer import JpgFuzzer
from Fuzzer.JsonFuzzer import JsonFuzzer
from Fuzzer.XmlFuzzer import XmlFuzzer
from Fuzzer.CsvFuzzer import CsvFuzzer
from Fuzzer.PlaintextFuzzer import PlaintextFuzzer

class FuzzerFactory:
    def get_fuzzer(self, input_type, input, min_mutation, max_mutation):
        if input_type == 'jpg':
            return JpgFuzzer(input, min_mutation, max_mutation)
        elif input_type == 'json':
            return JsonFuzzer(input, min_mutation, max_mutation)
        elif input_type == 'xml':
            return XmlFuzzer(input, min_mutation, max_mutation)
        elif input_type == 'csv':
            return CsvFuzzer(input, min_mutation, max_mutation)
        else:
            return PlaintextFuzzer(input, min_mutation, max_mutation) 
        

