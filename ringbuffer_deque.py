from collections import deque
import sys


class RingBuffer:
    def __init__(self, maxlen):
        self.q = deque(maxlen=maxlen)

    def append(self, item):
        if len(self.q) < self.q.maxlen:
            self.q.append(item)
            return True
        return False

    def write(self, items):
        total_added = 0
        for i in items:
            if self.append(i):
                total_added += 1
            else:
                break
        return total_added

    def read(self):
        if len(self.q) > 0:
            return self.q.popleft()
        raise BaseException(msg="ringbuffer is empty")

if __name__ == '__main__':

    try:
        buffer = RingBuffer(5)
        print(buffer.write([1, 2, 3]))
        print(buffer.write([4, 5, 6]))
        print(buffer.read())
        print(buffer.read())
        print(buffer.read())
        print(buffer.read())
        print(buffer.read())
    except:
        print(str(sys.exc_info()[0]))
