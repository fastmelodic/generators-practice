"""
Убрать повторяющиеся элементы из списка - сделать для этого генератор, внутри генератора можно использовать множество
"""


def list_cleaner(obj: list) -> int:
    converted_obj = sorted(list(set(obj)))
    #  без sorted, когда переводится в set, то сука 546 идет раньше 5 какого то хуя {1,2,3,546,6,23}

    for value in converted_obj:
        yield value


if __name__ == '__main__':
    obj = [1, 1, 2, 2, 2, 3, 5, 23, 23, 546]
    gen = list_cleaner(obj)

    assert next(gen) == 1
    assert next(gen) == 2
    assert next(gen) == 3
    assert next(gen) == 5
    assert next(gen) == 23
    assert next(gen) == 546
