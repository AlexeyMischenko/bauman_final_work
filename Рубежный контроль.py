import csv
import os

list_of_notebooks = ['test.csv']


# Документация
def help():
    list_of_commands = ['Команда\tДействие', '', 'create\tСоздать блакнот', 'check\tПосмотреть блакнот', 'fix\tИзменить блакнот', 'delite\tУдалить блакнот', 'stop\tЗавершить работу']
    print('\n'.join(list_of_commands))
    return True


# Просмотр блакнотов
def check_notebooks():
    print('\n'.join(list_of_notebooks))
    return True


# Создание нового блакнота
def create_notebook(name):
    with open(name + '.csv', 'w', newline = '', encoding='UTF8') as file:
        f = csv.writer(file)
        list_of_notebooks.append(name)


def ByPriority(priority):
    if priority == 'Низкий':
        return 2
    elif priority == 'Средний':
        return 1
    elif priority == 'Высокий':
        return 0
    else:
        return 3


def ByStatus(status):
    if status.lower() in ['выполнен', 'выполнено', 'выполнена']:
        return 1
    return 0



# Сортировка
def Sort(Key, string):
    if Key == '4':
        m = [ByPriority(i[4]) for i in string]
        m_1 = sorted(list(map(list, list(zip(m, string)))), key=lambda x:x[0])
        m_2 = [i[1] for i in m_1]
        string = []
        for i in m_2:
            string.append(i)
        # string.sort(key=lambda x:x[4])
    elif Key == '1':
        string.sort(key=lambda x:x[0])
    elif Key == '2':
        string.sort(key=lambda x:x[3])
    elif Key == '3':
        string.sort(key=lambda x:x[2])
    elif Key == '5':
        m = [ByStatus(i[5]) for i in string]
        m_1 = sorted(list(map(list, list(zip(m, string)))), key=lambda x:x[0])
        m_2 = [i[1] for i in m_1]
        string = []
        for i in m_2:
            string.append(i)
        # string.sort(key=lambda x:x[5])
    return string


# Редактирование файла
def fix_notebook():
    name = input('Введите имя файла: ')
    string = []
    with open(name + '.csv', 'r', newline='', encoding='UTF8') as file_1:
        f_1 = csv.reader(file_1)
        for index in f_1:
            string.append(index)
    
    with open(name + '.csv', 'w', newline = '', encoding='UTF8') as file:
        f = csv.writer(file)
        print('Добавить - 1')
        print('Изменить - 2')
        print('Сортировать - 3')
        action_1 = input('Введите номер соответствующего действия: ')
        while action_1 not in '123':
            action_1 = input('Введите номер соответствующего действия: ')
        if action_1 == '1':
            string.append(input('Введите значения через запятую: ').split(','))
        elif action_1 == '3':
            print('По чему сортировать?\n')
            Key = input('Номер - 1\nДата - 2\nВремя - 3\nПриоритетность - 4\nСтатус - 5\n\n').capitalize()
            string = Sort(Key, string)
        else:
            # print(string)
            number = int(input('Введите номер строки: ')) - 1
            if number > len(string):
                print('Вы превысили лимит строк, попробуйте еще раз!')
            else:
                string[number] = input('Введите новые значения через запятую: ').split(',')
        for i in string:
            f.writerow(i)
            

# Удаление файла
def delite_notebook(file):
    if(os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)
        return 'Файл удалён!'
    return 'Файл не найден!'


# Основной цикл
action = input('Введите команду: ')
while action.lower() not in  ['стоп', 'stop', 'break', 'exit', 'finish', 'финиш']:
    if action.lower() in ['help', 'create', 'check', 'fix', 'delite']:
        if action == 'help':
            help()
        elif action == 'create':
            name = input('Введите имя файла: ')
            create_notebook(name)
        elif action == 'check':
            check_notebooks()
        elif action == 'fix':
            fix_notebook()
        else:
            fi = input('Введите имя файла: ') + '.csv'
            print(delite_notebook(fi))
    else:
        print('Вы ввели неверный код команды, попробуйте еще раз')
    action = input('Введите команду: ')


print('!!!Работа завершена!!!')
