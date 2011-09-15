import bloomfilter

FILE = "out"

def test1():
    bf = bloomfilter.BloomFilter()
    #
    start_cha = 0
    end_cha = 10000000
    #
    start_not = 10000001
    end_not = 20000000
    
    #insert 1 ~ 100w
    for i in xrange(start_cha, end_cha):
        bf.Add(str(i))
    print "Dump before."
    bf.Dump(FILE) 
    print "Dump done."

def test2():
    bf = bloomfilter.BloomFilter(FILE)
    #
    start_cha = 0
    end_cha = 10000000
    #
    start_not = 10000001
    end_not = 20000000
    
    #check for FN
    cnt = 0
    for i in xrange(start_cha, end_cha):
        if not bf.Test(str(i)):
            cnt += 1
    print "FN", cnt
    
    #check for FP
    cnt = 0
    for i in xrange(start_not, end_not):
        if bf.Test(str(i)):
            cnt += 1
    print "FP", cnt

if __name__ == "__main__":
	test1()
	test2()

