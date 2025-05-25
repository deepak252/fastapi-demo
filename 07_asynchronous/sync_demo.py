import time

def counter():
    for _ in range(30000000):
        pass

def sequential_execution():
    start_time = time.time()

    counter()
    counter()
    counter()

    end_time = time.time()

    print(f"Sequential Execuction Time: {end_time-start_time} seconds")
    # Sequential Execuction Time: 2.069153070449829 seconds

if __name__ == "__main__":
    sequential_execution()