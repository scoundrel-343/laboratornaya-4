def get_number_word(number):
    units = ['', 'один', 'два', 'три', 'четыре', 'пять',
             'шесть', 'семь', 'восемь', 'девять', 'десять',
             'одиннадцать', 'двенадцать', 'тринадцать',
             'четырнадцать', 'пятнадцать', 'шестнадцать',
             'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['', 'десять', 'двадцать', 'тридцать', 'сорок',
            'пятьдесят', 'шестьдесят', 'семьдесят',
            'восемьдесят', 'девяносто']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста',
                'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']

    if number == 0:
        return 'ноль'

    if number < 20:
        return units[number]

    if number < 100:
        return tens[number // 10] + ' ' + units[number % 10]

    if number < 1000:
        if number % 100 == 0:
            return hundreds[number // 100]
        else:
            return hundreds[number // 100] + ' ' + get_number_word(number % 100)
    
    if number < 100000:
        if number < 10000:
            if (number // 1000) == 1:
                hundreds_word = 'одна тысяча '
            elif (number // 1000) == 2:
                hundreds_word = 'две тысячи '
            elif (number // 1000) == 3:
                hundreds_word = 'три тысячи '
            elif (number // 1000) == 4:
                hundreds_word = 'четыре тысячи '
            else:
                hundreds_word = units[(number // 1000) % 10] + ' тысяч '

            if number % 1000 == 0:
                return hundreds_word
            else:
                return hundreds_word + get_number_word(number % 1000)
        else:
            if (number // 1000) % 10 == 1:
                hundreds_word = 'одна тысяча '
            elif (number // 1000) % 10 == 2:
                hundreds_word = 'две тысячи '
            elif (number // 1000) % 10 == 3:
                hundreds_word = 'три тысячи '
            elif (number // 1000) % 10 == 4:
                hundreds_word = 'четыре тысячи '
            else:
                hundreds_word = units[(number // 1000) % 10] + ' тысяч '

            if number % 10000 == 0:
                return tens[number // 10000] + ' тысяч '
            else:
                return get_number_word(int(str(number // 1000)[0] + '0')) + hundreds_word + get_number_word(number % 1000)

    if number == 100000:
        return 'сто тысяч'
        

def get_currency_word(number):
    if 10 < number % 100 < 20:
        return 'рублей'

    if number % 10 == 1:
        return 'рубль'

    if 1 < number % 10 < 5:
        return 'рубля'

    return 'рублей'

# Получаем данные от пользователя
while True:
    try:
        number = int(input("Введите число от 1 до 100000: "))
        if 1 <= number <= 100000:
            break
        else:
            print("Число должно быть от 1 до 100000. Попробуйте еще раз.")
    except ValueError:
        print("Некорректный ввод. Попробуйте еще раз.")

# Преобразуем число в слова
number_word = get_number_word(number)

# Определяем правильное окончание для валюты
currency_word = get_currency_word(number)

# Выводим на экран результат
print(number, "-", number_word, currency_word)