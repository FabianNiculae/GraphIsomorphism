
from math import floor
from math import sqrt

def PrimesTo(n):
    isComposite = [False] * n
    primes = []

    for i in range(2, n+2):
        k = i-2
        if not isComposite[k]:
            primes.append(i)
            while k < n:
                isComposite[k] = True
                k += i
    
    return primes

def StackArray(size):
    arr = list()
    while len(arr) < size:
        arr.append(list())
    return arr


class RollingSieve:
    '''
    This rolling sieve algorithm is an incremental sieve to compute primes
    iteratively. It uses an circular array of stacks to store primes
    which can be used to efficiently compute the next prime.

    This algorithm is designed by J. P. Sorenson and it is fully described
    in his paper 'Two Compact Incremental Prime Sieves'. The paper can be
    found via this link: https://arxiv.org/pdf/1503.02592.pdf.

    The time complexity for calculating the next prime is O[log(n) / log(log(n))]
    and its spacial complexity is O[n^1/2 log(n)]. The calculations for these
    complexities can also be found in the abovementioned paper.
    '''
    def __init__(self):
        self.__n = 2
        self.__pos = 0
        self.__r = 2
        self.__s = self.__r * self.__r
        self.__delta = self.__r + 2
        self.__T = StackArray(self.__delta)
        self.__T[0].append(2)
    
    def __next(self):
        isPrime = True
        while len(self.__T[self.__pos]) > 0:
            p = self.__T[self.__pos].pop()
            self.__T[(self.__pos+p)%self.__delta].append(p)
            isPrime = False
        
        if self.__n == self.__s:
            if isPrime:
                self.__T[(self.__pos+self.__r)%self.__delta].append(self.__r)
                isPrime = False
            self.__r += 1
            self.__s = self.__r * self.__r
        
        self.__n += 1
        self.__pos = (self.__pos+1)%self.__delta

        if self.__pos == 0:
            self.__delta += 2
            self.__T.append(list())
            self.__T.append(list())

        return isPrime
    
    def Next(self):
        while not self.__next():
            pass
        return self.__n - 1

if __name__ == "__main__":

    primeGenerator = RollingSieve()

    for i in range(100):
        print(primeGenerator.Next())
