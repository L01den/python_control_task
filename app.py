import db
import gui as g
import operation as o


def run():
# дописать описания программы
    while True:
        o.hello()
        command = g.get_command()
        match command:
            case "w":
                data = g.write()
                print(data)
            case "ra":
                print('ra ещё не написан')
            case "r":
                print('r ещё не написан')
            case "d":
                print('d ещё не написан')
            case "e":
                break
            case _:
                print('Такой команды у меня нет')



def hello() -> object:
    print('Hi!')
