# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os


migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

files_dir = os.path.join(current_dir, migrations)
files_type = ".sql"

filelist = []


def get_text_from_file(full_file_name):
    with open(full_file_name, encoding='utf-8') as f:
        text = f.read()
    return text

def print_finded_files(filelist):
    i = 0
    for file_name in os.listdir(path=files_dir):  
        full_file_name = os.path.join(files_dir, file_name)
        if file_name.endswith(files_type) and user_input in get_text_from_file(full_file_name):
            filelist.append(file_name)
            i += 1
            print(file_name + "\n") 
    print("Всего: " + str(i) + "\n")   
    return filelist      


if __name__ == '__main__':
    while True:
        user_input = input("Введите строку:")
        print_finded_files(filelist)
