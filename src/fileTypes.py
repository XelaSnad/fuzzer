import csv
import json
from PIL import Image
import imghdr
import io
import xml.etree.ElementTree as elementTree

def findInputType(input):

    bytes = input.encode("ISO-8859-1")
    inputType = ""

    if validateJpg(bytes):
        inputType = "jpg"
    elif validateJSON(input):
        inputType = "json"
    elif validateXml(input):
        inputType = "xml"
    elif validateCSV(input):
        inputType = "csv"
    elif input == "":
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

'''
The split [1] is not "" means that the second line is not empty. Essentially saying is the file just one string.
'''

def validateCSV(string):
    lines = string.split("\n")
    if len(lines) > 1 and lines[1] != "":
        try:
            dialect = csv.Sniffer().sniff(lines[1])
        except csv.Error:
            return False
        return True
    return False

def validateJpg(string):
    

    try: 
       img = Image.open(io.BytesIO(string))
    except IOError:
        return False
    return True
    ''' try:
        img = imghdr.what(string)
    except OSError:
        return False
    if img is ('jpeg' or 'jpg'):
        return True
    return False
    '''
def validateXml(string): 
    try:
        elementTree.fromstring(string)
    except elementTree.ParseError:
        return False 
    return True 

# ========================= Todo ===========================
# - Add Elf and PDF file types 
# - Get Jpeg Working