
class NameValue:
    name = 'example-name'
    value = 'example-value'

    def __init__(self, name='', value=''):
        self.set_name(name)
        self.set_value(value)

    def set_name(self, name):
        self.name = name
        return self

    def get_name(self):
        return self.name

    def set_value(self, value):
        self.value = value
        return self

    def get_value(self):
        return self.value


class Pair:
    pair = []

    def __init__(self, pair=[]):
        self.pair = pair

    def set_pair(self, pair):
        self.pair = pair
        return self

    def get_pair(self):
        return self.pair


class NamedPair:
    name_value = NameValue()
    pair = Pair()

    def update_pair_from_name_value(self):
        self.pair.set_pair([
            self.name_value.get_name(), self.name_value.get_value()
        ])
        return self

    def update_name_value_from_pair(self):
        pair = self.pair.get_pair()
        name = pair[0]
        value = pair[1]
        self.name_value.set_name(name)
        self.name_value.set_value(value)
        # альтернатива
        # self.name_value.set_name(
        #     self.pair.get_pair()[0]
        # )
        # self.name_value.set_value(
        #     self.pair.get_pair()[1]
        # )
        return self

    def set_name(self, name):
        self.name_value.set_name(name)
        self.update_pair_from_name_value()
        return self

    def set_value(self, value):
        self.name_value.set_value(value)
        self.update_pair_from_name_value()
        return self

    def set_pair(self, pair):
        self.pair.set_pair(pair)
        self.update_name_value_from_pair()
        return self


class InterfaceNamedPair(NamedPair):

    def __init__(self, name='', value=''):
        self.set_name(name)
        self.set_value(value)

    def get_name(self):
        return self.name_value.get_name()

    def get_value(self):
        return self.name_value.get_value()

    def get_pair(self):
        return self.pair.get_pair()


class PrintInterfaceNamedPair(InterfaceNamedPair):

    def print_name(self, end='\n'):
        print(self.name_value.get_name(), end=end)
        return self

    def print_value(self, end='\n'):
        print(self.name_value.get_value(), end=end)
        return self

    def print_pair(self, end='\n'):
        print(self.pair.get_pair(), end=end)
        return self


class AbstractSyntaxTree(PrintInterfaceNamedPair):

    def __init__(self):
        super().__init__()


class AST(AbstractSyntaxTree):

    def __init__(self, name='', value=''):
        self.name_value.set_name(name)
        self.name_value.set_value(value)
        super().__init__()


# AST().set_pair(
#     [
#         ['test', 'hello'],
#         ['test', 'hello']
#     ]
# ).print_pair().print_name().print_value()





















