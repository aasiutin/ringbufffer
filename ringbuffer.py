import sys

class RingBuffer:
    def __init__(self, maxlen):
        self.q = [None]*maxlen
        self.size = 0
        self.writeCursor = 0
        self.readCursor = 0

    def append(self, item):
        if self.size < len(self.q):
            self.q[self.writeCursor] = item
            self.size += 1
            self.writeCursor = (self.writeCursor + 1) % len(self.q)
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
        if self.size > 0:
            self.size -= 1
            val = self.q[self.readCursor]
            self.readCursor = (self.readCursor+1) % len(self.q)
            return val

        raise BaseException("ringbuffer is empty")

    def __str__(self):
        return "{} r={},w={},size={}".format(self.q, self.readCursor, self.writeCursor, self.size)

if __name__ == '__main__':

    try:
        buffer = RingBuffer(5)

        print("Writing [1,2,3] to ringbuffer")
        items_written = buffer.write([1, 2, 3])
        print("{} items were written".format(items_written))

        print("Writing [4,5,6] to ringbuffer")
        items_written = buffer.write([4, 5, 6])
        print("{} items were written".format(items_written))

        print("Writing [100,100,100] to ringbuffer")
        items_written = buffer.write([100, 100, 100])
        print("{} items were written".format(items_written))

        print("reading ", buffer.read())
        print("reading ", buffer.read())

        print("Writing [7,77,777,7777] to ringbuffer")
        items_written = buffer.write([7, 77, 777, 7777])
        print("{} items were written".format(items_written))


        print("reading ", buffer.read())
        print("reading ", buffer.read())
        print("reading ", buffer.read())
        print("reading ", buffer.read())
        print("reading ", buffer.read())
    except:
        print(str(sys.exc_info()[0]))
