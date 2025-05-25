import time
import multiprocessing

# CPU Intensive Task
def counter():
    for _ in range(30000000):
        pass


def multiprocessing_execution():
    start_time = time.time()

    with multiprocessing.Pool(processes=3) as pool:
        results1 = pool.apply_async(counter)
        results2 = pool.apply_async(counter)
        results3 = pool.apply_async(counter)

        # Wait for all processes to finish
        results1.get()
        results2.get()
        results3.get()

    end_time = time.time()
    print(f"Multiprocesssing Execuction Time: {end_time-start_time} seconds")
    # Multiprocesssing Execuction Time: 0.8289031982421875 seconds

if __name__ == "__main__":
    multiprocessing_execution()