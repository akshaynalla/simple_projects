""""
Program that uses recursion to calculate the fibonacci number at a given place
example:
Position = 5
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8

"""
SEQUENCE = 7


def fibonacci(sequence):

    if sequence == 0:
        return 0
    if sequence == 1:
        return 1
    return fibonacci(sequence - 1) + fibonacci(sequence - 2)


def main():

    answer = fibonacci(SEQUENCE)
    print(answer)

    fibonacci_list = []

    for i in range(SEQUENCE + 1):
        fibonacci_list.append(fibonacci(i))
    print(fibonacci_list)


if __name__ == "__main__":
    main()