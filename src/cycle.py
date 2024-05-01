
class First:
    cycle_condition = False

    def __init__(self, value=False):
        self.cycle_condition = value

    def set_cycle_condition(self, value):
        self.cycle_condition = value
        return self

    def get_condition(self):
        return self.cycle_condition


class First2:
    first1 = First()

    def __init__(self, first=First()):
        self.first1 = first


class Cycle:
    pass













































