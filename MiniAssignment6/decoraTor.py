def twice(fun1):
    def math():
        fun1()
    return math()


@twice
def multipy_two_numbers(num1, num2):
    print(num1 * num2)


multipy_two_numbers(2, 3)

