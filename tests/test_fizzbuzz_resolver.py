from pytest import mark, raises
from fizz_buzz.fizzbuzz_resolver import fizzbuzz_resolver


@mark.parametrize('input_value', [15, 30, 45, 60])
def test_when_fizzbuzz_receives_multiples_of_3_and_5_should_return_fizzbuzz(input_value):
    assert fizzbuzz_resolver(value=input_value) == 'fizzbuzz'


@mark.parametrize('input_value', [3, 6, 9, 12])
def test_when_fizzbuzz_receives_multiples_of_3_should_return_fizz(input_value):
    assert fizzbuzz_resolver(value=input_value) == 'fizz'


@mark.parametrize('input_value', [5, 10, 20, 25])
def test_when_fizzbuzz_receives_multiples_of_5_should_return_buzz(input_value):
    assert fizzbuzz_resolver(value=input_value) == 'buzz'


@mark.parametrize('input_value', [1, 2, 43, 74])
def test_when_fizzbuzz_not_receives_multiples_of_3_and_5_should_return_itself_value(input_value):
    assert fizzbuzz_resolver(value=input_value) == input_value


# @mark.xfail()
def test_when_fizzbuzz_not_receives_int_value_should_raise_valueerror():
    with raises(ValueError):
        fizzbuzz_resolver(value='invalid')
