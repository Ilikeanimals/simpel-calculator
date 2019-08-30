if __name__ == '__main__':
    def add(num1, num2):
        return int(num1) + int(num2)

    def subtrac(num1, num2):
        return int(num1) - int(num2)

    def multiply(num1, num2):
        return int(num1) * int(num2)

    def divide(num1, num2):
        return int(num1) / int(num2)

    print("""Select operation.
    add
    subtract
    multiply
    divide""")
    o = input('Enter choice(1/2/3/4): ')
    num1 = input('Enter first number:')
    num2 = input('Enter second number:')
    if operation == "1":
        print(num1, " + ", num2, " = ", add(num1, num2))
    elif operation == "2":
        print(num1, " - ", num2, " = ", subtrac(num1, num2))
    elif operation == "3":
        print(num1, " * ", num2, " = ", multiply(num1, num2))
    elif operation == "4":
        print(num1, " / ", num2, " = ", divide(num1, num2))


