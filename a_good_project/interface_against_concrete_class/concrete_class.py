# Example with concrete class dependency


class ProgrammerConcrete:
    def write_code(self):
        return "write code"


class DesignerConcrete:
    def plan_system(self):
        return "plan system"


class TesterConcrete:
    def test_software(self):
        return "test software"


class CompanyConcrete:
    def __init__(self) -> None:
        self.programmer = ProgrammerConcrete()
        self.designer = DesignerConcrete()
        self.tester = TesterConcrete()

    def create_software(self):
        self.designer.plan_system()
        self.programmer.write_code()
        self.tester.test_software()
