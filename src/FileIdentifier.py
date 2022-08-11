import csv
import json
from PIL import Image
import imghdr
import io
import xml.etree.ElementTree as elementTree

class FileIdentifier:
    def __init__(self, input: str) -> None:
        '''Initialises
        'file is the file we are checking its type'''
        self.input = input

    def identify_type(self) -> str:
        '''determines what type of file we are looking at'''

        bytes = self.input.encode("ISO-8859-1")
        inputType = ""

        if validateJpg(bytes):
            inputType = "jpg"
        elif validateJSON(self.input):
            inputType = "json"
        elif validateXml(self.input):
            inputType = "xml"
        elif validateCSV(self.input):
            inputType = "csv"
        elif self.input == "":
            inputType = "empty"
        else:
            inputType = "plaintext"

        return inputType

def validateJSON(string):
    try:
        json.loads(string)
    except ValueError as err:
        return False
    return True

def validateXml(string):
    try:
        elementTree.fromstring(string)
    except elementTree.ParseError:
        return False
    return True
    
 

def validateJpg(string):
    try:
       img = Image.open(io.BytesIO(string))
    except IOError:
        return False
    return True

def validateCSV(string):
    lines = string.split("\n")
    if len(lines) > 1 and lines[1] != "":
        try:
            dialect = csv.Sniffer().sniff(lines[1])
        except csv.Error:
            return False
        if "," in string:
            return True
        else:
            return False



