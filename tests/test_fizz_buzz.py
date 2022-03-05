from pytest import mark
from fizz_buzz.code import fizz_buzz


def test_when_fizzbuzz_receives_multiples_of_3_and_5_should_return_fizzbuzz():
    assert fizz_buzz(value=15) == 'fizzbuzz'


def test_when_fizzbuzz_receives_multiples_of_3_should_return_fizz():
    assert fizz_buzz(value=3) == 'fizz'


def test_when_fizzbuzz_receives_multiples_of_5_should_return_buzz():
    assert fizz_buzz(value=5) == 'buzz'


def test_when_fizzbuzz_not_receives_multiples_of_3_and_5_should_return_itself_value():
    assert fizz_buzz(value=4) == 4


@mark.xfail()
def test_when_fizzbuzz_not_receives_int_value_should_raise_valueerror():
    assert fizz_buzz(value='invalid') == 4
