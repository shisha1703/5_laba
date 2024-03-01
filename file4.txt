def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    n = int(input("Номер элемента ряда Фибоначчи: "))
    result = fibonacci(n)
    print("Значение этого элемента:", result)


main()