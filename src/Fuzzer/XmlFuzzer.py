from Fuzzer.MutationFuzzer import MutationFuzzer
from typing import Dict, Tuple, Union, List, Any
import xml.etree.ElementTree as ET
import random

class XmlFuzzer(MutationFuzzer):
    rules = ["overflow", "negative", "postive", "zero", "large_positive, large_negative", "format", "bad_url", "nothing", "dom1", "dom2", "dom3", "dom4", "dom5"]

    def init(self, seed: List[str], rules: List[str],  min_mutations: int = 2, max_mutations: int = 10) -> None:
        super().__init__(self, seed, rules, min_mutations, max_mutations)

    def mutate(self, inp: str)->str: 
        root = ET.fromstring(inp)
        print("---")
        
        attributes = []
        texts = []

        for idx, node in enumerate(root.iter()):          

            if bool(node.attrib): 
                attributes.append(idx)
            
            if node.text != None:
                if not node.text.isspace():
                    texts.append(idx)

        text, attribute = (random.choice(texts), random.choice(attributes))

        for idx, node in enumerate(root.iter()):
            
            if idx == text:
                node.text = "%x%n" + self.repeated_parts(node.text)
                print(node.text)

            if idx == attribute:
                for key in node.attrib:
                    node.attrib[key] = "%x%n" + self.repeated_parts(node.attrib[key])
                    
                       

        string = ET.tostring(root).decode("ascii")
        return string



if __name__ == "__main__":
    data = '''<html>
    <head>
        <link href="http://somewebsite.com" />
    </head>
    <body>
        <h1>I'm not a web developer.</h1>
    </body>

    <div id="#lol">
        <a href="http://google.com">Here is some link...</a>
    </div>


    <tail>
        <a href="http://bing.com">Footer link</a>
    </tail>
</html>'''#data from xml1.txt

    fuzzer = XmlFuzzer()
    fuzzer.mutate(data)
