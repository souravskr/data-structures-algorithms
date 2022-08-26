# FIFO

class Queue:

    def __init__(self) -> None:

        self.queue = list()

    def enqueue(self, item):
        self.queue.append(item)

    def popleft(self):
        if len(self.queue) > 0:
            del(self.queue[0])
            return self.queue
        return None

    def __str__(self) -> str:
        return f"{self.queue}"


my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)

print(my_queue)

my_queue.popleft()

print(my_queue)
