n = 45

def is_happy(n: int) -> bool:
    """
    Determines whether a number is a happy number. A happy number is defined by the following process:
    starting with any positive integer, replace the number by the sum of the squares of its digits,
    and repeat the process until the number equals 1 or a loop is detected.

    A happy number will eventually reach 1, while a non-happy number will enter a cycle that does not include 1.

    :param n: The number to be checked.
    :type n: int
    :return: True if the number is a happy number, False otherwise.
    :rtype: bool
    """
    
    seen_numbers = set()
    while (n != 1) and (n not in seen_numbers):
        seen_numbers.add(n)
        n = sum([int(i) ** 2 for i in str(n)])
    return n == 1


if __name__ == "__main__":
    assert is_happy(7) is True
    assert is_happy(45) is False
    assert is_happy(44) is True