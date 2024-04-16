"""
2 Написать бесконечный генератор чисел def next_num() -> int, использовать метод send(),
а про close() и throw() - просто почитать

Число seed - старт последовательности

Пример последовательности вызовов генератора:

next_num() —> 1
next_num() —> 2
next_num(10) —> 11
next_num() —> 12
next_num(3) —> 4
next_num() —> 5
next_num() —> 6
next_num() —> 7
next_num() —> 8
"""


def num_generator():
    num = 0
    while True:
        seed = yield
        if seed:
            num = seed
        num += 1
        yield num


gen_instance = num_generator()


def next_num(seed: int = None):
    next(gen_instance)
    return gen_instance.send(seed)


if __name__ == '__main__':
    assert next_num() == 1
    assert next_num() == 2
    assert next_num(10) == 11
    assert next_num() == 12
    assert next_num(3) == 4
    assert next_num() == 5
    assert next_num() == 6
    assert next_num() == 7
    assert next_num() == 8
