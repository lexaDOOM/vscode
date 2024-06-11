def even_digit_count(number):
    if number % 1 != 0:
        return 0
    w = str(number)
    c = 0
    for i in range(len(w)):
        if w[i] == '.':
            break
        if int(w[i]) % 2 == 0:
            c += 1
    return c


num = float(input('Введите число >> '))
print('Кол-во чётных цифр в числе', even_digit_count(num))
