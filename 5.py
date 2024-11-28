#!/usr/bin/env python3
import threading

class SharedData:
    def __init__(self):
        self.data = ""
        self.readers = 0
        self.lock = threading.Lock()

shared_data = SharedData()

def reader():
    while True:
        with shared_data.lock:
            shared_data.readers += 1
        print(f"Reader is reading data: {shared_data.data}")
        with shared_data.lock:
            shared_data.readers -= 1
        break

def writer():
    while True:
        with shared_data.lock:
            while shared_data.readers > 0:
                pass
            shared_data.data = input("Writer: Enter new data: ")
        print("Writer has updated the data.")
        break

# Threads for reader and writer
reader_thread = threading.Thread(target=reader)
writer_thread = threading.Thread(target=writer)

writer_thread.start()
reader_thread.start()

writer_thread.join()
reader_thread.join()

