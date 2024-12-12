# điều kiến tương tranh ( lỗi bug)
import dis
from threading import Thread,Lock
X = 0
lock = Lock()
def addTwo():
    global x
    while x < 10000000:
        lock.acquire()
        x += 2
        lock.release()

def addOne():
    global x
    while x < 10000000:
        lock.acquire()
        x += 1
        lock.release()


t1 = Thread(target=addOne)
t2 = Thread(target=addTwo)
print('Start.')
t1. start()
t2.start()

#dis.dis ('x+1 ')