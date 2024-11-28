#!/usr/bin/env python3 

import threading

# Shared resource and lock
shared_data = 0
read_count = 0
data_lock = threading.Lock()
read_count_lock = threading.Lock()

def reader(reader_id):
    global read_count, shared_data
    with read_count_lock:
        read_count += 1
        if read_count == 1:
            data_lock.acquire()  # First reader locks the shared resource
    print(f"Reader {reader_id} is reading: {shared_data}")
    with read_count_lock:
        read_count -= 1
        if read_count == 0:
            data_lock.release()  # Last reader releases the shared resource

def writer(writer_id):
    global shared_data
    data_lock.acquire()
    shared_data += 1
    print(f"Writer {writer_id} is writing: {shared_data}")
    data_lock.release()

# Creating threads
threads = []
for i in range(2):
    threads.append(threading.Thread(target=writer, args=(i,)))
    threads.append(threading.Thread(target=reader, args=(i,)))

for t in threads:
    t.start()
for t in threads:
    t.join()
