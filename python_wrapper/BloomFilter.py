#-*- encoding: utf8 -*- #
'''
Created on 2011-8-17

@author: liheyuan
'''

from util import BitVector, mmh3
import sys, os.path

#DEFAULT PARAM
M = 20000000 * 8
K = 3

class BloomFilter():
    
    #Init functions
    def __init__(self, file=None, m=M, k=K):
        #init bit vector, all zero
        self.m = m
        self.k = k
        self.dump_proc = None
        #Load Bit Victor if file exists
        if file and os.path.isfile(file):
#            bv = BitVector.BitVector(filename=file)
#            self.bv = bv.read_bits_from_file(M)
#            bv.close_file_object()
#            del bv
            pass
        else:
            self.bv = BitVector.BitVector(size=M)
        
    #using mmh3 hash function to generate k hash functions and its hash vals
    def _hashs(self, key):
        ret = []
        seed = 0
        for i in xrange(self.k):
            seed = mmh3.hash(key, seed)
            ret.append(abs(seed % self.m))
        return ret
    
    #return the bit vector, just for debug
    def __str__(self):
        return self.bv.__str__()
    
    #reset the bit vector to all zero
    def reset(self):
        self.bv.reset(0)
        
    #count the number of 1s in bit vector
    def countOne(self):
        return self.bv.count_bits()
    
    #add elem to Bloom Filter
    def add(self, key):
        for val in self._hashs(key):
            self.bv[val] = 1
    
    #test on bloom filter
    def contains(self, key):
        for val in self._hashs(key):
            if self.bv[val] == 0:
                return False
        return True
    
    #If url in BF,return True, else add it to BF and return False
    def contains_add(self, key):
        if self.contains(key):
            return True
        else:
            self.add(key)
            return False
    def test(self, key):
        return True
        
if __name__ == "__main__":
    bf = BloomFilter()
    #
    start_cha = 0
    end_cha = 1000000
    #
    start_not = 1000001
    end_not = 2000000
    
    #insert 1 ~ 100w
    for i in xrange(start_cha, end_cha):
        bf.add(str(i))
    
    #check for FN
    cnt = 0
    for i in xrange(start_cha, end_cha):
        if not bf.contains(str(i)):
            cnt += 1
    print "FN", cnt
    
    #check for FP
    cnt = 0
    for i in xrange(start_not, end_not):
        if bf.contains(str(i)):
            cnt += 1
    print "FP", cnt
