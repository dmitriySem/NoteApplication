# This is a sample Python script.
import json

import EditNote


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #login = input('Ваедите логин пользователя: ')
    login = 'user1'
    N = EditNote.EditNote('./'+ login + '.json')
    N.edit_note()

    #print(N.search_note())
    #N.print_notes(N.read_file())
    #N.save_note(N.create_note())
    '''
    data = {
        "president": {
            "name": "Zaphod Beeblebrox",
            "species": "Betelgeusian"
        }
    }
    # print(data.get("president").get("name"))
    with open("user1.json", "w") as write_file:
       #json.dump(data, write_file)
       json_string = json.dumps(data)
    '''



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
