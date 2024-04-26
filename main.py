class Base:
    file = 0
    token_list2 = []
    lang_tokens = []
    lang_tokens_name = []
    lang_tokens_name_result = []
    counter = 0
    result_list = []
    tokens_result_list = []

    def __init__(self):
        self.file = open("D:\\asd\\char_array.c", "r")
        self.token_list2 = [
            ' ', '\n',
            '#', '&', '%', '+', '-', '*', '/',
            '\"', '\'', '\\', ',', '.', ';',
            '<', '>', '{', '}', '(', ')', '[', ']',
            '^', '&', '=', ':', '|',
        ]
        self.lang_tokens_name = [
            "space", "new line",
            'lattice', 'ampersand', 'percent', 'plus', 'minus', 'multiply', 'solidus',
            'double quotes', 'quotation mark', 'backslash', 'comma', 'dot', 'semicolon',
            'corner open bracket', 'corner close bracket', 'curly open bracket', 'curly closing bracket', 'open parenthesis',
            'close parenthesis', 'square open bracket', 'square close bracket',
            'caret', 'ampersand', 'equal', 'colon', 'vertical bar',
        ]

    def condition(self, char):
        for i in self.token_list2:
            if i == char:
                return True
        return False

    def work(self):
        string = ""
        for line in self.file:
            for i in line:
                if self.condition(i):
                    if len(string) > 0:
                        self.lang_tokens.append(string)
                        string = ""
                    self.lang_tokens.append(i)
                if not self.condition(i):
                    string = string + i
        return self

    def work2(self):
        for i in self.lang_tokens:
            self.counter = 0
            for i2 in self.token_list2:
                if i == i2:
                    temp = self.lang_tokens_name[self.counter]
                    self.lang_tokens_name_result.append(temp)
                self.counter += 1
            if not self.condition(i):
                if len(i) > 1:
                    self.lang_tokens_name_result.append("word")
                if len(i) == 1:
                    self.lang_tokens_name_result.append("character")
        return self

    def union_name_and_value(self):
        self.counter = 0
        while self.counter < len(self.lang_tokens_name_result) and self.counter < len(self.lang_tokens):
            temp_list = [self.lang_tokens_name_result[self.counter], self.lang_tokens[self.counter]]
            self.result_list.append(temp_list)
            self.counter += 1
        self.tokens_result_list = self.result_list
        return self

    def print_correct(self):
        self.counter = 0
        for i in self.lang_tokens_name_result:
            if i == "new line":
                print(i, end='\n')
            else:
                print(i, end='---')

    def __del__(self):
        self.file.close()


lexems_list = [
    ["comments", [
        "one line comment", "//",
        "open multi-line comment", "/*",
        "close multi-line comment", "*/"
    ]],
    ["preprocessor", [
        "begin preprocessor instruction", "#",
        "preprocessor include", "include", [
            "open include bracket base libs", "<", "close include bracket base libs", ">",
            "open include bracket user libs", "\"", "close include bracket user libs", "\""
        ],
        "preprocessor define", "define"
    ]],
    ["string", [
        "string open bracket", "\"", "string close bracket", "\""
    ]],
    ["code block open bracket", "{", "code block close bracket", "}"],
    ["base datatypes", [
        "char", "unsigned char", "short", "unsigned short", "int", "unsigned int", "long", "unsigned long",
        "long long", "unsigned long long", "float", "double"
    ]],
    ["language keywords", [
        ["if statement", "if"],
        ["switch statement", "switch", "into", [
            "name", "case", "into", [
                "name", "break"
            ]
        ]],
        ["cycle statement", "for", "into", [
            "name", "continue",
            "name", "break"
        ]],
        ["cycle statement", "while", "into", [
            "name", "continue",
            "name", "break"
        ]],
        ["special", "extern"],
        ["name", "namespace"],
        ["name", "class"],
        ["name", "object"],
        ["name", "sizeof"],
        ["name", "register"],
        ["name", "public"],
        ["name", "private"]
    ]],
    ["base operators", [
        "plus", "+",
        "minus", "-",
        "multiply", "*",
        "divide", "/",
        "plus and =", "+=",
        "minus and =", "-=",
        "multiply and =", "*=",
        "divide and =", "/=",
        "equal", "==",
        "more", ">",
        "more or equal", ">=",
        "less", "<",
        "less or equal", "<="
    ]]
]

base = Base()
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


# Упростить код
# Добавить работу с линиями кода
# Добавить вложенность класса в класс (token по работе с парами данных вложить в lines)
# Разбить на блоки кода
# Добавить в класс работу с блоками кода
# Сделать навигацию по полученному
# Описать набор правил языка

token = Token(base.tokens_result_list)

token.split_lines().switch_results_lists().print_lines(False).set_default()


while token.lines_condition:
    token.lines_print_current_line().lines_next()
