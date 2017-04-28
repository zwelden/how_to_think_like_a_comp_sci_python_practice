import time

class Queue:

    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def __str__(self):
        string = "["
        head = self.head
        while head is not None:
            if head.next is None:
                string += str(head)
            else:
                string += str(head) + ", "
            head = head.next
        string += "]"
        return string

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            self.head = node
            self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo

class ListQueue:

    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def insert(self, cargo):
        self.queue.append(cargo)

    def remove(self):
        item = None
        if self.queue:
            item = self.queue[0]
            del self.queue[0]
        return item

class PriorityQueue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item

class LinkedPriorityQueue:

    def __init__(self):
        self.length = 0
        self.head = None

    def __str__(self):
        string = "["
        head = self.head
        while head is not None:
            if head.next is None:
                string += str(head)
            else:
                string += str(head) + ", "
            head = head.next
        string += "]"
        return string

    def insert(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = None
        elif node.cargo >= self.head.cargo:
            node.next = self.head
            self.head = node
        else:
            current = self.head.next
            prior = self.head
            while current is not None:
                if node.cargo < current.cargo:
                    prior = current
                    current = current.next
                elif node.cargo >= current.cargo:
                    break

            prior.next = node
            node.next = current
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo

    def is_empty(self):
        return self.length == 0


class Node:

    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return (str(self.cargo))


class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return "{0:16}:  {1}".format(self.name, self.score)

    def __gt__(self, other):
        return self.score < other.score


# Testing run times for 4 queue types
# 100,000 runs each
# except priority queue --> only 10,000 runs, cuz... it slow

q = Queue()
lq = ListQueue()

time1 = time.time()
for i in range(100000):
    q.insert(i)
for i in range(100000):
    q.remove()
time2 = time.time()

print("{0:19}  :  {1}".format("Queue", time2-time1))

time1 = time.time()
for i in range(100000):
    lq.insert(i)
for i in range(100000):
    lq.remove()
time2 = time.time()
print("{0:19}  :  {1}".format("ListQueue", time2-time1))

pq = PriorityQueue()
lpq = LinkedPriorityQueue()

time1 = time.time()
for i in range(10000):
    pq.insert(i)
for i in range(10000):
    pq.remove()
time2 = time.time()

print("{0:19}  :  {1}".format("PriorityQueue", time2-time1))

time1 = time.time()
for i in range(100000):
    lpq.insert(i)
for i in range(100000):
    lpq.remove()
time2 = time.time()
print("{0:19}  :  {1}".format("LinkedPriorityQueue", time2-time1))
