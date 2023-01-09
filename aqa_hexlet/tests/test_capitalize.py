from capitalize import capitalize

assert capitalize('hello') != 'Hello':


if capitalize('') != '':
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!'