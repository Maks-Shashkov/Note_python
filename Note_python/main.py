from CRUD import create_file, read_file, update_file, delete_file
from view import view


if __name__ == '__main__':
    while True:
        operation = view()
        if operation == "create":
            create_file()
        elif operation == "read":
            read_file()
        elif operation == "update":
            update_file()
        elif operation == "delete":
            delete_file()
        else:
            print("Такой операции не существует")



