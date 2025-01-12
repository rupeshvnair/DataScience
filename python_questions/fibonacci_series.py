def fibonacci_tab(n):
    """
    Calculates the nth Fibonacci number using tabulation.
    :param n: Position of the Fibonacci number.
    :return: nth Fibonacci number.
    """
    if n <= 2:  # Base case
        return 1

    fib = [0] * (n + 1)  # Initialize table
    fib[1], fib[2] = 1, 1  # Set base cases

    for i in range(3, n + 1):  # Fill the table iteratively
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


# Example Usage

def fib(n):
    if n<=1:
        return 0
    if n==2:
        return 1
    val = fib(n-1)+ fib(n-2)
    return val

print(fibonacci_tab(10))
print(fib(11))