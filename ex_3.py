"""
3 Функция принимает на вход список целых чисел и список операций: square, count_positive, filter_zero, minus_one

square - возвести каждое число в списке в квадрат
count_positive - посчитать количество положительных чисел
filter_zero - убрать из списка нули
minus_one - вычесть из каждого числа в списке единицу

Задача: применить список операций к списку чисел

Важно:

а) список операций может быть пустым
б) необходимо учесть порядок операций, например если дан список: [square, minus_one] и числа [1, 2, 3] то результатом
будет: [0, 3, 8], но если [minus_one, square] то результатом будет: [0, 1, 4]
в) список операций может содержать повторяющиеся операции, например: [square, square]
"""


def square(array: list[int]):
    for element in array:
        yield element * element


def count_positive(array: list[int]):
    counter = 0
    for element in array:
        if element:
            counter += 1
        yield element
    print(f'Positive values: {counter}')


def filter_zero(array: list[int]):
    for element in array:
        if not element:
            continue
        yield element * element


def minus_one(array: list[int]):
    for element in array:
        yield element - 1


gen_catalog = {'square': square, 'minus_one': minus_one, 'filter_zero': filter_zero, 'count_positive': count_positive}


def bitch_do_the_math(operations: list[str], nums: list[int]):
    # Тут переебывается поданный на вход список nums, если этого нужно избежать можно сделать copy
    generators = [gen_catalog[op] for op in operations]

    for gen in generators:
        gen = gen(nums)
        nums = [el for el in gen]

    return nums


if __name__ == '__main__':
    assert bitch_do_the_math(['square', 'minus_one'], [1, 2, 3]) == [0, 3, 8]
    assert bitch_do_the_math(['minus_one', 'square'], [1, 2, 3]) == [0, 1, 4]
    assert bitch_do_the_math(['square', 'square'], [1, 2, 3]) == [1, 16, 81]
