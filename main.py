import tokens_list
import start_data

path = "char_array.c"
modifier = "r"


def is_char_list_contain_current_char(current_char, list_to_check):
    for char in list_to_check:
        if char == current_char:
            return True
    return False


def get_char_position_in_list(current_char, list_to_check):
    counter = 0
    for elem in list_to_check:
        if elem == current_char:
            return counter
        else:
            counter += 1
    return counter - 1


class Token:
    _file = None
    tokens_name_declaration = []
    tokens_value_declaration = []
    tokens_name = []
    tokens_value = []
    tokens_name_and_value = []

    pointer = 0
    current_list = []
    length = 0
    cycle_condition = False
    iterated_list = []

    blocks_result = []

    def update_length(self):
        self.length = len(self.iterated_list)
        return self

    def set_current_list(self):
        self.current_list = self.iterated_list[self.pointer]
        return self

    def get_current_list(self):
        return self.current_list

    def next(self, count=1):
        self.pointer += count
        if self.pointer > self.length - 1:
            self.pointer = self.length - 1
            self.stop_cycle()
        self.set_current_list()
        return self

    def back(self, count=1):
        self.pointer -= count
        if self.pointer < 0:
            self.pointer = 0
            self.stop_cycle()
        self.set_current_list()
        return self

    def set_iterated_list(self, value):
        self.iterated_list = value
        self.update_length()
        self.set_current_list()
        return self

    def stop_cycle(self):
        self.cycle_condition = False
        return self

    def start_cycle(self):
        self.cycle_condition = True
        return self

    def __init__(self, file_name, modifier):
        self.file = open(file_name, modifier)
        self.tokens_name_declaration = tokens_list.tokens_name
        self.tokens_value_declaration = tokens_list.tokens_value

    def split_tokens(self):
        string = ""
        for line in self.file:
            for current_char in line:
                if is_char_list_contain_current_char(current_char, self.tokens_value_declaration):
                    if string != "":
                        self.tokens_name.append(string)
                        string = ""
                        self.tokens_name.append(current_char)
                    elif string == "":
                        self.tokens_name.append(current_char)
                elif not is_char_list_contain_current_char(current_char, self.tokens_value_declaration):
                    string += current_char
        return self

    def add_names(self):
        for i in self.tokens_name:
            if is_char_list_contain_current_char(i, self.tokens_value_declaration):
                counter = get_char_position_in_list(i, self.tokens_value_declaration)
                self.tokens_value.append(self.tokens_name_declaration[counter])
            elif not is_char_list_contain_current_char(i, self.tokens_value_declaration):
                if len(i) == 1:
                    self.tokens_value.append('character')
                elif len(i) > 1:
                    self.tokens_value.append('word')
        return self

    def union_names_and_values(self):
        counter = 0
        for i in self.tokens_value:
            self.tokens_name_and_value.append(
                [self.tokens_value[counter], self.tokens_name[counter]]
            )
            counter += 1
        return self

    def get_list(self, start, end):
        result_list = []
        counter = start
        while counter <= end:
            result_list.append(self.iterated_list[counter])
            counter += 1
        return result_list

    def delete_from_list(self, start, end):
        counter = start
        while counter <= end:
            self.iterated_list.pop(start)
            counter += 1
        self.update_length()

    def replace(self, start, end):
        temp = self.get_list(start, end)
        self.delete_from_list(start, end)
        self.iterated_list.insert(start, temp)
        self.update_length()

    def split_blocks(self):
        self.set_iterated_list(self.tokens_name_and_value)
        self.start_cycle()
        temp_list = []
        while self.cycle_condition:
            if self.current_list[0] == "left curly brace" or self.current_list[0] == "right curly brace":
                temp_list.append([
                    self.pointer, self.current_list[0]
                ])
            if len(temp_list) > 1:
                if temp_list[len(temp_list) - 1][1] == "right curly brace":
                    close_bracket = temp_list.pop()
                    open_bracket = temp_list.pop()
                    self.replace(open_bracket[0], close_bracket[0])
                    self.pointer = open_bracket[0]
            self.next()
        return self

    def print_split_tokens(self):
        print(self.tokens_name)
        return self

    def print_add_names(self):
        print(self.tokens_value)
        return self

    def print_union_names_and_values(self):
        print(self.tokens_name_and_value)
        return self

    def print_split_blocks(self):
        for elem in self.iterated_list:
            if isinstance(elem[0], list):
                print(elem)
            else:
                print(elem)

    def __del__(self):
        self.file.close()


# token = Token("char_array.c", "r")
# token.split_tokens().add_names().union_names_and_values().split_blocks()
# token.print_split_blocks()


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


# file_settings = FileSettings().set_file_name(path).set_modifier(modifier)
# file_base = FileBase(file_settings).open_file()
# file_print = FilePrint(file_base).print_all_file_data()
# Кратко то же самое
FilePrint(
    FileBase(
        FileSettings().set_file_name(start_data.path).set_modifier(start_data.modifier)
    ).open_file()
).print_all_file_data()




















