import time
import random
import sys

arguments = sys.argv[1]
# We print 10 random numbers, sleeping for one second between every print
for i in range(0, 50):
    time.sleep(3)
    print(f'Hello World {random.randint(0, 50)} {arguments}')