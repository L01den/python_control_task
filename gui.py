def get_command():
    act = str(input('Выбирте действие: '))
    print('')
    return act


def write_all():
    name = str(input('Введите название заметки: '))
    note = str(input('Текст заметки: '))
    print('')
    data = [name, note]
    return data

def write_name():
    name = str(input('Введите название заметки: '))
    print('')
    return name