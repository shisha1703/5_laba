class FileOpener:
    def __init__(self):
        self.file_mapping = {
            '1': 'file1.txt',
            '2': 'file2.txt',
            '3': 'file3.txt',
            '4': 'file4.txt'
        }

    def open_file(self, input_number):
        file_name = self.file_mapping.get(input_number)
        if file_name:
                with open(file_name, 'r') as file:
                    content = file.read()
                    print(f'Содержимое файла {file_name}: {content}')


if __name__ == '__main__':
    file_opener = FileOpener()

    user_input = input('Введите число для открытия содержимого файла (1-4): ')
    if user_input in ['1', '2', '3', '4']:
        file_opener.open_file(user_input)
    else:
        print('Введите число заново от 1-4.')
