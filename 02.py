#encoding:utf-8

#1 queue 队列（FIFO）

#导入queue模块的Queue类
from queue import Queue

#创建队列
q = Queue()

#向队列添加数据
q.put("test_queue_01")
q.put("test_queue_02")
q.put("test_queue_03")
q.put("test_queue_04")
q.put("test_queue_05")

#获取队列的值
print("队列的值：",q.get())

#获取队列的大小
print("获取队列的大小：",q.qsize())

#循环获取队列的值
for i in range(q.qsize()):
    print("循环打印队列值：",q.get())


#encoding:utf-8
#2 LifoQueue（LIFO）Last In First Out 后进先出

from queue import LifoQueue

#创建后进先出队列
lq = LifoQueue()

#向队列添加数据
lq.put("test_queue_01")
lq.put("test_queue_02")
lq.put("test_queue_03")
lq.put("test_queue_04")
lq.put("test_queue_05")

#获取队列的值
print("后进先出队列的值：",lq.get())

#获取队列的大小
print("获取队列的大小：",lq.qsize())

#循环获取队列的值
for i in range(lq.qsize()):
    print("循环打印后进先出队列值：",lq.get())


#encoding:utf-8
#3 PriorityQueue（优先级队列）

from queue import PriorityQueue

#创建优先级队列
pq = PriorityQueue()

#向队列添加数据,并打乱顺序
pq.put("test_queue_05",)
pq.put("test_queue_01")
pq.put("test_queue_04")
pq.put("test_queue_03")
pq.put("test_queue_02")


#获取队列的大小
print("获取队列的大小：",pq.qsize())

#循环获取队列的值
for i in range(pq.qsize()):
    print("循环打印优先级队列值：",pq.get())