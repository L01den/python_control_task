def hello():
    print('''   Меню:
        Добавить запись - w
        Вывести названия всех заметок - ra
        Вывести заметку по названию - r
        Дописать заметку - m
        Вывети все заметки от даты - g
        Удалить заметку - d
        Выход - e
    ''')


def get_command():
    act = str(input('Выбирте действие: '))
    print()
    return act


def write_note():
    note = str(input('Текст заметки: '))
    print()
    return note

def write_name():
    name = str(input('Введите название заметки: '))
    print()
    return name

def write_date():
    name = str(input('Введите дату в формате 2000-12-31: '))
    print()
    return name