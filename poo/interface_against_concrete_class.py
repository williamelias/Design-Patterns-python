import abc


# Example with concrete class dependency


class ProgrammerConcrete:
    def write_code(self):
        return 'write code'


class DesignerConcrete:
    def plan_system(self):
        return 'plan system'


class TesterConcrete:
    def test_software(self):
        return 'test software'


class CompanyConcrete:
    def __init__(self) -> None:
        self.programmer = ProgrammerConcrete()
        self.designer = DesignerConcrete()
        self.tester = TesterConcrete()

    def create_software(self):
        self.designer.plan_system()
        self.programmer.write_code()
        self.tester.test_software()


# Example less coupled than before


class Employee(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_work(self):
        raise NotImplementedError


class Programmer(Employee):
    def do_work(self):
        return 'write code'


class Designer(Employee):
    def do_work(self):
        return 'plan system'


class Tester(Employee):
    def do_work(self):
        return 'test software'


class Company:
    def get_employees(self):
        return [Designer(), Programmer(), Tester()]

    def create_software(self):
        for employee in self.get_employees():
            employee.do_work()


# Example less coupled than before


class CompanyWithAbstract:
    @abc.abstractmethod
    def get_employees(self):
        raise NotImplementedError

    def create_software(self):
        for employee in self.get_employees():
            employee.do_work()


class CompanyA(Company):
    def get_employees(self):
        return [Tester()]


class CompanyB(Company):
    def get_employees(self):
        return [Designer(), Programmer()]
