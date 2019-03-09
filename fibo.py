# Fibonacci numbers module

def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


def fib(n):  # write Fibonacci series up to n
    print(fib2(n))


if __name__ == "__main__":  # True when called as main
    import sys

    fib(int(sys.argv[1]))