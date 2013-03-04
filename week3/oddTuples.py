def oddTuples(aTup):
    tups = (aTup[0],)
    for tup in range(len(aTup)):
        tups += aTup[tup]
    print(tups)

oddTuples(('I', 'am', 'a', 'test', 'tuple'))
