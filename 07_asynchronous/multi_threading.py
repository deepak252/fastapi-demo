import time
import threading

# CPU Intensive Task
def counter():
    for _ in range(30000000):
        pass

# def sequential_execution():
#     start_time = time.time()

#     counter()
#     counter()
#     counter()

#     end_time = time.time()

#     print(f"Sequential Execuction Time: {end_time-start_time} seconds")

def multithreading_execution():
    start_time = time.time()

    # Create threads for each method
    thread1 = threading.Thread(target=counter)
    thread2 = threading.Thread(target=counter)
    thread3 = threading.Thread(target=counter)

    # Start the threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for all threads to finish
    thread1.join()
    thread2.join()
    thread3.join()

    end_time = time.time()
    print(f"Multithreading Execuction Time: {end_time-start_time} seconds")


if __name__ == "__main__":
    # sequential_execution()
    multithreading_execution()
    # Multithreading Execuction Time: 2.0173051357269287 seconds