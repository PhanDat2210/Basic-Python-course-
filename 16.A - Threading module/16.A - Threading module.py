#Đa luồng -Multi-thread

def hello():
    for i in range(0,10):print("Hello",i)
def hi():
    for i in range(0,22):print("Hi",i)
import threading
x = threading.Thread(target = hello)
y = threading.Thread(target = hi)
x.start() 
y.start()
for i in range(0,6):print("World",i)
x.join()
y.join()
  
#single thread
print('Finish')