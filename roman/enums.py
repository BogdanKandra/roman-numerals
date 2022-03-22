from enum import Enum, unique


@unique
class RomanNumeral(Enum):
    """ Enumeration used for representing all possible roman numerals """
    N = 0
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
