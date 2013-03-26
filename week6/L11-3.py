def allStudents(self):
    if not self.isSorted:
        self.students.sort()
        self.isSorted = True
    for s in self.students:
        yield s

def genPrimes():
    x = 1
    primes = []
        
    while True:
        x += 1
        for p in primes:
            print x
            if x % p == 0:
                break
        else:
            primes.append(x)
            yield x
 
