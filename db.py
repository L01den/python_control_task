import json
import datetime


def save_in_file(data: list):
    date_now = datetime.datetime.now()
    dict = {}
    dict['note'] = []
    dict['note'].append({
        'Name': data[0],
        'Text': data[1],
        # 'Date': date_now
    })
    with open('db.json', 'w') as outfile:
        json.dump(dict, outfile)
    print('Сохранение успешно')


def read_all():
    with open('db.json') as json_file:
        dict = json.load(json_file)
        for p in dict['note']:
            print('Name: ' + p['Name'])
            print('')


def read_note():
    with open('db.json') as json_file:
        dict = json.load(json_file)
        for p in dict['note']:
            print('Name: ' + p['Name'])
            print('Text: ' + p['Text'])
            # print('Date: ' + p['Date'])
            print('')
