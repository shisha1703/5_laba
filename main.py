
class fileexec1:
    def run(self):
        print("Code executed from file1.py")


# file2.py
class fileexec2:
    def run(self):
        print("Code executed from file2.py")


# file3.py
class fileexec3:
    def run(self):
        print("Code executed from file3.py")


# file4.py
class fileexec4:
    def run(self):
        print("Code executed from file4.py")


# main.py
import importlib


class Main:
    def __init__(self):
        self.file_num = int(input("Введите номер файла (1-4): "))

    def run_file(self):
        if self.file_num < 1 or self.file_num > 4:
            print("Файл не найден, введите число заного от 1 до 4")
            return

        module_name = f"file{self.file_num}"
        class_name = f"File{self.file_num}"

        try:
            module = importlib.import_module(module_name)
            selected_class = getattr(module, class_name)()
            selected_class.run()
        except ModuleNotFoundError:
            print("Файл не найден.")


if __name__ == "__main__":
    main = Main()
    main.run_file()