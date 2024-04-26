import tokens_list


class Base:
    file = None
    tokens_name = []
    tokens_value = []
    tokens1 = []
    tokens2 = []
    tokens3 = []
    tokens4 = []
    counter = 0

    def __init__(self, file_name, modifier):
        self.file = open(file_name, modifier)
        self.tokens_name = tokens_list.tokens_name
        self.tokens_value = tokens_list.tokens_value

    def condition(self, char):
        for i in self.tokens_value:
            if i == char:
                return True
        return False

    def work(self):
        string = ""
        for line in self.file:
            for current_char in line:
                if self.condition(current_char):
                    if len(string) > 0:
                        self.tokens1.append(string)
                        string = ""
                    self.tokens1.append(current_char)
                if not self.condition(current_char):
                    string = string + current_char
        return self

    def work2(self):
        for i in self.tokens1:
            self.counter = 0
            for i2 in self.tokens_value:
                if i == i2:
                    temp = self.tokens_name[self.counter]
                    self.tokens2.append(temp)
                self.counter += 1
            if not self.condition(i):
                if len(i) > 1:
                    self.tokens2.append("word")
                if len(i) == 1:
                    self.tokens2.append("character")
        return self

    def union_name_and_value(self):
        self.counter = 0
        while self.counter < len(self.tokens2) and self.counter < len(self.tokens1):
            temp_list = [self.tokens2[self.counter], self.tokens1[self.counter]]
            self.tokens3.append(temp_list)
            self.counter += 1
        self.tokens4 = self.tokens3
        return self

    def __del__(self):
        self.file.close()


base = Base("D:\\asd\\char_array.c", "r")
base.work().work2().union_name_and_value()


class Token:
    result_list = []
    length = 0
    pointer = 0
    pair = []
    name = ""
    value = ""
    condition = False
    temp_list = []
    result_list2 = []
    lines_length = 0
    lines_pointer = 0
    lines_condition = False
    lines_current_line = []

    def __init__(self, list1, start_pointer=0):
        self.result_list = list1
        self.length = len(self.result_list)
        self.pointer = start_pointer
        self.update_pair_name_value()
        self.switch()

    def switch(self):
        if not self.condition:
            self.condition = True
        elif self.condition:
            self.condition = False
        return self

    def update_pair_name_value(self):
        self.pair = self.get_current_pair()
        self.name = self.get_current_name()
        self.value = self.get_current_value()
        return self

    def next(self, count=1):
        if self.pointer >= self.length - 1:
            self.pointer = self.length - 1
            self.switch()
        else:
            self.pointer += count
        self.update_pair_name_value()
        return self

    def back(self, count=1):
        if self.pointer <= 0:
            self.pointer = 0
        else:
            self.pointer -= count
        self.update_pair_name_value()
        return self

    def get_current_pair(self):
        return self.result_list[self.pointer]

    def get_current_name(self):
        return self.get_current_pair()[0]

    def get_current_value(self):
        return self.get_current_pair()[1]

    def print_pair(self):
        print(self.pair)
        return self

    def print_name(self):
        print(self.name)
        return self

    def print_value(self):
        print(self.value)
        return self

    def print_temp_cycle(self):
        print(self.condition)
        return self

    def print_temp_list(self):
        print(self.temp_list)
        return self

    def switch_results_lists(self):
        self.result_list = self.result_list2
        self.result_list2 = []
        return self

    def set_default(self):
        self.pointer = 0
        if not self.condition:
            self.switch()
        if len(self.temp_list) > 0:
            self.temp_list = []
        return self

    def print_lines(self, value=True):
        if not value:
            return self
        for i in self.result_list:
            print(i)
        return self

    def temp_list_append(self, value_for_append):
        self.temp_list.append(value_for_append)
        return self

    def result_list2_append(self, value_for_append):
        self.result_list2.append(value_for_append)
        return self

    def set_temp_list_empty(self):
        self.temp_list = []
        return self

    def split_lines(self):
        while self.condition:
            if self.name == "new line":
                self.temp_list_append(
                    self.get_current_pair()
                ).result_list2_append(
                    self.temp_list
                ).set_temp_list_empty()
            else:
                self.temp_list_append(self.get_current_pair())
            self.next()
        self.lines_set_default()
        return self

    def lines_set_default(self):
        self.lines_length = len(self.result_list)
        self.lines_pointer = 0
        self.lines_condition = True
        self.lines_update_current()
        return self

    def lines_set_current(self):
        self.lines_current_line = self.result_list[self.lines_pointer]
        return self

    def lines_get_current(self):
        return self.lines_current_line

    def lines_update_current(self):
        self.lines_set_current()
        return self

    def lines_switch(self):
        if not self.lines_condition:
            self.lines_condition = True
        elif self.lines_condition:
            self.lines_condition = False
        return self

    def lines_next(self, count=1):
        self.lines_length = len(self.result_list)
        if self.lines_pointer >= self.lines_length - 1:
            self.lines_pointer = self.lines_length - 1
            self.lines_switch()
        else:
            self.lines_pointer += count
        self.lines_update_current()
        return self

    def lines_back(self, count=1):
        if self.lines_pointer <= 0:
            self.lines_pointer = 0
        else:
            self.lines_pointer -= count
        self.lines_update_current()
        return self

    def lines_print_current_line(self):
        print(self.lines_get_current())
        return self


# token = Token(base.tokens4)

# token.split_lines().switch_results_lists().print_lines(False).set_default()
