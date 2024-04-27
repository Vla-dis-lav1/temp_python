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
    tokens_lines = []

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
            temp_list = [self.tokens_value_result[counter], self.tokens_name_result[counter]]
            self.tokens_name_and_value_result.append(temp_list)
            counter += 1
        return self

    def split_lines(self):
        temp_list = []
        for i in self.tokens_name_and_value_result:
            if i[0] == "new line":
                temp_list.append(i)
                self.tokens_lines.append(temp_list)
                temp_list = []
            else:
                temp_list.append(i)

    def print_tokens(self):
        print(self.tokens_name_result)
        return self

    def print_tokens2(self):
        print(self.tokens_value_result)
        return self

    def print_tokens3(self):
        print(self.tokens_name_and_value_result)
        return self

    def print_lines(self):
        for line in self.tokens_lines:
            print(line)
        return self

    def __del__(self):
        self.file.close()


token = Token("D:\\asd\\char_array.c", "r")
token.split_tokens().add_names().union_names_and_values().split_lines()
token.print_lines()
