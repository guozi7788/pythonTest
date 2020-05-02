#coding:UTF-8
import time
def consumer(name):
    print("%s is ready to study!"%name)
    
    while True:
        lesson = yield    #一次返回一个结果
        print("lesson = [%s],[%s] study!"%(lesson, name))
def producer():
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print(r"start learning!")
    
    for i in range(10):
        time.sleep(1)
        print(r"two Students is arrived")
        c.send(i)
        c2.send(i)

producer()