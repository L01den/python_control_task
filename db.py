import json
import os
from datetime import datetime

ID = 0


def save_in_file(data: list):
    date_now = datetime.now()
    global ID 
    ID += 1
    new_data = dict(id = ID, Name=data[0], Text=data[1], Date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    if os.path.isfile('db.json') is False:
        with open('db.json', 'w', encoding='utf-8') as f:
            json.dump([new_data, ], f, indent=2)
        print("Data created")
    
    # date_now = datetime.now()
    # new_data = {
    #     'Name': new_data[0],
    #     'Text': new_data[1]
    #     # 'Date': date_now
    # }
    with open('db.json', encoding='utf8') as f:
        all_data = json.load(f)
        all_data.append(new_data)
        with open('db.json', 'w', encoding='utf8') as outfile:
            json.dump(all_data, outfile, ensure_ascii=False, indent=2)
    print('Сохранение успешно')


def read_all():
    with open('db.json', encoding='utf8') as file:
        data = json.load(file)
        for p in data:
            print('Name: ' + p['Name'])
            


def read_note(name):
    with open('db.json', encoding='utf8') as file:
        data = json.load(file)
        for p in data:
            if(p['Name'] == name):
                print('Name: ' + p['Name'])
                print('Text: ' + p['Text'])
                print('')
            
