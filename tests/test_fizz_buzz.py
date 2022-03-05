from fizz_buzz.code import fizz_buzz


def test_when_fizzbuzz_receives_multiples_of_3_should_return_fizz():
    assert fizz_buzz(value=3) == 'fizz'


def test_when_fizzbuzz_receives_multiples_of_5_should_return_buzz():
    assert fizz_buzz(value=5) == 'buzz'
