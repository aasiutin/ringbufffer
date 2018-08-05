# Ring Buffer

The ring buffer is a data structure of fixed sized and is a FIFO queue that is connected end-to-end. This makes the ring buffer cyclic in nature.

You should have Python3 installed to run these scripts.

To run simply execute in your terminal.
```shell
python3 ringbuffer.py
```

To run tests please execute
```shell
python3 test_ringbuffer.py
```

`ringbuffer.py` implementation represents ringbuffer as data structure, which consists of an array with data (fixed size, equals to maxlen), read and write cursors (position in array for next read and next write) and buffer actual size.

Each time we write to a ring buffer:
- check if buffer has enough capacity for a new data.
- write item to data array in write cursor position
- adjust buffer size and write cursor position

Each time we read from a ring buffer:
- check if buffer is not empty
- pick the value stored in buffer data array at current reader cursor position
- adjust buffer size and read cursor position
- return value we picked from buffer

The important note here is we have to watch for read and write cursors moving out of buffer data range.
If this happens we should adjust cursors and move them to the beginning of data array.

`ringbuffer_deque.py` contains implementation which uses pythons deque data structure. We don't have to manage read and write cursors in this case, which makes whole algorithm easier. Tests for `ringbuffer_deque.py` are not implemented.
