def fizz_buzz_resolver(value: int):
    if value % 3 == 0 and value % 5 == 0:
        return 'fizzbuzz'
    elif value % 3 == 0:
        return 'fizz'
    elif value % 5 == 0:
        return 'buzz'
    else:
        return value

#
# var = fizz_buzz(value=4)
# print(var)
