import time

def count():
    print("One")
    time.sleep(1)
    print("Two")
    time.sleep(1)

def main():
    for _ in range(3):
        count()

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start
    file_name = __file__.split("\\")[-1]
    print(f"{file_name} executed in {elapsed:0.2f} seconds.")