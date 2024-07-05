# Задача "План перехват":

# Напишите 2 функции:
# Функция personal_sum(numbers):
# 1. Должна принимать коллекцию numbers.
# 2. Подсчитывать  сумму чисел в numbers путём перебора и увеличивать переменную result.
# 3. Если же при переборе встречается данное типа отличного от числового, то обработать исключение TypeError,
#    увеличив счётчик incorrect_data на 1.
# 4. В конечном итоге функция возвращает кортеж из двух значений: result - сумма чисел,
#    incorrect_data - кол-во некорректных данных.

# Функция calculate_average(numbers)
# Среднее арифметическое - сумма всех данных делённая на их количество.
# 1. Должна принимать коллекцию numbers и возвращать: среднее арифметическое всех чисел.
# 2. Внутри для подсчёта суммы используйте функцию personal_sum написанную ранее.
# 3. Т.к. коллекция numbers может оказаться пустой, то обработайте исключение ZeroDivisionError при делении
#    на 0 и верните 0.
# 4. Также в numbers может быть записана не коллекция, а другие типы данных, например числа. Обработайте
#    исключение TypeError выводя строку 'В numbers записан некорректный тип данных'. В таком случае
#    функция просто вернёт None.

# Пункты задачи:
# 1. Создайте функцию personal_sum на основе условий задачи.
# 2. Создайте функцию calculate_average на основе условий задачи.
# 3. Вызовите функцию calculate_average несколько раз, передав в неё данные разных вариаций.

def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
    return (result, incorrect_data)

def calculate_average(numbers):
    try:
        summ_ = personal_sum(numbers)
        summ = summ_[0]
    except TypeError as exe:
        print(f'В numbers записин некорректный тип данных: {exe}')
        return None
    try:
        mid = summ / (len(numbers)-summ_[1])
    except ZeroDivisionError:
        return 0

    return mid

y = (1, 2, 3, 4, 5)
print(calculate_average(y))
y = (1, 2, 3, 4, '5')
print(calculate_average(y))
y = 1
print(calculate_average(y))
y = [10, 10, '10', '10']
print(calculate_average(y))
y = ['10', '10']
print(calculate_average(y))