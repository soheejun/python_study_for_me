# deque: can insert element in last and first (thread-safe biderectional queue)
#      : thread-safe: synchronized (can safely communication between threads)
#      : can limit maximum length
#      : if deque is full, maintain in latest automatically (remove the oldest)
# optimize for first / last insert and pop (not middle) 

from collections import deque
dq = deque(range(10), maxlen=10)
print(dq)

dq.rotate(3)
print(dq)

dq.appendleft(-1)
print(dq)

dq.append(11)
print(dq)

dq.extendleft([-2, -3])
print(dq)

dq.extend([12,13,14])
print(dq)


# vs queue
#: queue is also thread-safe
#: when the queue is full, block the insert operation and wait until other thread make space by remove some element --> can handle number of active thread 

# vs multiprocessing 
#: offer optimized queue object for support communication between multiple process 

# vs asyncio 
#: include in queue, multiprocessing module 
#: handle asynchronize proramming 

# vs heapq
#: does not implement queue object
#: can make immutable sequence to heapq or priority queue by using heappush(), heappop() 
