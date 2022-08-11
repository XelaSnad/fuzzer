from Fuzzer.MutationFuzzer import MutationFuzzer
from typing import Dict, Tuple, Union, List, Any
import xml.etree.ElementTree as ET
import random

BAD_DOM_1 = '''<div class="bad_dom1" id="nice"><a class="bad_dom1" href="http://google.com">Look at goole</a><link class="bad_dom1" href="http://nomoremrwww.com"/><span class = "bad_dom1">catch me if you can</span></div>'''

    #The tags have a format string
BAD_DOM_2 = '''<fs class="bad_dom2">%s</fs>'''

    # Just a span
BAD_DOM_3 = '''<span class="bad_dom3" id="no">stick em up codger</span>'''

BAD_DOM_4 = '''<div class = "bad_dom4" id="lol" date="lol" user="lol" data="lol" name="lol" dob="lol"></div>'''
    # Just Weird
BAD_DOM_5 = '''<weird class="nad_dom5" id="weird">weird</weird>'''


class XmlFuzzer(MutationFuzzer):
    
    def init(self, seed: List[str], rules: List[str],  min_mutations: int = 2, max_mutations: int = 10) -> None:
        super().__init__(self, seed, rules, min_mutations, max_mutations)

    def mutate(self, inp: str)->str: 
        root = ET.fromstring(inp)
        



        
        attributes = []
        texts = []

        for idx, node in enumerate(root.iter()):          

            if bool(node.attrib): 
                attributes.append(idx)
            
            if node.text != None:
                if not node.text.isspace():
                    texts.append(idx)
            

        match self.getCurrentRule():
            case "overflow":
                root = self.handleMutate(root, attributes, texts, "A"*10000)
            case "negative":
                root = self.handleMutate(root, attributes, texts, "-1")
            case "positive":
                root = self.handleMutate(root, attributes, texts, "1")
            case "zero":
                root = self.handleMutate(root, attributes, texts, "0")
            case "large_positive":
                root = self.handleMutate(root, attributes, texts, f"{10**55}")
            case "large_negative":
                root = self.handleMutate(root, attributes, texts, f"{-10**55}")
            case "format":
                root = self.handleMutate(root, attributes, texts, "%x%n")
            case "bad_url":
                root = self.handleMutate(root, attributes, texts, "https://idontaccesstheworldwideweb.com")
            case "nothing":
                root = self.handleMutate(root, attributes, texts, "")
            case "dom1":
                node = ET.fromstring(BAD_DOM_1)
                root.append(node)
            case "dom2": 
                node = ET.fromstring(BAD_DOM_2)
                root.append(node)
            case "dom3":
                node = ET.fromstring(BAD_DOM_3)
                root.append(node)
            case "dom4":
                node = ET.fromstring(BAD_DOM_4)
                root.append(node)
            case "dom5":
                node = ET.fromstring(BAD_DOM_5)
                root.append(node)
    
        
        string = ET.tostring(root).decode()
        print(string)
        return string
        '''

        text, attribute = (random.choice(texts), random.choice(attributes))

        for idx, node in enumerate(root.iter()):
            
            if idx == text:
                node.text = "%x%n" + self.repeated_parts(node.text)
                print(node.text)

            if idx == attribute:
                for key in node.attrib:
                    node.attrib[key] = "%x%n" + self.repeated_parts(node.attrib[key])
                    
    '''

    def handleMutate(self, root, attributes, text, payload):
        for idx, node in enumerate(root.iter()):
            if idx in text:
                node.text = payload
            if idx in attributes:
                for key in node.attrib:
                    node.attrib[key] = payload
                    
        
        return root

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
