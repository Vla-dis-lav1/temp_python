# TODO:
# Сделать циклы в классе (перебор значения с помощью класса для облегчения себе работы)
# Протестировать работу циклов (обязательно!)
# Сделать и протестировать работу с файлами (дополнительно - не обязательно)
# Сделать свои списки
# Протестировать работу своих список (вложенность и т.д.)
# Сделать систему для навигации и в итоге получить абстрактное синтаксическое дерево и проверить его работу
# АСД (абстрактное синтаксическое дерево)
# Далее разбить исходный код на токены и записать в АСД
# Далее определить правила языка
# Далее определить интерпретацию для программы ранее описанных правил языка
# Построить второе АСД на основе первого уже используя токены для генерации
# Здесь еще стоит подумать как реализовать
# Далее сгенерировать специальный байт код для своей виртуальной машины
# Далее сгенерировать из байт-кода реальный исполняемый код на си
# Либо сделать сразу генерацию кода на Си (этот путь сложнее и гораздо сильнее подвержен ошибкам,
# которые еще и отлавливать и исправлять будет сложно, но он более короткий(вероятно) )
# TODO: End


import tokens_list
import start_data
import lang_rules
# token
import src.file
import src.ast
import src.cycle
import src.token


inter = src.ast.InterfaceNamedPair()
cycle = src.cycle.Cycle()
file = src.file.File()
token2 = src.token.Token()

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


token = Token("char_array.c", "r")
token.split_tokens().add_names().union_names_and_values()
# token.print_union_names_and_values()


pair_list = token.tokens_name_and_value

global_position = []
line = []
symbol_start_end = []
size = []


counter = 0
for pair in pair_list:
    if len(pair[1]) == 1:
        symbol_start_end.append([
            counter + 1, counter + 1
        ])
    elif len(pair[1]) > 1:
        symbol_start_end.append([
            counter + 1, counter + len(pair[1]) + 1
        ])
    counter += len(pair[1])
    global_position.append(counter)

for i in symbol_start_end:
    size.append(
        int(i[1]) - int(i[0]) + 1
    )

for pair in pair_list:
    if pair[1] == '\n':
        pass

# print(global_position)
# print(symbol_start_end)
print(size)






































