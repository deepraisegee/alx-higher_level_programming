#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        max_val = max(a_dictionary.values())
        for k in a_dictionary:
            if a_dictionary[k] == max_val:
                return k
        return None
    return None
