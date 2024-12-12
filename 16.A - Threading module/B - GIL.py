#Đa luồng -Multi-thread
# concurency : sự đồng thời
#Parallelism / simultanously: song song
def hello():
    for i in range(0,2000000):pass

import threading
import time
x = threading.Thread(target = hello)
start = time.time()
print('Start')
x.start() 

for i in range(0,1000000):pass
x.join()

  
#single thread
print('Finish')
end = time.time()

print('Time elapsed:',end - start)