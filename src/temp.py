import start_data


class FileSettings:
    file_name = None
    modifier = None

    def __init__(self, file_name=None, modifier=None):
        self.file_name = file_name
        self.modifier = modifier

    def set_file_name(self, value):
        self.file_name = value
        return self

    def set_modifier(self, value):
        self.modifier = value
        return self

    def get_file_name(self):
        return self.file_name

    def get_modifier(self):
        return self.modifier

    def check(self):
        if self.file_name is None or self.modifier is None:
            if self.file_name is None:
                print('file_name = None')
                raise Exception('file_name = None')
            if self.modifier is None:
                print('modifier = None')
                raise Exception('modifier = None')


class GetInfo(FileSettings):
    pass


class FileBase:
    file_settings = None
    file = None

    def get_file(self):
        return self.file

    def get_file_settings(self):
        return self.file_settings

    def __init__(self, file_settings=FileSettings()):
        self.file_settings = file_settings

    def open_file(self):
        self.file_settings.check()
        self.file = open(self.file_settings.get_file_name(), self.file_settings.get_modifier())
        return self

    def close_file(self):
        if self.file is not None:
            # print('file')
            self.file.close()
        else:
            # print('file = None')
            pass
        return self

    def __del__(self):
        self.close_file()


class FilePrint:
    file_base = None

    def __init__(self, file_base=FileBase()):
        self.file_base = file_base

    def print_all_file_data(self):
        for line in self.file_base.get_file():
            print(line, end='')
        return self


class FileData:
    file_base = None
    file_data_row = None

    def __init__(self, file_base=FileBase()):
        self.file_base = file_base

    def read_file_data(self):
        self.file_data_row = self.file_base.get_file().read()
        return self

    def get_file_data_row(self):
        return self.file_data_row


class FileDataPrint:
    file_data_object = None

    def __init__(self, file_data=FileData(), value=False, end=''):
        self.file_data_object = file_data
        if value:
            self.print_file_data(end)

    def print_file_data(self, end=''):
        print(self.file_data_object.get_file_data_row(), end=end)
        return self


# file_settings = FileSettings().set_file_name(path).set_modifier(modifier)
# file_base = FileBase(file_settings).open_file()
# file_print = FilePrint(file_base).print_all_file_data()
# Кратко то же самое
FilePrint(
    FileBase(
        FileSettings().set_file_name(start_data.path).set_modifier(start_data.modifier)
    ).open_file()
)  # .print_all_file_data()

file_data = FileData(
    FileBase(
        FileSettings().set_file_name(start_data.path).set_modifier(start_data.modifier)
    ).open_file()
).read_file_data()
# file_data_print = FileDataPrint(file_data).print_file_data()
FileDataPrint(file_data, True)



