import re


def extract_marks(script_string):
    pattern = r'\[[^\[\]]*\]'

    matches = re.findall(pattern, script_string)
    return matches

def extract_sgpa(data):
    pattern = r'\d+\.\d+'
    match = re.findall(pattern,data)
    return match
