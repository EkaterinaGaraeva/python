# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


def add_contact(f):
    input_name = input('Введите Имя: ')
    input_last_name = input('Введите Фамилию: ')
    input_phone = input('Введите номер телефона: ')
    data = f'{input_last_name}; {input_name}; {input_phone}'
    with open(f, 'a', encoding='utf-8') as fd:
        fd.write(f'{data}\n')
    print(f'Запись {data} добавлена')


def read_all(f):
    with open(f, 'r', encoding='utf-8') as fd:
        file_list = fd.readlines()
        return file_list


def print_all(f):
    adr_book = read_all(f)
    for line in adr_book:
        line = line.replace(';', '')
        line = line.replace('\n', '')
        print(line)


def search_contact(f):
    print('Выберите тип данных для поиска:')
    user_choice = input('1 - фамилия,\n2 - имя,\n'
                        '3 - номер телефона\n-> ')
    adr_book = read_all(f)
    if user_choice == '1':
        last_name = input('Введите фамилию для поиска: ')
        for i in range(len(adr_book)):
            last_name_in_adr_book, name_in_adr_book, phone_in_adr_book = adr_book[i].split('; ')
            if last_name == last_name_in_adr_book:
                print(i, adr_book[i].replace(';', '').replace('\n', ''))
    elif user_choice == '2':
        name = input('Введите имя для поиска: ')
        for i in range(len(adr_book)):
            last_name_in_adr_book, name_in_adr_book, phone_in_adr_book = adr_book[i].split('; ')
            if name == name_in_adr_book:
                print(i, adr_book[i].replace(';', '').replace('\n', ''))
    elif user_choice == '3':
        phone = input('Введите номер телефона для поиска: ')
        for i in range(len(adr_book)):
            last_name_in_adr_book, name_in_adr_book, phone_in_adr_book = adr_book[i].split('; ')
            if phone == phone_in_adr_book:
                print(i, adr_book[i].replace(';', '').replace('\n', ''))


def replace_contact(f):
    adr_book = read_all(f)
    search_contact(f)
    idx = int(input('Введите индекс для замены: '))
    print('Выберите тип данных для замены:')
    user_choice = input('1 - фамилия,\n2 - имя,\n'
                        '3 - номер телефона\n-> ')
    if user_choice == '1':
        new_last_name = input('Введите новую фамилию: ')
        _, name, phone = adr_book[idx].split('; ')
        new_record = f'{new_last_name}; {name}; {phone}\n'
    elif user_choice == '2':
        new_name = input('Введите новое имя: ')
        last_name, _, phone = adr_book[idx].split('; ')
        new_record = f'{last_name}; {new_name}; {phone}\n'
    elif user_choice == '3':
        new_phone = input('Введите новый номер телефона: ')
        last_name, name, _ = adr_book[idx].split('; ')
        new_record = f'{last_name}; {name}; {new_phone}\n'
    adr_book[idx] = new_record
    with open(f, 'w', encoding='utf-8') as fd:
        fd.writelines(adr_book)


def delete_contact(f):
    adr_book = read_all(f)
    search_contact(f)
    idx = int(input('Введите индекс для удаления контакта: '))
    adr_book.pop(idx)
    with open(f, 'w', encoding='utf-8') as fd:
        fd.writelines(adr_book)


def main():
    # user_choice = ''
    # while user_choice != 'z':
    file = 'address_book.txt'
    while True:
        user_choice = input('1 - добавить запись,\n2 - прочитать всю тел.книгу,\n'
                            '3 - найти запись,\n4 - заменить запись,\n5 - удалить запись,\n'
                            'z - для выхода\n-> ')
        if user_choice == '1':
            add_contact(file)
        elif user_choice == '2':
            print_all(file)
        elif user_choice == '3':
            search_contact(file)
        elif user_choice == '4':
            replace_contact(file)
        elif user_choice == '5':
            delete_contact(file)
        elif user_choice == 'z':
            print('Всего хорошего')
            break


if __name__ == '__main__':
    main()

