# 1 queue 队列（FIFO）
FIFO 全称是First Input First Output（先进先出），先进先出简言之就是在获取队列的数据时，优先取队列前面的数据。

Queue模块中的常用方法:

Queue.qsize() 返回队列的大小

Queue.empty() 如果队列为空，返回True,反之False

Queue.full() 如果队列满了，返回True,反之False

Queue.full 与 maxsize 大小对应

Queue.get([block[, timeout]])获取队列，timeout等待时间

Queue.get_nowait() 相当Queue.get(False)

Queue.put(item, block=True, timeout=None) 写入队列，timeout等待时间

Queue.put_nowait(item) 相当 Queue.put(item, False)

Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号

Queue.join() 实际上意味着等到队列为空，再执行别的操作

# 2 LifoQueue（LIFO）
Last In First Out 后进先出

# 3 PriorityQueue（优先级队列）
数据越小优先级越高，也就是数据越小优先获取到
