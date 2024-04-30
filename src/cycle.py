
class First1:
    cycle_condition = False

    def set_cycle_condition(self, cycle_condition):
        self.cycle_condition = cycle_condition
        return self

    def get_cycle_condition(self):
        return self.cycle_condition


class First2(First1):

    def is_cycle_running(self):
        if self.get_cycle_condition():
            return self.get_cycle_condition()
        else:
            return not self.get_cycle_condition()

    def is_cycle_not_running(self):
        if self.get_cycle_condition():
            return not self.get_cycle_condition()
        else:
            return self.get_cycle_condition()


class First(First2):

    def start_cycle(self):
        self.set_cycle_condition(True)
        return self

    def stop_cycle(self):
        self.set_cycle_condition(False)
        return self


class Pointer:
    pointer = 0

    def __init__(self, pointer=0):
        self.pointer = pointer

    def set_pointer(self, pointer):
        self.pointer = pointer
        return self

    def get_pointer(self):
        return self.pointer


class IteratedList(Pointer):
    iterated_list = []
    length = 0
    current_list = []
    current_list_length = 0

    def __init__(self, iterated_value=[]):
        super().__init__()
        self.set_iterated_list(iterated_value)

    def set_iterated_list(self, value):
        self.iterated_list = value
        return self

    def get_iterated_list(self):
        return self.iterated_list

    def set_length(self, value):
        self.length = value
        return self

    def get_length(self):
        return self.length

    def set_current_list(self, value):
        self.current_list = value
        return self

    def get_current_list(self):
        return self.current_list

    def set_current_list_length(self, value):
        self.current_list_length = value
        return self

    def get_current_list_length(self):
        return self.current_list_length


class Update:
    iterated_list_object = IteratedList()

    def __init__(self, value=IteratedList()):
        self.iterated_list_object = value

    def update_length(self):
        self.iterated_list_object.set_length(
            len(self.iterated_list_object.get_iterated_list())
        )

    def update_current_value(self):
        pointer = self.iterated_list_object.get_pointer()
        self.iterated_list_object.set_current_list(
            self.iterated_list_object.get_iterated_list()[pointer]
        )
        pass

    def set_all_default(self):
        self.iterated_list_object.set_iterated_list([])
        self.iterated_list_object.set_pointer(0)
        self.iterated_list_object.set_current_list('')


class Cycle(First):

    def __init__(self, value=False):
        self.set_cycle_condition(value)

    def switch(self):
        if self.is_cycle_running():
            self.stop_cycle()
        elif self.is_cycle_not_running():
            self.start_cycle()
        return self
















































