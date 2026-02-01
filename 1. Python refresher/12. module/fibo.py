def fibo(x):
    a, b = 0, 1
    for _ in range(x):
        if a > x:
            break
        print(a, end= " ")
        a, b = b, a+b;

def fibo_list(x):
    a, b = 0, 1
    result = []
    for _ in range(x):
        if a > x:
            break;
        result.append(a)
        a, b = b, a+b;
    print(result)
    return result;


if __name__ == "__main__":
    fibo_list(15);

