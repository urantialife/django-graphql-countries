import re


def dashed_to_camel(dashed_data, regex=re.compile(r'(?!^)_([a-zA-Z])')):
    data = {}
    for key, value in dashed_data.items():
        if isinstance(value, dict):
            value = dashed_to_camel(value)
        data[regex.sub(lambda match: match.group(1).upper(), key)] = value
    return data
