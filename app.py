import db
import gui as g
import operation as o


def run():
    print('Это консольное приложения для напсиания заметок')
    print()
    while True:
        o.hello()
        command = g.get_command()
        match command:
            case "w":
                data = g.write_all()
                db.save_in_file(data)
            case "ra":
                db.read_all()
            case "r":
                data = g.write_name()
                db.read_note(data)
            case "d":
                print('d ещё не написан')
            case "e":
                break
            case _:
                print('Такой команды у меня нет')


def hello() -> object:
    print('Hi!')
