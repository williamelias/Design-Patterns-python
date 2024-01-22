# Before
class EmployeeA:
    def __init__(self, name) -> None:
        self.__name

    def get_name(self):
        return self.name

    def print_time_sheet_report(self):
        print(self.__dict__)


# After


class EmployeeB:
    def __init__(self, name) -> None:
        self.__name = name

    def get_name(self):
        return self.__name


class TimeSheetReport:
    def print_time_sheet_report(self, employee: EmployeeB):
        print(employee.__dict__)
