import json
from _datetime import datetime as dt
class EditNote:
    def __init__(self, nameFile):
        self.__nameFile = nameFile


    def read_file(self):
        file_json = open(self.__nameFile, 'r', encoding='utf-8' )
        return json.loads(file_json.read())


    def create_note(self):
        print(self.__nameFile)
        idtemp = self.get_id() + 1
        new_note = {
            "id": int(idtemp),
            "header": self.input_text('Ваедите название заметки: '),
            "body": self.input_text('Ваедите текст заметки: '),
            "date": (self.get_dateTime()).strftime("%d-%m-%Y %H:%M:%S")
        }
        return new_note
    def add_note(self, note):
        dictNotes = self.read_file()
        dictNotes["notes"].append(note)
        #print("Словарь")
        #print(dictNotes)
        return dictNotes


    def save_note(self, note):
        dictNotes = self.add_note(note)
        #print(dictNotes)
        file_json = open(self.__nameFile, 'w', encoding='utf-8')
        json.dump(dictNotes, file_json, ensure_ascii=False)

    def print_notes(self, notes):
        if type(notes) == list:
            for note in notes:
                print('Заметка: {} \n \t{} \n'.format(note['header'], note['body']))

        if type(notes) == dict:
            for note in notes["notes"]:
                print('Заметка: {} \n \t{} \n'.format(note['header'], note['body']))

    def print_heders(self, notes):
        if type(notes) == list:
            for note in notes:
                print('Заметка: {}'.format(note['header']))

        if type(notes) == dict:
            for note in notes["notes"]:
                print('Заметка: {}'.format(note['header']))
    def print_note(self, note):
        print('Заметка: {} \n \t{} \n'.format(note['header'], note['body']))


    def read_note(self):
        dictNotes = self.read_file()
        list = self.search_note()
        return list





    def search_note(self):
        print(
            'Возможные варианты поиска: \n'
            '1. По названию \n'
            '2. По тексту заметки \n'
            '3. По дате'
        )
        listNotes = self.read_file()['notes']
        var = input('Выберите вариант действий: ')
        while var not in ('1', '2', '3'):
            print('Некоректный ввод!')
            var = input('Выберите вариант действий: ')

        list = []
        match var:
            case "1":
                search = input('Введите название заметки для поиска: ')
                for note in listNotes:
                    if search in note["header"]:
                        list.append(note)
                if (len(list) > 1 and len(list) != 0 ):
                    print("Нашлось несколько заметок, укажите необходимую заметку")
                    self.__correct_search(list)
                    return list
                else:
                    return list
                #return list
            case "2":
                search = input('Введите содержимое заметки для поиска: ')
                for note in listNotes:
                    if search in note["body"]:
                        list.append(note)
                if (len(list) > 1 and len(list) != 0):
                    print("Нашлось несколько заметок, укажите необходимую заметку")
                    self.__correct_search(list)
                    return list
                else:
                    return list
                 #       return note
            case "3":
                search = input('Введите дату (в формате dd-mm-yyyy)  создания или изменения заметки для поиска: ')
                list = []
                for note in listNotes:
                    if search in note["date"]:
                        list.append(note)
                if (len(list) > 1 and len(list) != 0 ):
                    print("Нашлось несколько заметок, укажите необходимую заметку")
                    self.__correct_search(list)
                    return list
                else:
                    return list

        if(len(list) == 0):
            print("Заметки с указанными параметрами не нашлись")
            return []
        else:
            return list
                #self.print_note(note)

    def __correct_search(self, list):
        for i in range(len(list)):
            print("Заметка №{}".format(i))
            self.print_note(list[i])
            # self.print_heders(list[0])
        return list[int(input("Введите номер заметки:"))]

    def remove_note(self, note):
        notes = self.read_file()
        #print(note['header'])
        notes['notes'] = list(filter(lambda x: x.get('header') != note['header'], notes.get('notes', [])))
        file_json = open(self.__nameFile, 'w', encoding='utf-8')
        return json.dump(notes, file_json, ensure_ascii=False)


    def edit_note(self):
        print("Укажите какую заметку нужно отредактировать")
        note = self.search_note()[0]
        self.remove_note(note)
        while(True):
            flag_header = input("Нужно отредактировать заголовок? Да/Нет\n").lower()
            if (flag_header.__eq__("да") or flag_header.__eq__("yes") or flag_header.__eq__("y") or flag_header.__eq__("lf") or flag_header.__eq__("нуы") or flag_header.__eq__("д")):
                note["header"] = input("Укажите новый заголовок заметки: ")
                note["date"] = (self.get_dateTime()).strftime("%d-%m-%Y %H:%M:%S")

            flag_body = input("Нужно отредактировать текст заметки? Да/Нет \n").lower()
            if (flag_body.__eq__("да") or flag_body.__eq__("yes") or flag_body.__eq__("y") or flag_body.__eq__("lf") or flag_body.__eq__("нуы") or flag_body.__eq__("д")):
                note["body"] = input("Укажите новый текст заметки: ")
                note["date"] = (self.get_dateTime()).strftime("%d-%m-%Y %H:%M:%S")

            flag_cont = input("Хотите отредактировать измененную заметку? Да/Нет").lower()
            if (flag_cont.__eq__("нет") or flag_cont.__eq__("no") or flag_cont.__eq__("n") or flag_cont.__eq__("ytn") or flag_cont.__eq__("тщ") or flag_cont.__eq__("н")):
                self.save_note(note)
                break




    def input_text(self, strHeader):
        return input(strHeader)


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



