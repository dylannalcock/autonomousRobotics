def compute_fibonacci(n):
    """Return the nth Fibonacci number.

    >>> compute_fibonacci(0)
    0
    >>> compute_fibonacci(1)
    1
    >>> compute_fibonacci(2)  # 0 + 1
    1
    >>> compute_fibonacci(3)  # 1 + 1
    2
    >>> compute_fibonacci(4)  # 1 + 2
    3
    """
    # BEGIN QUESTION 1.1
    "*** REPLACE THIS LINE ***"
    if n == 0:
        return 0
    elif n == 1:
        return 1

    prev1 = 0
    prev2 = 1

    for i in range(1,n):
        temp = prev2
        prev2 = prev1 + prev2
        prev1 = temp
    return prev2
    # END QUESTION 1.1
