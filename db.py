import json
import os
from datetime import datetime

ID = 0


def save_in_file(name, note):
    global ID
    ID += 1
    new_data = dict(id=ID, Name=name, Text=note,
                    Create_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    if os.path.isfile('db.json') is False:
        with open('db.json', 'w', encoding='utf-8') as f:
            json.dump([new_data, ], f, indent=2)
        print('Data created\n')

    with open('db.json', encoding='utf8') as f:
        all_data = json.load(f)
        all_data.append(new_data)
        with open('db.json', 'w', encoding='utf8') as outfile:
            json.dump(all_data, outfile, ensure_ascii=False, indent=2)
    print('Сохранение успешно\n')


def read_all():
    with open('db.json', encoding='utf8') as f:
        data = json.load(f)
        for p in data:
            print('Name: ' + p['Name'])


def read_note(name):
    with open('db.json', encoding='utf8') as f:
        data = json.load(f)
        for p in data:
            if p['Name'] == name:
                print('Name: ' + p['Name'])
                print('Text: ' + p['Text'])
                print('')
                break
        else:
            print('Заметки с таким именем не найдено')


def mod_note(name, new_text):
    with open('db.json', encoding='utf8') as f:
        data = json.load(f)
        for p in data:
            if p['Name'] == name:
                new_text = p['Text'] + ' ' + new_text
                p['Text'] = new_text
                print('Заметка изменена\n')
                break
        else:
            print('Заметки с таким именем не найдено')    
        with open('db.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)

def search_by_date(date):
    with open('db.json', encoding='utf8') as f:
        data = json.load(f)
        for p in data:
            str = p['Create_date'].split(' ')
            if str[0] == date:
                print('Name: ' + p['Name'])
                print('Create_date: ' + p['Create_date'])
                print('')


def delite_note(name):
    with open('db.json', encoding='utf8') as f:
        data = json.load(f)
        item = 0
        for p in data:
            if p['Name'] == name:
                data.pop(item)
                print('Заметка удалена\n')
                break
            item += 1
        else:
            print('Заметки с таким именем не найдено')
        with open('db.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)
        
