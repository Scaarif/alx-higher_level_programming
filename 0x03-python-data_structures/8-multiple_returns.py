#!/usr/bin/python3
def multiple_returns(sentence):
    """ Returns a tuple with the length f a string and its
    first character
    Args:
        sentence: the string
    """
    return len(sentence), sentence[0] if len(sentence) > 0 else None
