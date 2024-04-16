import csv

"""
В файле записано выражение, содержащее только числа (от 0 до 1_000_000)
и операции + и * например: 1+2*3+2+2*3*100*4+1032
Задача: считать выражение из файла и вычислить его, ответ записать в другой файл
"""


def csv_value_generator():
    # Контекстный менеджер открыт до конца прохождения по генератору - как лучше и быстрее?
    # каждый раз при обращении открывать и закрывать?
    with open('resource.csv', newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            for eq in row:
                yield eq


def solve_and_save():
    resource_data = csv_value_generator()

    for row in resource_data:
        # Тут наоборот каждый раз открывает и закрывается, как лучше хз.
        # Копить где-то чтобы потом залить разом - можно вытечь к хуям
        with open('result.csv', 'a', newline='') as csvfile:
            data = csv.writer(csvfile, delimiter=',')
            data.writerow([eval(row)])


if __name__ == '__main__':
    f = open('result.csv', 'w+')
    f.close()

    solve_and_save()

    f = open('result.csv', 'r')
    assert f.read() == '3441\n3341\n5628\n'
