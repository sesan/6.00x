def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if aDict == {}:
        return None
    else:
        return "".join([k for k,v in aDict.iteritems() if len(v) == max([len(e) for e in aDict.values()])])

    # There's gotta be a better way to do this...
