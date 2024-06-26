import asyncio
import itertools
from typing import Iterator, List, Union
from scripts.enums import RomanNumeral
from scripts.exceptions import RomanNumeralValueError, RomanNumeralTypeError


### User-defined decorator function
def validated(fn):
    """ Decorator which enables the validation of input for functions taking roman numeral representations as a
    parameter (decimal or string). The typing syntax used here means that <fn> takes a parameter of type Union[int, str]
    and returns a value of type Union[str, int]. The decorator will wrap the function and check if the provided
    representation is valid before calling the wrapped function. If the representation is invalid, a
    RomanNumeralValueError exception will be raised. If the representation is valid, the wrapped function will be
    called with the representation as a parameter. The decorator will return the wrapped function."""
    def wrapper(representation: Union[str, int]):
        validation_result = Roman.validate(representation)
        if validation_result == 'OK':
            return fn(representation)
        else:
            raise RomanNumeralValueError(validation_result)

    return wrapper


class Roman:
    """ Class which implements support for and arithmetic operations with Roman Numerals """
    def __init__(self, representation: Union[str, int] = 'N'):
        """ The constructor first checks if the representation is a valid roman numeral representation, then converts
        the representation to get the other one and then sets the appropriate fields **roman** and **decimal** on the
        object. Parameterless constructor creates the *N* roman numeral (Nulla = 0) """
        validation_result = Roman.validate(representation)

        if validation_result == 'OK':
            # Convert it and set fields
            if isinstance(representation, str):
                self.roman = representation.upper()
                self.decimal = Roman.convert_to_decimal(representation)
            elif isinstance(representation, int):
                self.roman = Roman.convert_to_roman(representation)
                self.decimal = representation
        else:
            raise RomanNumeralValueError(validation_result)

        self.iter_idx = 0

    ### Type conversion methods
    def __repr__(self) -> str:
        """ Returns an information-rich string representation of the Roman numeral object. Typically used for debugging.
        This will also be the form used in hashable collections, such as sets, frozensets and dictionaries. """
        representation = 'Roman Numeral -> Roman representation: {self.roman}; decimal representation: {self.decimal}'
        return representation.format(self=self)

    def __str__(self) -> str:
        """ Represents the Roman numeral in a more informal way. It is called when printing and if this function is not
        defined, __repr__ will be used """
        return '{self.roman} ({self.decimal})'.format(self=self)

    def __int__(self) -> int:
        """ Converts the Roman numeral to an integer """
        return self.decimal

    def __bool__(self) -> bool:
        """ Converts the Roman numeral to a boolean """
        return bool(self.decimal)

    def __len__(self) -> int:
        """ Returns the number of letters in the roman representation """
        return len(self.roman)

    def __abs__(self) -> int:
        """ Returns the absolute value of the Roman numeral. Since Roman cannot be negative, the value will be returned
        as it is, in decimal format """
        return abs(self.decimal)

    def __hash__(self) -> int:
        """ Returns the hashed version of the object, for use on members of hashed collections, such as set, frozenset
        and dict. Without implementing this, Roman numbers will not be usable as items in hashable collections """
        return hash(self.decimal)

    ### Arithmetic operators
    def __add__(self, other) -> 'Roman':
        """ Implements the left-sided addition for Roman numerals """
        if isinstance(other, Roman):
            return Roman(self.decimal + other.decimal)
        elif isinstance(other, int):
            return Roman(self.decimal + other)
        elif isinstance(other, str):
            return Roman(self.decimal + Roman(other).decimal)
        else:
            raise TypeError(f'Roman numeral addition requires str, int or Roman as right operand, not {type(other)}')

    def __radd__(self, other) -> 'Roman':
        """ Implements the right-sided addition for Roman numerals. Without this function, computing 100 + Roman("X")
        is not possible """
        return self.__add__(other)

    def __sub__(self, other) -> 'Roman':
        """ Implements the left-sided subtraction for Roman numerals """
        if isinstance(other, Roman):
            return Roman(self.decimal - other.decimal)
        elif isinstance(other, int):
            return Roman(self.decimal - other)
        elif isinstance(other, str):
            return Roman(self.decimal - Roman(other).decimal)
        else:
            raise TypeError(f'Roman numeral subtraction requires str, int or Roman as right operand, not {type(other)}')

    def __mul__(self, other) -> 'Roman':
        """ Implements the left-sided multiplication for Roman numerals """
        if isinstance(other, Roman):
            return Roman(self.decimal * other.decimal)
        elif isinstance(other, int):
            return Roman(self.decimal * other)
        elif isinstance(other, str):
            return Roman(self.decimal * Roman(other).decimal)
        else:
            raise TypeError(f'Roman numeral multiplication requires str, int or Roman as right operand, not {type(other)}')

    def __rmul__(self, other) -> 'Roman':
        """ Implements the right-sided multiplication for Roman numerals. Without this function, computing
        100 * Roman("X") is not possible """
        return self.__mul__(other)

    def __floordiv__(self, other) -> 'Roman':
        """ Implements the left-sided floor division for Roman numerals """
        if isinstance(other, Roman):
            return Roman(self.decimal // other.decimal)
        elif isinstance(other, int):
            return Roman(self.decimal // other)
        elif isinstance(other, str):
            return Roman(self.decimal // Roman(other).decimal)
        else:
            raise TypeError(f'Roman numeral division requires str, int or Roman as right operand, not {type(other)}')

    def __mod__(self, other) -> 'Roman':
        """ Implements the left-sided modulus operation for Roman numerals """
        if isinstance(other, Roman):
            return Roman(self.decimal % other.decimal)
        elif isinstance(other, int):
            return Roman(self.decimal % other)
        elif isinstance(other, str):
            return Roman(self.decimal % Roman(other).decimal)
        else:
            raise TypeError(f'Roman numeral modulus requires str, int or Roman as right operand, not {type(other)}')

    ### Comparison operators
    def __lt__(self, other) -> bool:
        """ Implements < comparison between Roman numerals """
        if isinstance(other, Roman):
            return self.decimal < other.decimal
        elif isinstance(other, int):
            return self.decimal < other
        elif isinstance(other, str):
            return self.decimal < Roman(other).decimal
        else:
            raise TypeError(f'Roman numeral less than comparison requires str, int or Roman as right operand, not {type(other)}')

    def __le__(self, other) -> bool:
        """ Implements <= comparison between Roman numerals """
        if isinstance(other, Roman):
            return self.decimal <= other.decimal
        elif isinstance(other, int):
            return self.decimal <= other
        elif isinstance(other, str):
            return self.decimal <= Roman(other).decimal
        else:
            raise TypeError(f'Roman numeral less or equal than comparison requires str, int or Roman as right operand, not {type(other)}')

    def __gt__(self, other) -> bool:
        """ Implements > comparison between Roman numerals """
        return not self <= other

    def __ge__(self, other) -> bool:
        """ Implements >= comparison between Roman numerals """
        return not self < other

    def __eq__(self, other) -> bool:
        """ Implements equality testing between Roman numerals """
        return not self < other and not self > other

    def __ne__(self, other) -> bool:
        """ Implements inequality testing between Roman numerals """
        return not self == other

    def __contains__(self, item) -> bool:
        """ Enables membership testing for the *in* and *not in* operators """
        if isinstance(item, str):
            return item.upper() in self.roman
        else:
            raise TypeError(f"'in <Roman>' requires string as left operand, not {type(item)}")

    ### Iterator methods
    def __iter__(self) -> 'Roman':
        """ Represents the basis of the iterator protocol, making the Roman class *iterable*. It returns an iterator
         object that defines the __next__ method; self is returned in our case, because the __next__ method is defined
         in this class. This allows Roman variables to be used with the *for .. in ..* statements, which call __iter__
         internally """
        self.iter_idx = 0
        return self

    def __next__(self) -> str:
        """ Returns the next item from the iterator. If there are no further items, raise the StopIteration exception"""
        if self.iter_idx == len(self.roman):
            raise StopIteration

        item = self.roman[self.iter_idx]
        self.iter_idx += 1

        return item

    ### Static utility methods
    @staticmethod
    def validate(representation: Union[str, int]) -> str:
        """ Checks whether the specified representation is / can be a valid Roman numeral representation. In the case
        of a string representation, it is first checked that the representation doesn't contain characters other than
        the supported ones. Then it is verified that only I, X and C are followed by larger letters and that only I, X,
        C and M are repeated in succession, no more than three times in each succession. In the case of integer
        representations, it is checked whether the representation is a non-negative number, no bigger than 3999 (the
        maximum Roman numeral) """
        if isinstance(representation, str):
            representation = representation.upper()
            roman_characters = [r.name for r in RomanNumeral]

            # Check if only the required characters are present
            character_set_difference = set(representation).difference(set(roman_characters))
            if character_set_difference != set():
                message = 'The string representation provided contains invalid characters: {}'
                return message.format(character_set_difference)

            # Make checks on each character from the representation
            for i, current in enumerate(representation):
                if i < len(representation) - 1:
                    successor = representation[i + 1]

                    # Check if current character is succeeded by a bigger character
                    if roman_characters.index(current) < roman_characters.index(successor) and \
                            current not in ['I', 'X', 'C']:
                        message = 'Only "I", "X" and "C" can be used as subtractive numerals (Used "{}")'
                        return message.format(current)

                    # Check if the current character is repeated in succession
                    if current == successor:
                        if current not in ['I', 'X', 'C', 'M']:
                            message = 'Only "I", "X", "C" and "M" can be repeated in succession (Repeated "{}")'
                            return message.format(current)

                        if i < len(representation) - 3 and successor == representation[i + 2] == representation[i + 3]:
                            message = 'Characters cannot be repeated more than 3 times in one succession (Repeated "{}" too many times)'
                            return message.format(current)

            return 'OK'
        elif isinstance(representation, int):
            if representation < 0:
                message = f'Negative Roman numerals do not exist; conversion is impossible (Provided {representation})'
            elif representation > 3999:
                message = 'The maximum Roman numeral is 3999 (Provided {})'.format(representation)
            else:
                message = 'OK'

            return message
        else:
            message = 'The representation of the Roman numeral must be in str or int format (Given: {})'
            raise RomanNumeralTypeError(message.format(type(representation)))

    @validated
    @staticmethod
    def convert_to_decimal(roman_number: str) -> int:
        """ Converts the given Roman numeral to the coresponding decimal value """
        roman_number = roman_number.upper()
        decimal_number = 0
        i = 0

        while i < len(roman_number):
            current = RomanNumeral[roman_number[i]].value

            if i < len(roman_number) - 1:
                # There are remaining letters in the representation, look ahead
                succesor = RomanNumeral[roman_number[i + 1]].value

                if current < succesor:
                    # If succesor is greater, subtract current from succesor and store the result
                    decimal_number += (succesor - current)
                    i += 1  # Skipping the succesor
                elif current > succesor:
                    # If succesor is smaller, add all smaller occurences to
                    # current and store the result; only do this if the succesor isn't
                    # a subtractive numeral
                    decimal_number += current

                    while succesor < current and (i + 1) < len(roman_number) - 1:
                        if RomanNumeral[roman_number[i + 2]].value <= succesor:
                            decimal_number += succesor
                            i += 1
                            succesor = RomanNumeral[roman_number[i + 1]].value
                        else:
                            break
                else:
                    # If succesor is same, then add up all repeated occurences and store the result
                    decimal_number += (current * 2)
                    i += 1
                    if (i + 1) < len(roman_number) - 1:
                        succsuccesor_num = RomanNumeral[roman_number[i + 1]].value
                        if succsuccesor_num == current:
                            decimal_number += current
                            i += 1
            else:
                # We are at the last character in the representation
                decimal_number += current

            i += 1

        return decimal_number

    @validated
    @staticmethod
    def convert_to_roman(decimal_number: int) -> str:
        """ Converts the given decimal number to the coresponding Roman numeral """
        if decimal_number == 0:
            roman_representation = 'N'
        else:
            roman_characters = [r.name for r in RomanNumeral]
            roman_representation = ''
            digit_order = 1

            while decimal_number != 0:
                last_digit = decimal_number % 10

                if last_digit in [1, 2, 3]:
                    letter_index = digit_order * 2 - 1
                    roman_representation = last_digit * roman_characters[letter_index] + \
                                           roman_representation
                elif last_digit == 4:
                    letter_index = digit_order * 2 - 1
                    roman_representation = roman_characters[letter_index] + \
                                           roman_characters[letter_index + 1] + \
                                           roman_representation
                elif last_digit == 5:
                    letter_index = digit_order * 2
                    roman_representation = roman_characters[letter_index] + \
                                           roman_representation
                elif last_digit in [6, 7, 8]:
                    letter_index = digit_order * 2
                    roman_representation = roman_characters[letter_index] + \
                                           (last_digit - 5) * roman_characters[letter_index - 1] + \
                                           roman_representation
                elif last_digit == 9:
                    letter_index = digit_order * 2 - 1
                    roman_representation = roman_characters[letter_index] + \
                                           roman_characters[letter_index + 2] + \
                                           roman_representation

                decimal_number = decimal_number // 10
                digit_order += 1

        return roman_representation

    ### User-defined Generators
    @staticmethod
    def roman_generator() -> Iterator['Roman']:
        """ Generator function which generates the Roman numerals from 1 to 3999 """
        for i in range(4000):
            yield Roman(i)

    @staticmethod
    def fibonacci_generator() -> Iterator['Roman']:
        """ Generator function which generates the Roman Fibonacci numbers """
        a, b = Roman(1), Roman(1)

        while True:
            yield a
            if a.decimal + b.decimal < 4000:
                a, b = b, a + b
            else:
                yield b
                break

    @staticmethod
    def prime_generator() -> Iterator['Roman']:
        """ Generator function which generates the Roman prime numbers """
        yield Roman(2)

        candidate = 3
        divisors = [2]

        while True:
            # If dividing <candidate> by all the numbers in <divisors>, up to and including sqrt(<candidate>), produces
            # a non-zero remainder, then <candidate> is prime
            if all(candidate % f > 0 for f in itertools.takewhile(lambda f: f * f <= candidate, divisors)):
                yield Roman(candidate)
                divisors.append(candidate)
            if candidate + 2 < 4000:
                candidate += 2
            else:
                break

    ### User-defined Coroutines
    @staticmethod
    async def producer(queue: asyncio.Queue) -> None:
        ''' Produce Roman Fibonacci numbers and put them into a queue'''
        for number in Roman.fibonacci_generator():
            await queue.put(number)
            await asyncio.sleep(0.5)  # Simulate I/O-bound operation
        await queue.put(None)  # Signal to the consumer that the producer is done

    @staticmethod
    async def consumer(queue: asyncio.Queue) -> List['Roman']:
        ''' Consume Roman numbers from a queue and print them if they are prime '''
        roman_primes = list(Roman.prime_generator())
        consumed_primes = []

        while True:
            number = await queue.get()
            queue.task_done()
            if number is None:
                break
            if number in roman_primes:
                print(f'Consumed Roman prime: {number}')
                consumed_primes.append(number)

        return consumed_primes
