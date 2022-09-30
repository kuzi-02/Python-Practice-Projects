queue = [None for i in range(int(input("MaXC")))]
noelements = 0
head = 0
tail = -1


def enqueue(new):
    global queue, noelements, head, tail
    if noelements < len(queue):
        if tail == len(queue) - 1:
            tail = 0
        else:
            tail = tail + 1
        queue[tail] = new

    else:
        print("queue is full!")


def deque():
    global head, queue, tail
    item = queue[head]
