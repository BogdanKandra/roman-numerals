from scripts.exceptions import RomanNumeralTypeError, RomanNumeralValueError
from scripts.roman import Roman
import pytest


class TestRoman:
    ''' Tests for the Roman class '''
    ### Tests for the creation of Roman numerals
    def test_invalid_representation_characters(self):
        ''' Tests that a RomanNumeralValueError is raised when trying to create
        a Roman numeral with a representation string containing unsupported
        characters '''
        representation = 'KANDIA'
        with pytest.raises(RomanNumeralValueError) as e:
            r = Roman(representation)
            assert 'The string representation provided contains invalid characters:' in e

    def test_invalid_representation_invalid_subtractive_numerals(self):
        ''' Tests that a RomanNumeralValueError is raised when trying to create
        a Roman numeral with a representation string containing invalid
        subtractive numerals '''
        representation = 'LM'
        with pytest.raises(RomanNumeralValueError) as e:
            r = Roman(representation)
            assert 'Only "I", "X" and "C" can be used as subtractive numerals' in e

    def test_invalid_representation_invalid_repeated_numerals(self):
        ''' Tests that a RomanNumeralValueError is raised when trying to create
        a Roman numeral with a representation string containing invalid
        repeated numerals '''
        representation = 'LLD'
        with pytest.raises(RomanNumeralValueError) as e:
            r = Roman(representation)
            assert 'Only "I", "X", "C" and "M" can be repeated in succession' in e

    def test_invalid_representation_over_repeated_numerals(self):
        ''' Tests that a RomanNumeralValueError is raised when trying to create
        a Roman numeral with a representation string containing too many
        repetitions of a valid character, in a single succession '''
        representation = 'IIIII'
        with pytest.raises(RomanNumeralValueError) as e:
            r = Roman(representation)
            assert 'Characters cannot be repeated more than 3 times in one succession' in e

    def test_invalid_representation_negative_number(self):
        ''' Tests that a RomanNumeralValueError is raised when trying to create
        a Roman numeral from a negative number '''
        representation = -420
        with pytest.raises(RomanNumeralValueError) as e:
            r = Roman(representation)
            assert 'Negative Roman numerals do not exist; conversion is impossible' in e

    def test_invalid_representation_too_big(self):
        ''' Tests that a RomanNumeralValueError is raised when trying to create
        a Roman numeral from a number too big '''
        representation = 7777
        with pytest.raises(RomanNumeralValueError) as e:
            r = Roman(representation)
            assert 'The maximum Roman numeral is 3999' in e

    def test_invalid_representation_type(self):
        ''' Tests that a RomanNumeralTypeError is raised when trying to create
        a Roman numeral from a representation of an invalid format '''
        representation = 8.5
        with pytest.raises(RomanNumeralTypeError) as e:
            r = Roman(representation)
            assert 'The representation of the Roman numeral must be in str or int format' in e

    def test_valid_representation_string(self):
        ''' Tests that Roman numerals are successfully created from a valid
        representation string and the conversion to decimal is correct '''
        representation = 'MMXXI'
        r = Roman(representation)
        
        assert r.decimal == 2021
        assert r.roman == 'MMXXI'

    def test_valid_representation_number(self):
        ''' Tests that Roman numerals are successfully created from a valid
        representation number and the conversion to Roman is correct '''
        representation = 3999
        r = Roman(representation)
        assert r.decimal == 3999
        assert r.roman == 'MMMCMXCIX'

        representation = 0
        r = Roman(representation)
        assert r.decimal == 0
        assert r.roman == 'N'

    ### Tests for the type conversion and string methods
    def test_repr(self):
        ''' Tests that the __repr__ method prints the expected information '''
        representation = 777
        r = Roman(representation)

        expected = 'Roman Numeral -> Roman representation: DCCLXXVII; decimal representation: 777'
        assert repr(r) == expected

    def test_str(self):
        ''' Tests that the __str__ method prints the expected information '''
        representation = 'MMXCV'
        r = Roman(representation)

        expected = 'MMXCV (2095)'
        assert str(r) == expected

    def test_int(self):
        ''' Tests that the int() function returns the decimal representation of
        the Roman numeral '''
        representation = 'CCCXXXIII'
        r = Roman(representation)

        expected = 333
        assert int(r) == expected

    def test_bool(self):
        ''' Tests that the bool() function correctly identifies zero and non-zero
        Roman numerals '''
        representation = 'CXI'
        r = Roman(representation)
        expected = True
        assert bool(r) == expected

        representation = 'N'
        r = Roman(representation)
        expected = False
        assert bool(r) == expected

    def test_len(self):
        ''' Tests that the len() function correctly prints the number of letters
        from the Roman representation of a numeral '''
        representation = 3999
        r = Roman(representation)

        expected = 9
        assert len(r) == expected

    def test_abs(self):
        ''' Tests that the abs() function correctly prints the decimal
        representation of a Roman numeral '''
        representation = 'MCMXCIII'
        r = Roman(representation)

        expected = 1993
        assert abs(r) == expected

    def test_hash(self):
        ''' Tests that the Roman objects can be used as keys in dicts '''
        r = Roman(2021)
        s = Roman(2020)
        d = {r: 'first', s: 'second'}

        d[r] = 'third'
        d[s] = 'fourth'

        assert d == {r: 'third', s: 'fourth'}

    ### Tests for the arithmetic operators
    def test_addition(self):
        ''' Tests that Roman numerals can be added between them and with valid
        string or integer representations of Roman numerals '''
        r1 = Roman('C')
        r2 = Roman(10)
        r3 = r1 + r2
        assert str(r3) == 'CX (110)'

        r1 = Roman('C')
        r2 = 10
        r3 = r1 + r2
        r4 = r2 + r1
        assert str(r3) == 'CX (110)'
        assert str(r4) == 'CX (110)'

        r1 = Roman('C')
        r2 = 'X'
        r3 = r1 + r2
        r4 = r2 + r1
        assert str(r3) == 'CX (110)'
        assert str(r4) == 'CX (110)'

    def test_subtraction(self):
        ''' Tests that Roman numerals can be subtracted between them and with
        valid string or integer representations of Roman numerals '''
        r1 = Roman('C')
        r2 = Roman(10)
        r3 = r1 - r2
        assert str(r3) == 'XC (90)'

        r1 = Roman('C')
        r2 = 10
        r3 = r1 - r2
        assert str(r3) == 'XC (90)'

        r1 = Roman('C')
        r2 = 'X'
        r3 = r1 - r2
        assert str(r3) == 'XC (90)'

    def test_multiplication(self):
        ''' Tests that Roman numerals can be multiplied between them and with
        valid string or integer representations of Roman numerals '''
        r1 = Roman('C')
        r2 = Roman(10)
        r3 = r1 * r2
        assert str(r3) == 'M (1000)'

        r1 = Roman('C')
        r2 = 10
        r3 = r1 * r2
        r4 = r2 * r1
        assert str(r3) == 'M (1000)'
        assert str(r4) == 'M (1000)'

        r1 = Roman('C')
        r2 = 'X'
        r3 = r1 * r2
        r4 = r2 * r1
        assert str(r3) == 'M (1000)'
        assert str(r4) == 'M (1000)'

    def test_division(self):
        ''' Tests that Roman numerals can be divided between them and with
        valid string or integer representations of Roman numerals '''
        r1 = Roman('C')
        r2 = Roman(10)
        r3 = r1 // r2
        assert str(r3) == 'X (10)'

        r1 = Roman('C')
        r2 = 10
        r3 = r1 // r2
        assert str(r3) == 'X (10)'

        r1 = Roman('C')
        r2 = 'X'
        r3 = r1 // r2
        assert str(r3) == 'X (10)'

    def test_modulus(self):
        ''' Tests that Roman numerals can be divided with modulus between them
        and with valid string or integer representations of Roman numerals '''
        r1 = Roman('C')
        r2 = Roman(10)
        r3 = r1 % r2
        assert str(r3) == 'N (0)'

        r1 = Roman('C')
        r2 = 10
        r3 = r1 % r2
        assert str(r3) == 'N (0)'

        r1 = Roman('C')
        r2 = 'X'
        r3 = r1 % r2
        assert str(r3) == 'N (0)'

    ### Tests for the comparison operators
    def test_less_than(self):
        ''' Tests that Roman numerals can be "<" compared between them and with
        valid string or integer representations of Roman numerals '''
        r1 = Roman('C')
        r2 = Roman(10)
        assert not r1 < r2

        r1 = Roman('C')
        r2 = 10
        assert not r1 < r2

        r1 = Roman('C')
        r2 = 'X'
        assert not r1 < r2

        r1 = Roman('N')
        r2 = Roman(3999)
        assert r1 < r2

        r1 = Roman('N')
        r2 = 3999
        assert r1 < r2

        r1 = Roman('N')
        r2 = 'MMMCMXCIX'
        assert r1 < r2

    def test_less_equal(self):
        ''' Tests that Roman numerals can be "<=" compared between them and
        with valid string or integer representations of Roman numerals '''
        r1 = Roman('C')
        r2 = Roman(10)
        assert not r1 <= r2

        r1 = Roman('C')
        r2 = 10
        assert not r1 <= r2

        r1 = Roman('C')
        r2 = 'X'
        assert not r1 <= r2

        r1 = Roman('N')
        r2 = Roman(0)
        assert r1 <= r2

        r1 = Roman('N')
        r2 = 0
        assert r1 <= r2

        r1 = Roman('N')
        r2 = 'N'
        assert r1 <= r2

    def test_greater_than(self):
        ''' Tests that Roman numerals can be ">" compared between them and
        with valid string or integer representations of Roman numerals '''
        r1 = Roman('C')
        r2 = Roman(10)
        assert r1 > r2

        r1 = Roman('C')
        r2 = 10
        assert r1 > r2

        r1 = Roman('C')
        r2 = 'X'
        assert r1 > r2

        r1 = Roman('N')
        r2 = Roman(0)
        assert not r1 > r2

        r1 = Roman('N')
        r2 = 0
        assert not r1 > r2

        r1 = Roman('N')
        r2 = 'N'
        assert not r1 > r2

    def test_greater_equal(self):
        ''' Tests that Roman numerals can be ">=" compared between them and
        with valid string or integer representations of Roman numerals '''
        r1 = Roman('C')
        r2 = Roman(10)
        assert r1 >= r2

        r1 = Roman('C')
        r2 = 10
        assert r1 >= r2

        r1 = Roman('C')
        r2 = 'X'
        assert r1 >= r2

        r1 = Roman('N')
        r2 = Roman(1)
        assert not r1 >= r2

        r1 = Roman('N')
        r2 = 1
        assert not r1 >= r2

        r1 = Roman('N')
        r2 = 'I'
        assert not r1 >= r2

    def test_equal(self):
        ''' Tests that Roman numerals can be "==" compared between them and
        with valid string or integer representations of Roman numerals '''
        r1 = Roman('C')
        r2 = Roman(10)
        assert not r1 == r2

        r1 = Roman('C')
        r2 = 10
        assert not r1 == r2

        r1 = Roman('C')
        r2 = 'X'
        assert not r1 == r2

        r1 = Roman('I')
        r2 = Roman(1)
        assert r1 == r2

        r1 = Roman('I')
        r2 = 1
        assert r1 == r2

        r1 = Roman('I')
        r2 = 'I'
        assert r1 == r2

    def test_not_equal(self):
        ''' Tests that Roman numerals can be "!=" compared between them and
        with valid string or integer representations of Roman numerals '''
        r1 = Roman('C')
        r2 = Roman(10)
        assert r1 != r2

        r1 = Roman('C')
        r2 = 10
        assert r1 != r2

        r1 = Roman('C')
        r2 = 'X'
        assert r1 != r2

        r1 = Roman('I')
        r2 = Roman(1)
        assert not r1 != r2

        r1 = Roman('I')
        r2 = 1
        assert not r1 != r2

        r1 = Roman('I')
        r2 = 'I'
        assert not r1 != r2

    ### Invertibility test
    def test_invertible(self):
        ''' Tests that the conversion to Roman numerals is invertible, i.e.
        converting to Roman and back to decimal should yield the same numbers '''
        romans = []
        decimals = []

        for i in range(4000):
            romans.append(Roman.convert_to_roman(i))
        
        for n in romans:
            decimals.append(Roman.convert_to_decimal(n))
        
        assert decimals == list(range(4000))
