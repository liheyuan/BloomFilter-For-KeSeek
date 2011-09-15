'''
Created on 2011-8-19

@author: liheyuan
'''

from xmlrpclib import ServerProxy
from multiprocessing import Process
import sys

def test():
    proxy = ServerProxy("http://localhost:8080")
    #for i in xrange(100):
    proxy.contains("http://kclab.ibcas.ac.cn/lunwen/关于国际植物生物技术联合会统计会员的通知.doc")

if __name__ == "__main__":
    proxy = ServerProxy("http://localhost:8080")
    proxy.contains("http://www.cjxb.ac.cn/../qikan/public/pdfdow.asp?xiazailx=Ãâ·Ñ&bsid=15128&ag=0&gaohao=1000ª²0550£¨2011£©04ª²0798ª²11ª¤&houzhui=.htm")
    sys.exit()
    procs = []
    for i in xrange(1):
        p = Process(target=test)
        p.start()
        procs.append(p)
    for proc in procs:
        proc.join()
