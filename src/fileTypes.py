import csv
import json
from PIL import Image
import imghdr
import xml.etree.ElementTree as elementTree

def validateJSON(string): 
    try:
        json.loads(string)
    except ValueError as err:
        return False
    return True

def validateCSV(string):
    if len(string.split("\n")) > 1:
        try:
            dialect = csv.Sniffer().sniff(string)
        except csv.Error:
            return False
        return True
    return False

def validateJpg(string):
    try:
        img = imghdr.what(string)
    except OSError:
        return False
    if img is ('jpeg' or 'jpg'):
        return True
    return False

def validateXml(string): 
    try:
        elementTree.fromstring(string)
    except elementTree.ParseError:
        return False 
    return True 

# ========================= Todo ===========================
# - Add Elf and PDF file types 
# - Get Jpeg Working