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
        self.print_heders(dictNotes)
        list = self.search_note(False)
        #headerNote = self.input_text('Ваедите название заметки, которую хотите открыть: ')
        #listNotes = dictNotes['notes']




    def search_note(self, flag):
        '''print(
            'Возможные варианты поиска: \n'
            '1. По названию \n'
            '2. По тексту заметки \n'
            '3. По дате'
        )

        var = input('Выберите вариант действий: ')
        while var not in ('1', '2', '3'):
            print('Некоректный ввод!')
            var = input('Выберите вариант действий: ')
        i_var = int(var) - 1
        '''
        search = input('Введите данные для поиска: ')
        listNotes = self.read_file()['notes']
        #print((listNotes))

        for note in listNotes:
            if search in note.values():
                return note
        return {}
                #self.print_note(note)


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



