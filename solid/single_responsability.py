# Before
class EmployeeA:
    def __init__(self, name) -> None:
        self.__name

    def get_name(self):
        pass

    def print_time_sheet_report(self):
        return self.get_name()


# After


class EmployeeB:
    def __init__(self, name) -> None:
        self.__name = name

    def get_name(self):
        return self.__name


class TimeSheetReport:
    def print_time_sheet_report(self, employee: EmployeeB):
        return employee.get_name()
