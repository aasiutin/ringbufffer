import unittest
from ringbuffer import RingBuffer

class RingBufferTestCase(unittest.TestCase):
    """Test for RingBuffer class"""

    def test_write_once(self):
        """signle write should return number of elements written to buffer"""

        buffer = RingBuffer(5)
        items_written = buffer.write([1, 2, 3])
        self.assertEqual(items_written, 3, msg="3 items should have been written")

    def test_write_with_overflow(self):
        """
        if we want to write more items than free space in Buffer, we get only
        subset of items written in buffer
        """

        buffer = RingBuffer(5)
        num_items = buffer.write([1, 2, 3])
        self.assertEqual(num_items, 3)
        num_items = buffer.write([4, 5, 6, 7])
        self.assertEqual(num_items, 2)

    def test_read_from_empty_buffer(self):
        """if we read from empty buffer, we get an exception"""

        buffer = RingBuffer(5)
        with self.assertRaises(BaseException):
            item = buffer.read()

    def test_a_typical_workflow(self):
        """here we test typical buffer workflow (writes and reads)"""

        buffer = RingBuffer(5)
        buffer.write([1, 2, 3])
        buffer.write([4, 5, 6])
        buffer.read()
        buffer.read()
        buffer.write([7,77,777,7777])
        buffer.read()
        buffer.read()
        buffer.read()
        buffer.read()
        buffer.read()

        with self.assertRaises(BaseException):
            item = buffer.read()

if __name__ == '__main__':
    unittest.main()
