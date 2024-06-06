import time 

start = time.time()

# Print current time
print(time.asctime())

now = time.gmtime()
print(now)

# number of second you want the programm to stop
time.sleep(3)

stop = time.time()

print(stop - start)
