# Fibonacci sequence

def fibonacci(n):
    a = 0
    b = 1

    if n < 0:
        print("Incorrect input: n can't be less than 0")

    elif n == 0:
        return 0

    elif n == 1:
        return b

    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return c

     

print(fibonacci(3))