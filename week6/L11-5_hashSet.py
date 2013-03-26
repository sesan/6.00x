class hashSet(object):
    """A hashSet is a hashed set of integers"""
    
    def __init__(self, numBuckets):
        '''
        numBuckets: int. (# of buckets for hash set)
        Raises ValueError if numBuckets not int > zero.

        Sets up an empty hash set with numBuckets # of buckets
        '''
        self.vals = {}
        if self.isInt(numBuckets) and numBuckets > 0:
            self.numBuckets = numBuckets
        else:
            raise ValueError(str(numBuckets) + ' must be an integer > 0')
        for i in range(numBuckets):
            self.vals[i] = []

    def isInt(self, n):
        if type(n) != int:
            raise ValueError(str(n) + ' must be an integer')
        else:
            return True

    def hashValue(self, e):
        '''
        e: an int

        returns: a hash value for e, ie.e % numBuckets
        raises ValueError is e not int
        '''
        if self.isInt(e):
            return e % self.getNumBuckets()
            
    def getNumBuckets(self):
        '''
        returns the number of buckets
        '''
        return self.numBuckets
    
    def insert(self, n):
        '''
        insert an int. (n) or raise ValueError if n not int type
        '''
        return self.vals[self.hashValue(n)].append(n)

    def remove(self, n):
        '''
        n: integer value to remove from the set
        Raises ValueError via self.isInt() if not int type
        '''
        return self.vals[self.hashValue(n)].remove(n)
        
    def member(self, n):
        '''
        n: an integer
        Checks if n is contained in the hash set
        Raises ValueError via self.isInt() is not int type
        '''
        return self.vals[self.hashValue(n)].count(n) > 0

    def __str__(self):
        return str(self.vals)

    def __repr__(self):
        return 'hashSet(' + str(self.numBuckets) + ')'
