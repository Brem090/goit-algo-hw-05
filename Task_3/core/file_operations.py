def read_file(file_path):
    with open(file_path, 'r', encoding='cp1251') as file:
        return file.read()
