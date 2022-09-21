

def name(doc, number1):
    """выводит имя по номеру документа"""
    # number = input("введите номер документа ")
    for item in doc:
        if number1 == item['number']:
            print(item['name'])
            return item['name']
    return "Документа с таким номером не существует"


def shelf(dir, number):
    """выводит номер полки по номеру документа"""
    # number = input("введите номер документа ")
    for shelf_no, num in dir.items():
        for i in num:
            if i == number:
                print(shelf_no)
                return shelf_no
    print("Документа с таким номером не существует")



def add(doc, dir, number, type, name, shelf):
    """добавляет документ в каталог и перечень полок"""
    # number = input("введите иномер ")
    # type = input('введите тип документа ')
    # name = input('введите имя ')
    # shelf = input('введите номер полки ')
    # print()
    exist = False
    dict = {"type": type, "number": number, "name": name}
    doc.append(dict)
    for number_shelf, num in dir.items():
        if number_shelf == shelf:
            num.append(number)
            exist = True
    if exist == False:
        print("Вы ввели несуществующий номер полки")
    # print(doc, dir)
    return doc, dir


def list(doc):
    """выводит список всех документов"""

    all_docs = []
    for i in doc:
        type = i['type']
        number = i['number']
        name = i['name']
        result = f"{type}, {number}, {name}"
        all_docs.append(result)
    print(all_docs)
    return all_docs


# ________ Задача №2. Дополнительная______________

def delete(doc, dir, number):
    """Удаляет"""
    # number = input('Введите номер докуента ')
    doc_exist = False
    dir_exist = False
    doc_copy = doc.copy()
    for item in doc_copy:
        if number == item['number']:
            doc.remove(item)
            doc_exist = True
    if doc_exist == True:
        print(doc)
    else:
        print('Документа в каталоге с таким номером не существует')

    dir_copy = dir.copy()
    for shelf_no, num in dir_copy.items():
        for i in num:
            if number == i:
                num.remove(number)
                dir_exist = True
    if dir_exist == True:
        print(dir)
    else:
        print('Документа на полках с таким номером не существует')
    return(doc, dir)

def move(dir):
    """Перемещает"""
    number = input('Введите номер документа ')
    shelf = input('Введите номер целевой полки ')
    exist_number = False
    exist_shelf = False
    dir_copy = dir.copy()

    for shelf_no, num in dir_copy.items():
        if shelf_no == shelf:
            exist_shelf = True
    if exist_shelf == False:
        print('Полки с таким номером не существует')
        return
    for shelf_no, num in dir_copy.items():
        for i in num:
            if number == i:
                num.remove(number)
                dir[shelf] = [number]
                exist_number = True
    if exist_number == True:
        print(dir)
    else:
        print('Документа на полках с таким номером не существует')


def add_shelf(dir):
    """Добавляет полку"""
    new_shelf = input('Введите номер новой полки ')
    for shelf_no, num in dir.items():
        if shelf_no == new_shelf:
            print('Полка с таким номером уже существует')
            print(dir)
            return
    dir[new_shelf] = []
    print(dir)


# _________________________________________________


def main(documents, directories):
    while True:
        command = input("введите команду ")

        if command == "p":
            print(name(documents))
            print()

        elif command == "s":
            shelf(directories)

        elif command == "l":
            list(documents)

        elif command == "a":
            add(documents, directories)
            for i in documents:
                print(i)
            print()
            for shelf_no, number in directories.items():
                print(f'{shelf_no}: {number}')

        # ------Задача 2. Дополнительная---------------

        elif command == "d":
            delete(documents, directories)

        elif command == "m":
            move(directories)

        elif command == "as":
            add_shelf(directories)

        # -------------------------------------------------

        elif command == 'q':
            print('Выход')
            return

        else:
            print("Hеверная команда!")


if __name__ == '__main__':

    documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]

    directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
    }

    # main(documents, directories)

