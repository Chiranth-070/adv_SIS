import re


def extract_marks(script_string):
    pattern = r'\[[^\[\]]*\]'

    matches = re.findall(pattern, script_string)
    return matches
