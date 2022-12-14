# https://py.checkio.org/en/mission/bigger-together/

from typing import List


def bigger_together(ints: List[int]) -> int:
    """
        Returns difference between the largest and smallest values
        that can be obtained by concatenating the integers together.
    """

    max_length = max(len(str(x)) for x in ints)
    # if it is any integer with maximum length - if maximum lenght is 2,
    # divide it by 10, lenght 3 - divided by 100 etc
    # if it is an integer of length smaller than maxumum length,
    # turn it into a float such that the digits to the right and the digits
    # to the  left of the decimal point are equal - for example 43 becomes 43.43
    # This way if you have 423 and 42 for example, 42 will go in front of 423
    # and you will have 42423 maximum nu8mber and not 42342
    maximum = sorted(ints, reverse=True,
                     key=lambda x: float(str(x) + '.' + str(x)) if len(str(x)) < max_length else x / (
                                 10 ** (len(str(x)) - 1)))
    # The same as the above to get the minimum
    minimum = sorted(ints, key=lambda x: float(str(x) + '.' + str(x)) if len(str(x)) < max_length else x / (
                10 ** (len(str(x)) - 1)))
    str_maximum = "".join(map(lambda x: str(x), maximum))
    str_minimum = "".join(map(lambda x: str(x), minimum))

    return abs(int(str_maximum) - int(str_minimum))
