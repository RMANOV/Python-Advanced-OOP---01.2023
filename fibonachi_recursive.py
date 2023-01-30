# fibonachi recursive


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

n = int(input("Enter a number: "))

print(* [fib(i) for i in range(n)], sep = ", ")
