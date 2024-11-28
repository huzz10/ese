#!/usr/bin/env python3

import threading

# Shared resource and semaphore
shared_data = 0
read_count = 0
data_sem = threading.Semaphore(1)
read_count_sem = threading.Semaphore(1)

def reader(reader_id):
    global read_count, shared_data
    read_count_sem.acquire()
    read_count += 1
    if read_count == 1:
        data_sem.acquire()  # First reader locks the shared resource
    read_count_sem.release()

    # Reading the shared data
    print(f"Reader {reader_id} is reading: {shared_data}")

    read_count_sem.acquire()
    read_count -= 1
    if read_count == 0:
        data_sem.release()  # Last reader releases the shared resource
    read_count_sem.release()

def writer(writer_id):
    global shared_data
    data_sem.acquire()
    shared_data += 1
    print(f"Writer {writer_id} is writing: {shared_data}")
    data_sem.release()

# Creating threads
threads = []
for i in range(2):
    threads.append(threading.Thread(target=writer, args=(i,)))
    threads.append(threading.Thread(target=reader, args=(i,)))

for t in threads:
    t.start()
for t in threads:
    t.join()

