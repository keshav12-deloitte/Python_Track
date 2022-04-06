def twice_multiply(fun1):
    def mul(num1, num2):
        fun1(num1, num2)
        fun1(num1, num2)

    return mul


@twice_multiply
def multiply(num1, num2):
    print(num1 * num2)


num1 = int(input("enter the first number: "))
num2 = int(input("enter the second  number: "))
multiply(num1, num2)
