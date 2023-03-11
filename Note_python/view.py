import csv


def view():
    with open('csv_example_2.csv', 'r', encoding='utf-8') as csvfile:
        arr = list(csvfile)
        for row in arr:
            read_array = row.strip().split(';')
            print(";".join(read_array))

    operation_text = input('Выбирите одну из операций - (create-read-update-delete):')
    return operation_text



