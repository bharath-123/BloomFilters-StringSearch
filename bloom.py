'''
    Bloom filter class
'''

import math
from bitarray import bitarray
import mmh3

class Bloom() :

    def __init__(self,entries,error) :
        self.ready = 0
        if error == 0 :
            print("Error of 0 is not possible\n")
            return -1
        self.entries = entries
        self.no_of_elements = 0
        self.error = error
        self.num = math.log(self.error)
        self.denom = 0.4804530139
        self.bpe = -(self.num/self.denom)

        self.bits = int(self.entries*self.bpe)

        self.hashes = int(0.693147180*self.bpe)

        self.bf = bitarray(self.bits)
        self.bf.setall(0)

        self.ready = 1

    def bloom_print(self) :
        if self.ready == 0 :
            print("Bloom filter is not created properly\n")
            return 0
        else :
            print("The number of hashes are {}\n".format(self.hashes))
            print("The number of bits per element are {}\n".format(self.bpe))
            print("The error rate is {}\n".format(self.error))
            print("The size of the bitarray is {}\n".format(self.bits))
            return 1

    def bloom_add(self,buffer) :
        if self.ready == 0  :
            print("Bloom filter was not created properly\n")
            return 1
        else :
            if self.no_of_elements < self.entries :
                a = mmh3.hash64(buffer)[0]
                b = mmh3.hash64(buffer)[1]
                for i in range(self.hashes) :
                    x = (a + i*b) % (self.bits)
                    self.bf[x] = 1
                    self.no_of_elements += 1
            else :
                print("Bloom filter capacity crossed\n")
                return -1
            return 0

    def bloom_check(self,buffer):
        if self.ready == 0 :
            print("Bloom filter was not created properly\n")
        else :
            hits = 0
            a = mmh3.hash64(buffer)[0]
            b = mmh3.hash64(buffer)[1]
            for i in range(self.hashes) :
                x = (a + i*b) % (self.bits)
                if self.bf[x] == 1 :
                    hits += 1
            if hits == self.hashes :
                return 1 # might be there
            else :
                return 0 # not there for sure
