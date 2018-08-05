package main

import (
  "fmt"
  "errors"
)

type RingBuffer struct {
  size uint
  readCursor uint
  writeCursor uint
  data []int
}

func createBuffer(size int) *RingBuffer {
  r := &RingBuffer{}
  r.data = make([]int, size, size)
  return r
}

func (buf *RingBuffer) append(item int) bool {
  if buf.size < uint(len(buf.data)) {
    buf.data[buf.writeCursor] = item
    buf.size +=1
    buf.writeCursor = (buf.writeCursor+1) % uint(len(buf.data))
    return true
  }
  return false
}

func (buf *RingBuffer) Write(items []int) int {
  items_written := 0
  for _, v := range items {
    if buf.append(v) {
      items_written += 1
    } else {
      break
    }
  }
  return items_written
}

func (buf RingBuffer) IsEmpty() bool {
  return buf.size == 0
}

func (buf *RingBuffer) Read() (int, error) {
  if buf.IsEmpty() {
    return 0, errors.New("ringbuffer is empty")
  }
  value := buf.data[buf.readCursor]
  buf.readCursor = (buf.readCursor+1) % uint(len(buf.data))
  buf.size -= 1
  return value, nil
}

func main() {
  buf := createBuffer(5)
  i := buf.Write([]int{1,2,3})
  fmt.Printf("%d items were written\n", i)
  i = buf.Write([]int{4,5,6})
  fmt.Printf("%d items were written\n", i)
  var err error
  var v int
  for !buf.IsEmpty() {
    v, err = buf.Read()
    if err == nil {
      fmt.Printf("read %d\n",v)
    }
  }
  fmt.Println("Finish reading")
}
