import tokens_list


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


token = Token("char_array.c", "r")
token.split_tokens().add_names().union_names_and_values().split_blocks()
token.print_split_blocks()

# Сделать AST - абстрактное дерево для удобной навигации по коду
# Формат (конкретный формат) хранения данных в памяти не важен
# Важно чтобы по коду было удобно перещаться (вперед-назад/вверх-вниз)
# Далее в соответствии с правилами языка проверить корректность выражений
# Сделать динамический проход по данным
# Далее сгенерировать код на си (выходной)

name = [
    'new line'
]
value = [
    '\n'
]
position_line = [
    '1'
]
position_char_into_line = [
    '1'
]
size = [
    1
]
characteristics = [
    'char'
]

data = [
    'token', [
        ['name', 'new line'],
        ['value', '\n'],
        ['position_line', '1'],
        ['position_char_into_line', 'new line'],
        ['size', '1'],
        ['characteristics', 'char'],
    ]
]


class Hello:
    pointer = 0

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    def __init__(self):
        self.length = 0

    def __del__(self):
        self.length = None


class File:
    _file = None
    _path = ""
    _modifier = ""

    def __init__(self, path='', modifier='r'):
        if path != '':
            self._path = path
            self._modifier = modifier
            self._file = open(self._path, self._modifier)

    def set_path(self, path):
        self._path = path
        return self

    def set_modifier(self, modifier='r'):
        self._modifier = modifier
        return self

    def open_file(self):
        self._file = open(self._path, self._modifier)
        return self

    def __del__(self):
        if self._file is not None:
            self._file.close()


file = File()


class Example:
    list1 = []
    pointer_list1 = 0

    list2 = []
    pointer_list2 = 0

    list3 = []
    pointer_list3 = 0

    list4 = []
    pointer_list4 = 0

    iterated_list = None
    iterated_list_length = 0
    iterated_list_pointer = 0
    iterated_list_current_data = None
    iterated_list_cycle_condition = False

    def set_iterated_list(self, value):
        self.iterated_list = value
        self.update_length()
        return self

    def get_iterated_list(self):
        return self.iterated_list

    def update_length(self):
        self.iterated_list_length = len(self.get_iterated_list())
        return self

    def get_length(self):
        return self.iterated_list_length

    def set_pointer(self, value=0):
        self.iterated_list_pointer = value
        return self

    def get_pointer(self):
        return self.iterated_list_pointer

    def set_current_data(self, value):
        self.iterated_list_current_data = value
        return self

    def get_current_data(self):
        return self.iterated_list_current_data

    def start_cycle(self):
        self.iterated_list_cycle_condition = True
        return self

    def stop_cycle(self):
        self.iterated_list_cycle_condition = False
        return self

    def __init__(self):
        pass

    def go_next(self, count=1):
        self.set_pointer(
            self.get_pointer() + count
        )
        if self.get_pointer() >= self.get_length() - 1:
            self.set_pointer(self.get_length() - 1)
        return self

    def go_back(self, count=1):
        self.set_pointer(
            self.get_pointer() - count
        )
        if self.get_pointer() < 0:
            self.set_pointer(0)
        return self

    def go_down(self, count=1):
        pass

    def go_up(self, count=1):
        pass

    def go_over(self, count=1):
        pass

    def go_out(self, count=1):
        pass
