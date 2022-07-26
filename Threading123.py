'''from threading import Thread
import time
class Hello(Thread):
    def run(self):
        for i in range(10):
            print('HELLO')

class Hi(Thread):
    def run(self):
        for i in range(10):
            print('HI')
start = time.time()
#Hello().run()
#Hi().run()
t1=Hello()
t2=Hi()
t1.start()
t2.start()
t1.join()
t2.join()

end=time.time()
print(end-start)'''

'''t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))'''

'''import sys
l=[]
l1=l
l2=[]
l3=l2
l4=l3
print(sys.getrefcount(l),sys.getrefcount(l1),sys.getrefcount([]))'''

'''from multiprocessing import Pool
from threading import Thread
import time

COUNT = 50000000
def countdown(n):
    while n>0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(countdown, [COUNT//2])
    r2 = pool.apply_async(countdown, [COUNT//2])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds -', end - start)
    start=time.time()
    t1=Thread(target=countdown,args=(COUNT//2,))
    t2=Thread(target=countdown,args=(COUNT//2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end=time.time()
    print(end-start)
    start=time.time()
    countdown(COUNT)
    end=time.time()
    print(end-start)'''


from multiprocessing import Process
from threading import Thread
# Code snippet for Part 5
import time
def cpu_bound(n):
    while n>0:
        n-=1
if __name__ == '__main__':
    COUNT=500000
    p1 = Process(target = cpu_bound, args =(COUNT//2, ))
    p2 = Process(target = cpu_bound, args =(COUNT//2, ))
    
    start=time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end=time.time()
    print(end-start)
    
    t1 = Thread(target = cpu_bound, args =(COUNT//2, ))
    t2 = Thread(target = cpu_bound, args =(COUNT//2, ))
    start=time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end=time.time()
    print(end-start)

    start=time.time()
    cpu_bound(COUNT)
    end=time.time()
    print(end-start)