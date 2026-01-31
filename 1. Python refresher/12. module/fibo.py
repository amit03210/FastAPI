def fibo(x):
    a, b = 0, 1
    for _ in range(x):
        print(a, end= " ")
        a, b = b, a+b;

if __name__ == "__main__":
    import sys
    fibo(int(sys.argv[1]))

