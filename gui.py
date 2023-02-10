

def get_command():
    act = str(input('Выбирте действие: '))
    return act


def write():
    name = str(input('Введите название заметки: '))
    note = str(input('Текст заметки: '))
    data = [name, note]
    return data
