# print(user_input.split())
import sys

while (True):
    user_input = input("enter the String: ")
    if (user_input == "quit"):
        sys.exit()
    ls1 = list(user_input.split(" "))
    try:
        num1 = float(ls1[0])
        num2 = float(ls1[2])
        if (ls1[1] == "+"):
            print(num2 + num1)
        elif (ls1[1] == "-"):
            print(num1 - num2)
        else:
            raise Exception()
    except Exception as e:
        print("!!Incorrect format ,please enter correct Formulae")
    finally:
        print("bye")
