def fizzbuzz_resolver(value: int):
    if not isinstance(value, int):
        return {'ValueError': 'value param must be a integer'}, 400
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

