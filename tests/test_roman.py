from scripts.exceptions import RomanNumeralTypeError, RomanNumeralValueError
from scripts.roman import Roman, validated
from typing import List
import asyncio
import pytest


class TestRoman:
    """ Tests for the Roman class """
    ### Tests for the creation of Roman numerals
    def test_invalid_representation_characters(self):
        """ Tests that a RomanNumeralValueError is raised when trying to create
        a Roman numeral with a representation string containing unsupported
        characters """
        representation = 'KANDIA'
        with pytest.raises(RomanNumeralValueError) as e:
            Roman(representation)
        err_msg = "The string representation provided contains invalid characters:"
        assert err_msg in str(e.value)

    def test_invalid_representation_invalid_subtractive_numerals(self):
        """ Tests that a RomanNumeralValueError is raised when trying to create
        a Roman numeral with a representation string containing invalid
        subtractive numerals """
        representation = 'LM'
        with pytest.raises(RomanNumeralValueError) as e:
            Roman(representation)
        err_msg = 'Only "I", "X" and "C" can be used as subtractive numerals (Used "L")'
        assert str(e.value) == err_msg

    def test_invalid_representation_invalid_repeated_numerals(self):
        """ Tests that a RomanNumeralValueError is raised when trying to create
        a Roman numeral with a representation string containing invalid
        repeated numerals """
        representation = 'LLD'
        with pytest.raises(RomanNumeralValueError) as e:
            Roman(representation)
        err_msg = 'Only "I", "X", "C" and "M" can be repeated in succession (Repeated "L")'
        assert str(e.value) == err_msg

    def test_invalid_representation_over_repeated_numerals(self):
        """ Tests that a RomanNumeralValueError is raised when trying to create
        a Roman numeral with a representation string containing too many
        repetitions of a valid character, in a single succession """
        representation = 'IIIII'
        with pytest.raises(RomanNumeralValueError) as e:
            Roman(representation)
        err_msg = 'Characters cannot be repeated more than 3 times in one succession (Repeated "I" too many times)'
        assert str(e.value) == err_msg

    def test_invalid_representation_negative_number(self):
        """ Tests that a RomanNumeralValueError is raised when trying to create
        a Roman numeral from a negative number """
        representation = -420
        with pytest.raises(RomanNumeralValueError) as e:
            Roman(representation)
        err_msg = 'Negative Roman numerals do not exist; conversion is impossible (Provided -420)'
        assert str(e.value) == err_msg

    def test_invalid_representation_too_big(self):
        """ Tests that a RomanNumeralValueError is raised when trying to create
        a Roman numeral from a number too big """
        representation = 7777
        with pytest.raises(RomanNumeralValueError) as e:
            Roman(representation)
        err_msg = 'The maximum Roman numeral is 3999 (Provided 7777)'
        assert str(e.value) == err_msg

    def test_invalid_representation_type(self):
        """ Tests that a RomanNumeralTypeError is raised when trying to create
        a Roman numeral from a representation of an invalid format """
        representation = 8.5
        with pytest.raises(RomanNumeralTypeError) as e:
            Roman(representation)
        err_msg = "The representation of the Roman numeral must be in str or int format (Given: <class 'float'>)"
        assert str(e.value) == err_msg

    def test_valid_representation_string(self):
        """ Tests that Roman numerals are successfully created from a valid
        representation string and the conversion to decimal is correct """
        representation = 'MMXXI'
        r = Roman(representation)

        assert r.decimal == 2021
        assert r.roman == 'MMXXI'

        representation = 'xiii'
        r = Roman(representation)

        assert r.decimal == 13
        assert r.roman == 'XIII'

    def test_valid_representation_number(self):
        """ Tests that Roman numerals are successfully created from a valid
        representation number and the conversion to Roman is correct """
        representation = 3999
        r = Roman(representation)
        assert r.decimal == 3999
        assert r.roman == 'MMMCMXCIX'

        representation = 0
        r = Roman(representation)
        assert r.decimal == 0
        assert r.roman == 'N'

    ### Tests for the type conversion methods
    def test_repr(self):
        """ Tests that the __repr__ method prints the expected information """
        representation = 777
        r = Roman(representation)

        expected = 'Roman Numeral -> Roman representation: DCCLXXVII; decimal representation: 777'
        assert repr(r) == expected

    def test_str(self):
        """ Tests that the __str__ method prints the expected information """
        representation = 'MMXCV'
        r = Roman(representation)

        expected = 'MMXCV (2095)'
        assert str(r) == expected

    def test_int(self):
        """ Tests that the int() function returns the decimal representation of
        the Roman numeral """
        representation = 'CCCXXXIII'
        r = Roman(representation)

        expected = 333
        assert int(r) == expected

    def test_bool(self):
        """ Tests that the bool() function correctly identifies zero and non-zero
        Roman numerals """
        representation = 'CXI'
        r = Roman(representation)
        expected = True
        assert bool(r) == expected

        representation = 'N'
        r = Roman(representation)
        expected = False
        assert bool(r) == expected

    def test_len(self):
        """ Tests that the len() function correctly prints the number of letters
        from the Roman representation of a numeral """
        representation = 3999
        r = Roman(representation)

        expected = 9
        assert len(r) == expected

    def test_abs(self):
        """ Tests that the abs() function correctly prints the decimal
        representation of a Roman numeral """
        representation = 'MCMXCIII'
        r = Roman(representation)

        expected = 1993
        assert abs(r) == expected

    def test_hash(self):
        """ Tests that the Roman objects can be used as keys in dicts """
        r = Roman(2021)
        s = Roman(2020)
        d = {r: 'first', s: 'second'}

        d[r] = 'third'
        d[s] = 'fourth'

        assert d == {r: 'third', s: 'fourth'}

    ### Tests for the arithmetic operators
    def test_addition(self):
        """ Tests that Roman numerals can be added between them and with valid
        string or integer representations of Roman numerals """
        r1 = Roman('C')
        r2 = Roman(10)
        r3 = r1 + r2
        assert str(r3) == 'CX (110)'

        r2 = 10
        r3 = r1 + r2
        r4 = r2 + r1
        assert str(r3) == 'CX (110)'
        assert str(r4) == 'CX (110)'

        r2 = 'X'
        r3 = r1 + r2
        r4 = r2 + r1
        assert str(r3) == 'CX (110)'
        assert str(r4) == 'CX (110)'

        r2 = [15]
        with pytest.raises(TypeError) as e:
            r3 = r1 + r2
        err_msg = "Roman numeral addition requires str, int or Roman as right operand, not <class 'list'>"
        assert str(e.value) == err_msg

    def test_subtraction(self):
        """ Tests that Roman numerals can be subtracted between them and with
        valid string or integer representations of Roman numerals """
        r1 = Roman('C')
        r2 = Roman(10)
        r3 = r1 - r2
        assert str(r3) == 'XC (90)'

        r2 = 10
        r3 = r1 - r2
        assert str(r3) == 'XC (90)'

        r2 = 'X'
        r3 = r1 - r2
        assert str(r3) == 'XC (90)'

        r2 = [15]
        with pytest.raises(TypeError) as e:
            r3 = r1 - r2
        err_msg = "Roman numeral subtraction requires str, int or Roman as right operand, not <class 'list'>"
        assert str(e.value) == err_msg

    def test_multiplication(self):
        """ Tests that Roman numerals can be multiplied between them and with
        valid string or integer representations of Roman numerals """
        r1 = Roman('C')
        r2 = Roman(10)
        r3 = r1 * r2
        assert str(r3) == 'M (1000)'

        r2 = 10
        r3 = r1 * r2
        r4 = r2 * r1
        assert str(r3) == 'M (1000)'
        assert str(r4) == 'M (1000)'

        r2 = 'X'
        r3 = r1 * r2
        r4 = r2 * r1
        assert str(r3) == 'M (1000)'
        assert str(r4) == 'M (1000)'

        r2 = [15]
        with pytest.raises(TypeError) as e:
            r3 = r1 * r2
        err_msg = "Roman numeral multiplication requires str, int or Roman as right operand, not <class 'list'>"
        assert str(e.value) == err_msg

    def test_division(self):
        """ Tests that Roman numerals can be divided between them and with
        valid string or integer representations of Roman numerals """
        r1 = Roman('C')
        r2 = Roman(10)
        r3 = r1 // r2
        assert str(r3) == 'X (10)'

        r2 = 10
        r3 = r1 // r2
        assert str(r3) == 'X (10)'

        r2 = 'X'
        r3 = r1 // r2
        assert str(r3) == 'X (10)'

        r2 = [15]
        with pytest.raises(TypeError) as e:
            r3 = r1 // r2
        err_msg = "Roman numeral division requires str, int or Roman as right operand, not <class 'list'>"
        assert str(e.value) == err_msg

    def test_modulus(self):
        """ Tests that Roman numerals can be divided with modulus between them
        and with valid string or integer representations of Roman numerals """
        r1 = Roman('C')
        r2 = Roman(10)
        r3 = r1 % r2
        assert str(r3) == 'N (0)'

        r2 = 10
        r3 = r1 % r2
        assert str(r3) == 'N (0)'

        r2 = 'X'
        r3 = r1 % r2
        assert str(r3) == 'N (0)'

        r2 = [15]
        with pytest.raises(TypeError) as e:
            r3 = r1 % r2
        err_msg = "Roman numeral modulus requires str, int or Roman as right operand, not <class 'list'>"
        assert str(e.value) == err_msg

    ### Tests for the comparison operators
    def test_less_than(self):
        """ Tests that Roman numerals can be "<" compared between them and with
        valid string or integer representations of Roman numerals """
        r1 = Roman('C')
        r2 = Roman(10)
        assert not r1 < r2

        r2 = 10
        assert not r1 < r2

        r2 = 'X'
        assert not r1 < r2

        r1 = Roman('N')
        r2 = Roman(3999)
        assert r1 < r2

        r2 = 3999
        assert r1 < r2

        r2 = 'MMMCMXCIX'
        assert r1 < r2

        r2 = [15]
        with pytest.raises(TypeError) as e:
            r1 < r2
        msg = "Roman numeral less than comparison requires str, int or Roman as right operand, not <class 'list'>"
        assert str(e.value) == msg

    def test_less_equal(self):
        """ Tests that Roman numerals can be "<=" compared between them and
        with valid string or integer representations of Roman numerals """
        r1 = Roman('C')
        r2 = Roman(10)
        assert not r1 <= r2

        r2 = 10
        assert not r1 <= r2

        r2 = 'X'
        assert not r1 <= r2

        r1 = Roman('N')
        r2 = Roman(0)
        assert r1 <= r2

        r2 = 0
        assert r1 <= r2

        r2 = 'N'
        assert r1 <= r2

        r2 = [15]
        with pytest.raises(TypeError) as e:
            r1 <= r2
        msg = "Roman numeral less or equal than comparison requires str, int or Roman as right operand, not <class 'list'>"
        assert str(e.value) == msg

    def test_greater_than(self):
        """ Tests that Roman numerals can be ">" compared between them and
        with valid string or integer representations of Roman numerals """
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
        """ Tests that Roman numerals can be ">=" compared between them and
        with valid string or integer representations of Roman numerals """
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
        """ Tests that Roman numerals can be "==" compared between them and
        with valid string or integer representations of Roman numerals """
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
        """ Tests that Roman numerals can be "!=" compared between them and
        with valid string or integer representations of Roman numerals """
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

    def test_contains(self):
        """ Tests that Roman numerals can be used in conjunction with the *in* and *not in* operators for membership of
         strings (and only strings) into the roman representation of the numeral """
        r = Roman('CLIII')
        assert 'C' in r
        assert 'c' in r
        assert 'X' not in r

        with pytest.raises(TypeError) as e:
            2 in r
        err_msg = "'in <Roman>' requires string as left operand, not <class 'int'>"
        assert str(e.value) == err_msg

    ### Tests for the iterator and generator methods
    def test_iterator_protocol(self):
        """ Tests that the Python Iterator Protocol is respected by the Roman class. As such, it will be tested that
         passing a Roman instance to the iter() function will result in an iterator which can be looped over using the
         next() function. The "exhaustion" of the iterator will also be tested (i.e. calling next() after the last
         element was returned raises a StopIteration exception) """
        roman_numeral = Roman(2022)
        roman_iterator = iter(roman_numeral)
        letters = []

        # This is a simulation of the Python for loop
        while True:
            try:
                letter = next(roman_iterator)
            except StopIteration:
                break  # Iterator is exhausted; stop the loop
            else:
                letters.append(letter)

        assert letters == ['M', 'M', 'X', 'X', 'I', 'I']

    def test_iterator_is_iterable(self):
        """ Tests that the iterator is an iterable """
        roman_numeral = Roman(1993)
        roman_iterator = iter(roman_numeral)

        assert roman_iterator is iter(roman_iterator)

    def test_roman_generator(self):
        expected_numbers = [Roman(i) for i in range(4000)]

        assert list(Roman.roman_generator()) == expected_numbers

    def test_fibonacci_generator(self):
        """ Tests that the fibonacci_generator function generates the expected values """
        expected_numbers = [Roman(1), Roman(1), Roman(2), Roman(3), Roman(5), Roman(8), Roman(13),
                            Roman(21), Roman(34), Roman(55), Roman(89), Roman(144), Roman(233),
                            Roman(377), Roman(610), Roman(987), Roman(1597), Roman(2584)]

        assert list(Roman.fibonacci_generator()) == expected_numbers

    def test_prime_generator(self):
        """ Tests that the prime_generator function generates the expected values """
        expected_numbers = [Roman(2), Roman(3), Roman(5), Roman(7), Roman(11), Roman(13), Roman(17),
                            Roman(19), Roman(23), Roman(29), Roman(31), Roman(37), Roman(41), Roman(43),
                            Roman(47), Roman(53), Roman(59), Roman(61), Roman(67), Roman(71), Roman(73),
                            Roman(79), Roman(83), Roman(89), Roman(97), Roman(101), Roman(103), Roman(107),
                            Roman(109), Roman(113), Roman(127), Roman(131), Roman(137), Roman(139), Roman(149),
                            Roman(151), Roman(157), Roman(163), Roman(167), Roman(173), Roman(179), Roman(181),
                            Roman(191), Roman(193), Roman(197), Roman(199), Roman(211), Roman(223), Roman(227),
                            Roman(229), Roman(233), Roman(239), Roman(241), Roman(251), Roman(257), Roman(263),
                            Roman(269), Roman(271), Roman(277), Roman(281), Roman(283), Roman(293), Roman(307),
                            Roman(311), Roman(313), Roman(317), Roman(331), Roman(337), Roman(347), Roman(349),
                            Roman(353), Roman(359), Roman(367), Roman(373), Roman(379), Roman(383), Roman(389),
                            Roman(397), Roman(401), Roman(409), Roman(419), Roman(421), Roman(431), Roman(433),
                            Roman(439), Roman(443), Roman(449), Roman(457), Roman(461), Roman(463), Roman(467),
                            Roman(479), Roman(487), Roman(491), Roman(499), Roman(503), Roman(509), Roman(521),
                            Roman(523), Roman(541), Roman(547), Roman(557), Roman(563), Roman(569), Roman(571),
                            Roman(577), Roman(587), Roman(593), Roman(599), Roman(601), Roman(607), Roman(613),
                            Roman(617), Roman(619), Roman(631), Roman(641), Roman(643), Roman(647), Roman(653),
                            Roman(659), Roman(661), Roman(673), Roman(677), Roman(683), Roman(691), Roman(701),
                            Roman(709), Roman(719), Roman(727), Roman(733), Roman(739), Roman(743), Roman(751),
                            Roman(757), Roman(761), Roman(769), Roman(773), Roman(787), Roman(797), Roman(809),
                            Roman(811), Roman(821), Roman(823), Roman(827), Roman(829), Roman(839), Roman(853),
                            Roman(857), Roman(859), Roman(863), Roman(877), Roman(881), Roman(883), Roman(887),
                            Roman(907), Roman(911), Roman(919), Roman(929), Roman(937), Roman(941), Roman(947),
                            Roman(953), Roman(967), Roman(971), Roman(977), Roman(983), Roman(991), Roman(997),
                            Roman(1009), Roman(1013), Roman(1019), Roman(1021), Roman(1031), Roman(1033), Roman(1039),
                            Roman(1049), Roman(1051), Roman(1061), Roman(1063), Roman(1069), Roman(1087), Roman(1091),
                            Roman(1093), Roman(1097), Roman(1103), Roman(1109), Roman(1117), Roman(1123), Roman(1129),
                            Roman(1151), Roman(1153), Roman(1163), Roman(1171), Roman(1181), Roman(1187), Roman(1193),
                            Roman(1201), Roman(1213), Roman(1217), Roman(1223), Roman(1229), Roman(1231), Roman(1237),
                            Roman(1249), Roman(1259), Roman(1277), Roman(1279), Roman(1283), Roman(1289), Roman(1291),
                            Roman(1297), Roman(1301), Roman(1303), Roman(1307), Roman(1319), Roman(1321), Roman(1327),
                            Roman(1361), Roman(1367), Roman(1373), Roman(1381), Roman(1399), Roman(1409), Roman(1423),
                            Roman(1427), Roman(1429), Roman(1433), Roman(1439), Roman(1447), Roman(1451), Roman(1453),
                            Roman(1459), Roman(1471), Roman(1481), Roman(1483), Roman(1487), Roman(1489), Roman(1493),
                            Roman(1499), Roman(1511), Roman(1523), Roman(1531), Roman(1543), Roman(1549), Roman(1553),
                            Roman(1559), Roman(1567), Roman(1571), Roman(1579), Roman(1583), Roman(1597), Roman(1601),
                            Roman(1607), Roman(1609), Roman(1613), Roman(1619), Roman(1621), Roman(1627), Roman(1637),
                            Roman(1657), Roman(1663), Roman(1667), Roman(1669), Roman(1693), Roman(1697), Roman(1699),
                            Roman(1709), Roman(1721), Roman(1723), Roman(1733), Roman(1741), Roman(1747), Roman(1753),
                            Roman(1759), Roman(1777), Roman(1783), Roman(1787), Roman(1789), Roman(1801), Roman(1811),
                            Roman(1823), Roman(1831), Roman(1847), Roman(1861), Roman(1867), Roman(1871), Roman(1873),
                            Roman(1877), Roman(1879), Roman(1889), Roman(1901), Roman(1907), Roman(1913), Roman(1931),
                            Roman(1933), Roman(1949), Roman(1951), Roman(1973), Roman(1979), Roman(1987), Roman(1993),
                            Roman(1997), Roman(1999), Roman(2003), Roman(2011), Roman(2017), Roman(2027), Roman(2029),
                            Roman(2039), Roman(2053), Roman(2063), Roman(2069), Roman(2081), Roman(2083), Roman(2087),
                            Roman(2089), Roman(2099), Roman(2111), Roman(2113), Roman(2129), Roman(2131), Roman(2137),
                            Roman(2141), Roman(2143), Roman(2153), Roman(2161), Roman(2179), Roman(2203), Roman(2207),
                            Roman(2213), Roman(2221), Roman(2237), Roman(2239), Roman(2243), Roman(2251), Roman(2267),
                            Roman(2269), Roman(2273), Roman(2281), Roman(2287), Roman(2293), Roman(2297), Roman(2309),
                            Roman(2311), Roman(2333), Roman(2339), Roman(2341), Roman(2347), Roman(2351), Roman(2357),
                            Roman(2371), Roman(2377), Roman(2381), Roman(2383), Roman(2389), Roman(2393), Roman(2399),
                            Roman(2411), Roman(2417), Roman(2423), Roman(2437), Roman(2441), Roman(2447), Roman(2459),
                            Roman(2467), Roman(2473), Roman(2477), Roman(2503), Roman(2521), Roman(2531), Roman(2539),
                            Roman(2543), Roman(2549), Roman(2551), Roman(2557), Roman(2579), Roman(2591), Roman(2593),
                            Roman(2609), Roman(2617), Roman(2621), Roman(2633), Roman(2647), Roman(2657), Roman(2659),
                            Roman(2663), Roman(2671), Roman(2677), Roman(2683), Roman(2687), Roman(2689), Roman(2693),
                            Roman(2699), Roman(2707), Roman(2711), Roman(2713), Roman(2719), Roman(2729), Roman(2731),
                            Roman(2741), Roman(2749), Roman(2753), Roman(2767), Roman(2777), Roman(2789), Roman(2791),
                            Roman(2797), Roman(2801), Roman(2803), Roman(2819), Roman(2833), Roman(2837), Roman(2843),
                            Roman(2851), Roman(2857), Roman(2861), Roman(2879), Roman(2887), Roman(2897), Roman(2903),
                            Roman(2909), Roman(2917), Roman(2927), Roman(2939), Roman(2953), Roman(2957), Roman(2963),
                            Roman(2969), Roman(2971), Roman(2999), Roman(3001), Roman(3011), Roman(3019), Roman(3023),
                            Roman(3037), Roman(3041), Roman(3049), Roman(3061), Roman(3067), Roman(3079), Roman(3083),
                            Roman(3089), Roman(3109), Roman(3119), Roman(3121), Roman(3137), Roman(3163), Roman(3167),
                            Roman(3169), Roman(3181), Roman(3187), Roman(3191), Roman(3203), Roman(3209), Roman(3217),
                            Roman(3221), Roman(3229), Roman(3251), Roman(3253), Roman(3257), Roman(3259), Roman(3271),
                            Roman(3299), Roman(3301), Roman(3307), Roman(3313), Roman(3319), Roman(3323), Roman(3329),
                            Roman(3331), Roman(3343), Roman(3347), Roman(3359), Roman(3361), Roman(3371), Roman(3373),
                            Roman(3389), Roman(3391), Roman(3407), Roman(3413), Roman(3433), Roman(3449), Roman(3457),
                            Roman(3461), Roman(3463), Roman(3467), Roman(3469), Roman(3491), Roman(3499), Roman(3511),
                            Roman(3517), Roman(3527), Roman(3529), Roman(3533), Roman(3539), Roman(3541), Roman(3547),
                            Roman(3557), Roman(3559), Roman(3571), Roman(3581), Roman(3583), Roman(3593), Roman(3607),
                            Roman(3613), Roman(3617), Roman(3623), Roman(3631), Roman(3637), Roman(3643), Roman(3659),
                            Roman(3671), Roman(3673), Roman(3677), Roman(3691), Roman(3697), Roman(3701), Roman(3709),
                            Roman(3719), Roman(3727), Roman(3733), Roman(3739), Roman(3761), Roman(3767), Roman(3769),
                            Roman(3779), Roman(3793), Roman(3797), Roman(3803), Roman(3821), Roman(3823), Roman(3833),
                            Roman(3847), Roman(3851), Roman(3853), Roman(3863), Roman(3877), Roman(3881), Roman(3889),
                            Roman(3907), Roman(3911), Roman(3917), Roman(3919), Roman(3923), Roman(3929), Roman(3931),
                            Roman(3943), Roman(3947), Roman(3967), Roman(3989)]

        assert list(Roman.prime_generator()) == expected_numbers

    ### Invertibility test
    def test_invertible(self):
        """ Tests that the conversion to Roman numerals is invertible, i.e.
        converting to Roman and back to decimal should yield the same numbers """
        romans = []
        decimals = []

        for i in range(4000):
            romans.append(Roman.convert_to_roman(i))

        for r in romans:
            decimals.append(Roman.convert_to_decimal(r))

        assert decimals == list(range(4000))

    ### Decorator test
    def test_invalid_decorator_use(self):
        """ Tests that the *validated* decorator raises the appropriate exception if incorrectly applied """
        with pytest.raises(RomanNumeralTypeError) as e:
            @validated
            def test(l: List[int]):
                print(l)

            test([1, 2, 3])

        err_msg = "The representation of the Roman numeral must be in str or int format (Given: <class 'list'>)"
        assert str(e.value) == err_msg

        with pytest.raises(RomanNumeralValueError) as e:
            @validated
            def test(s: str):
                print(s)

            test('XXXX')

        err_msg = 'Characters cannot be repeated more than 3 times in one succession (Repeated "X" too many times)'
        assert str(e.value) == err_msg

    ### Tests for the coroutines
    @pytest.mark.asyncio
    async def test_producer(self):
        ''' Tests that the producer coroutine yields the Roman Fibonacci numbers '''
        queue = asyncio.Queue()
        await Roman.producer(queue)

        # Assert that the queue contains the expected numbers
        for r in Roman.fibonacci_generator():
            assert await queue.get() == r
        assert await queue.get() is None

    @pytest.mark.asyncio
    async def test_consumer(self):
        ''' Tests that the consumer coroutine returns the prime Roman numbers found in the queue '''
        queue = asyncio.Queue()

        # Put some items into the queue
        for i in range(1, 50):
            await queue.put(Roman(i))
        await queue.put(None)

        result = await Roman.consumer(queue)

        # Assert that the consumer returned the expected numbers
        expected = [Roman(2), Roman(3), Roman(5), Roman(7), Roman(11), Roman(13), Roman(17), Roman(19),
                    Roman(23), Roman(29), Roman(31), Roman(37), Roman(41), Roman(43), Roman(47)]

        assert result == expected
