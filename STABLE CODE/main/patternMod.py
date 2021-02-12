try:
    import re2 as re
except ImportError:
    import re

def find_pattern(pattern_to_search_for, data):
    '''
    pattern_to_search_for = pattern match (must be r'str') 
    data = find pattern in data
    '''
    pattern = re.compile(pattern_to_search_for)
    pattern_matches = pattern.finditer(data)
    initial_match = [match for match in pattern_matches]
    return initial_match[0].group(0)