import db
import gui as g


def run():
    print('Это консольное приложения для напсиания заметок')
    print()
    while True:
        g.hello()
        command = g.get_command()
        match command:
            case "w":
                name = g.write_name()
                note = g.write_note()
                db.save_in_file(name, note)
            case "ra":
                db.read_all()
            case "r":
                data = g.write_name()
                db.read_note(data)
            case "d":
                data = g.write_name()
                db.delite_note(data)
            case "m":
                name = g.write_name()
                note = g.write_note()
                db.mod_note(name, note)   
            case "g":
                date = g.write_date()
                db.search_by_date(date)     
            case "e":
                break
            case _:
                print('Такой команды у меня нет')


def hello() -> object:
    print('Hi!')
