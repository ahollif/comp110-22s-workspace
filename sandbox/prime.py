"""Prime number functions."""


def is_prime(number: int) -> bool:
    assert type(number) == int
    if number % 2 == 0:
        return False
    i = int(number ** 0.5)
    while i <= number / 2:
        if number % i == 0:
            return False
        else: 
            i += 1
    return True


def prime_range(number: int) -> list:
    i = 1
    output = []
    while i < number:
        if is_prime(i):
            output.append(i)
            i += 2
        else:
            i += 2
    return output


def largest_prime_factor(number: int) -> int:
    """Returns the largest prime factor of a number."""
    sqrt = (int(number ** 0.5))
    ticker1 = 1
    ticker2 = sqrt
    if is_prime(number):
        return number
    if ticker2 % 2 == 0: 
        ticker2 -= 1
    max1 = 1
    max2 = 1
    while ticker1 <= sqrt:
        if number % ticker1 == 0 and is_prime(ticker1):
            max1 = ticker1
            ticker1 += 2
        else:
            ticker1 += 2
    while ticker2 <= (number / 2):
        if number % ticker2 == 0 and is_prime(ticker2):
            max2 = ticker2
            ticker2 += 2
        else:
            ticker2 += 2
    
    return max(max1, max2)