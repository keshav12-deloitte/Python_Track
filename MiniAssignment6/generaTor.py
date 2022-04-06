def fibonacci(n):
    first = 0
    second = 1
    while (n > 0):
        yield first
        sum = first + second
        first = second
        second = sum
        n -= 1


n = int(input("enter the value of n : "))
value = fibonacci(n)
for i in value:
    print(i)
