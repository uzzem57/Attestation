import operation
import note
import int

number = 6  # сколько знаков МИНИМУМ может быть в тексте заметки


def add():
    note = int.create_note(number)
    array = operation.read_file()
    for notes in array:
        if note.Note.get_id(note) == note.Note.get_id(notes):
            note.Note.set_id(note)
    array.append(note)
    operation.write_file(array, 'a')
    print('Заметка добавлена...')


def show(text):
    logic = True
    array = operation.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in note.Note.get_date(notes):
                print(note.Note.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки...')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = operation.read_file()
    logic = True
    for notes in array:
        if id == note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = int.create_note(number)
                note.Note.set_title(notes, note.get_title())
                note.Note.set_body(notes, note.get_body())
                note.Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(note.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    operation.write_file(array, 'a')