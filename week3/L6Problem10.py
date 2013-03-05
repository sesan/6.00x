def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    return sum(len(v) for v in aDict.values())

# list comprehensions deserve more study.
