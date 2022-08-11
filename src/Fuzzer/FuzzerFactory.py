from Fuzzer.JpgFuzzer import JpgFuzzer
from Fuzzer.JsonFuzzer import JsonFuzzer
from Fuzzer.XmlFuzzer import XmlFuzzer
from Fuzzer.CsvFuzzer import CsvFuzzer
from Fuzzer.PlaintextFuzzer import PlaintextFuzzer

JPG_RULES = []
PLAINTEXT_RULES = ["nothing", "newline", "zero", "positive", "negative", "large_positive", "large_negative", "null_terminator", "format"]
JSON_RULES = ["overflow", "zero", "positive", "negative", "large_positive", "large_negative", "format"]
CSV_RULES = ["overflow_rows", "overflow_values", "zero", "positive", "negative", "large_positive", "large_negative", "null_terminator", "format"]
XML_RULES = ["overflow", "negative", "postive", "zero", "large_positive, large_negative", "format", "bad_url", "nothing", "dom1", "dom2", "dom3", "dom4", "dom5"]


class FuzzerFactory:
    def get_fuzzer(self, input_type, input, min_mutation, max_mutation):
        if input_type == 'jpg':
            return JpgFuzzer(input, JPG_RULES, min_mutation, max_mutation)
        elif input_type == 'json':
            return JsonFuzzer(input, JSON_RULES, min_mutation, max_mutation)
        elif input_type == 'xml':
            return XmlFuzzer(input, XML_RULES, min_mutation, max_mutation)
        elif input_type == 'csv':
            return CsvFuzzer(input, CSV_RULES, min_mutation, max_mutation)
        else:
            return PlaintextFuzzer(input, PLAINTEXT_RULES, min_mutation, max_mutation) 
        

