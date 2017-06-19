from multiprocessing import Pool
from multiprocessing import Process
import os
import sys
import urllib.request
sys.setrecursionlimit(2000)


# def f(x):
#     if x == 1 or x == 0:
#         return 1
#     else:
#         return x * f(x - 1)
#
# name = "Siddharth"
# age  = 33
#
# print("{0}, {1} is presently writing python code".format(name, age))
# print("{0:_^6}".format("ola"))
# print("{0:.3f}".format(1/3))
def trigger10ktimes():
    while True:
        with urllib.request.urlopen('http://NodeECS92-EcsElb-1L6MD2ZWJI59I-1840691753.ap-southeast-1.elb.amazonaws.com') as response:
            html = response.read()
            print("{}-{}".format(os.getpid(), html))

processes = []
for i in range(10):
    new_process = Process(target=trigger10ktimes)
    processes.append(new_process)
    new_process.start()
    print("Launched: {}", new_process.pid)

for process in processes:
    process.join()


