import abc


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


class CompanyWithAbstract(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_employees(self):
        raise NotImplementedError

    def create_software(self):
        for employee in self.get_employees():
            employee.do_work()


class CompanyA(CompanyWithAbstract):
    def get_employees(self):
        return [Tester()]


class CompanyB(CompanyWithAbstract):
    def get_employees(self):
        return [Designer(), Programmer()]
