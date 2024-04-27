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
    file = None
    tokens_name = []
    tokens_value = []
    tokens_name_result = []
    tokens_value_result = []
    tokens_name_and_value_result = []
    positions = []

    pointer = 0
    current_list = []
    length = 0
    cycle_condition = False
    iterated_list = []

    def set_current_list(self):
        self.current_list = self.iterated_list[self.pointer]
        return self

    def next(self, count=1):
        self.pointer += count
        if self.pointer >= self.length - 1:
            self.stop_cycle()
        self.set_current_list()
        return self

    def back(self, count=1):
        self.pointer -= count
        if self.pointer <= 0:
            self.pointer = 0
        self.set_current_list()
        return self

    def set_iterated_list(self, value):
        self.iterated_list = value
        self.length = len(self.iterated_list)
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
        self.tokens_name = tokens_list.tokens_name
        self.tokens_value = tokens_list.tokens_value

    def split_tokens(self):
        string = ""
        for line in self.file:
            for current_char in line:
                if is_char_list_contain_current_char(current_char, self.tokens_value):
                    if string != "":
                        self.tokens_name_result.append(string)
                        string = ""
                        self.tokens_name_result.append(current_char)
                    elif string == "":
                        self.tokens_name_result.append(current_char)
                elif not is_char_list_contain_current_char(current_char, self.tokens_value):
                    string += current_char
        return self

    def add_names(self):
        for i in self.tokens_name_result:
            if is_char_list_contain_current_char(i, self.tokens_value):
                counter = get_char_position_in_list(i, self.tokens_value)
                self.tokens_value_result.append(self.tokens_name[counter])
            elif not is_char_list_contain_current_char(i, self.tokens_value):
                if len(i) == 1:
                    self.tokens_value_result.append('character')
                elif len(i) > 1:
                    self.tokens_value_result.append('word')
        return self

    def union_names_and_values(self):
        counter = 0
        for i in self.tokens_value_result:
            self.tokens_name_and_value_result.append(
                [self.tokens_value_result[counter], self.tokens_name_result[counter]]
            )
            counter += 1
        return self

    def split_brackets(self):
        pointer = 0
        for token in self.tokens_name_and_value_result:
            if token[0] == "left curly brace" or token[0] == "right curly brace":
                self.positions.append(
                    [pointer, token]
                )
            pointer += 1
        return self

    def work(self):
        self.set_iterated_list(self.positions)
        self.start_cycle()
        while self.cycle_condition:
            print(self.current_list)
            self.next()
        return self

    def print_split_tokens(self):
        print(self.tokens_name_result)
        return self

    def print_add_names(self):
        print(self.tokens_value_result)
        return self

    def print_union_names_and_values(self):
        print(self.tokens_name_and_value_result)
        return self

    def print_split_brackets(self):
        for element in self.positions:
            print(element)
        return self

    def __del__(self):
        self.file.close()


token = Token("D:\\asd\\char_array.c", "r")
token.split_tokens().add_names().union_names_and_values().split_brackets().work()
# token.print_split_brackets()
