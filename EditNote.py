import json
from _datetime import datetime as dt
class EditNote:
    def __init__(self, nameFile):
        self.__nameFile = nameFile


    def read_file(self):
        file_json = open(self.__nameFile, 'r', encoding='utf-8' )
        return json.loads(file_json.read())


    def add_note(self):
        print(self.__nameFile)
        idtemp = self.get_id() + 1
        new_note = {
            "id": int(idtemp),
            "header": self.input_header(),
            "body": self.input_body(),
            "date": (self.get_dateTime()).strftime("%d-%m-%Y %H:%M:%S")
        }
        return new_note

    def save_note(self, new_data):
        mylist = self.read_file()
        mylist["notes"].append(new_data)
        #print(mylist)
        file_json = open(self.__nameFile, 'w', encoding='utf-8')
        json.dump(mylist, file_json, ensure_ascii=False)


    def input_header(self):
        return input('Ваедите название заметки: ')

    def input_body(self):
        return input('Ваедите текст заметки: ')

    def get_dateTime(self):
        return dt.now()
    def get_id(self):
        last_id = 0
        for item in self.read_file()['notes']:
            for key, value in item.items():
                if key == 'id':
                    if last_id < value:
                        last_id = value
        return last_id




    def print_note(self, data):
         #for item in data:
             for key, value in data.items():
                 if type(value) == list:
                     print(key, ':', ','.join(value))
    
                 if type(value) == dict:
                    print(key, ':')
                    for k, v in value.items():
                        print(k, v)
                 else:
                     print(key, ':', value)
    
             print()

