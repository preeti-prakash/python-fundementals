def next_fibonacci(threshold):
    a=0
    b=1
    while True:
        fib = a + b
        if fib > threshold:
            break
        a=b
        b=fib
    return fib
    
print(next_fibonacci(20))