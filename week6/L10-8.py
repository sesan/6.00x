class Queue(object):
    def __init__(self):
        self.vals = []

    def __str__(self):
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def __repr__(self):
        return str(self.vals.sort())
        
    def insert(self, n):
        if not n in self.vals:
            self.vals.append(n)
    
    def remove(self):
        if not self.vals == []:
            return self.vals.pop()
        else:
            raise ValueError()
