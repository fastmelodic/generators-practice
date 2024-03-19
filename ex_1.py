from copy import copy

"""
Убрать повторяющиеся элементы из списка - сделать для этого генератор, внутри генератора можно использовать множество
"""


def list_cleaner(obj: list):
    static_obj = copy(obj)
    values_store = set()

    for value in static_obj:
        if value in values_store:
            obj.remove(value)
            yield
        else:
            values_store.add(value)


if __name__ == '__main__':
    obj = [1, 1, 2, 2, 2, 3, 5, 23, 23, 546]
    gen = list_cleaner(obj)

    next(gen)
    assert obj == [1, 2, 2, 2, 3, 5, 23, 23, 546]

    next(gen)
    assert obj == [1, 2, 2, 3, 5, 23, 23, 546]

    next(gen)
    assert obj == [1, 2, 3, 5, 23, 23, 546]

    next(gen)
    assert obj == [1, 2, 3, 5, 23, 546]
