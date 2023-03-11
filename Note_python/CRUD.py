import csv
import pathlib


def create_file():
    with open('csv_example_2.csv', 'r', encoding='utf-8') as rf:
        arr = list(rf)
        if len(arr) == 0:
            k = 0
        else:
            k = int(arr[len(arr) - 1][0])

    with open('csv_example_2.csv', 'a', encoding='utf-8', newline='\n') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter = ";")
        index = k + 1
        diction = {
            'head': input('Введите заголовок:'),
            'note': input('Введите текст заметки:'),
            'date': input('Введите дату и время.Например 10.03.2023/10:45:'),
        }
        csv_writer.writerow([index, diction["head"], diction["note"], diction["date"]])
        while True:
            stop = input('Если хотите продолжить вводить данные напишите "y" если хотите закончить, напишите "n":')
            if stop == "n":
                break
            elif stop == "y":
                continue
            else:
                print("Вы ввели не то значение.Попробуйте еще раз")


def delete_file():
    index = str(input("Введите индекс:"))

    with open('csv_example_2.csv', 'r', encoding='utf-8') as csvfile:
        arr = list(csvfile)

    with open('csv_example_2.csv', 'w', encoding='utf-8', newline='\n') as wf:
        csv_writer = csv.writer(wf, delimiter = ";")
        for row in arr:
            if row[0] != index:
                csv_writer.writerows([row.strip().split(';')])


def read_file():
    while True:
        choice = str(input('Прочитать записку по дате или по индексу?:'))
        if choice == "дата":
            num = str(input('Введите дату и время.Например 10.03.2023/10:45:'))
            i = 3
            break
        elif choice == "индекс":
            num = str(input('Введите индекс'))
            i = 0
            break
        else:
            print("Вы ввели не верное значение")

    with open('csv_example_2.csv', 'r', encoding='utf-8') as csvfile:
        arr = list(csvfile)
        flag = False
        for row in arr:
            mass = row.strip().split(';')
            if mass[i] == num:
                read_array = row.strip().split(';')
                print(";".join(read_array))
                flag = True
    if flag == False:
        print("Такой записки нет в базе данных")
    print("----------------")


def update_file():
    index = str(input("ведите индекс:"))

    with open('csv_example_2.csv', 'r', encoding='utf-8') as csvfile:
        arr = list(csvfile)

    with open('csv_example_2.csv', 'w', encoding='utf-8', newline='\n') as wf:
        csv_writer = csv.writer(wf, delimiter = ";")
        for row in arr:
            if row[0] == index:
                row = row.strip().split(';')
                name = str(input("Что вы хотите поменять?:"))
                if name == 'заголовок':
                    row[1] = input("Введите новый заголовок:")
                elif name == 'текст':
                    row[2] = input("Введите новый текст:")
                elif name == "дату":
                    row[3] = input("Введите новую дату:")
                else:
                    print("Данного поля не существует")
                csv_writer.writerows([row])

            else:
                csv_writer.writerows([row.strip().split(';')])
