# Before apply Principle


class MongoDb:
    def __init__(self) -> None:
        pass

    def insert_data(self, item):
        pass

    def update_data(self, item):
        pass

    def delete_data(self, item):
        pass


class ReportDatabase:
    def __init__(self) -> None:
        self.__mongodb = MongoDb()

    def add_report(self, item):
        self.__mongodb.insert_data(item)

    def update_report(self, item):
        self.__mongodb.update_data(item)

    def delete_report(self, item):
        self.__mongodb.delete_data(item)


# After apply Principle
import abc


class Database(metaclass=abc.ABCMeta):
    def insert_data(self, item):
        raise NotImplementedError

    def update_data(self, item):
        raise NotImplementedError

    def delete_data(self, item):
        raise NotImplementedError


class MongoDatabase(Database):
    def insert_data(self, item):
        pass

    def update_data(self, item):
        pass

    def delete_data(self, item):
        pass


class PostgresDatabase(Database):
    def insert_data(self, item):
        pass

    def update_data(self, item):
        pass

    def delete_data(self, item):
        pass


class MysqlDatabase(Database):
    def insert_data(self, item):
        pass

    def update_data(self, item):
        pass

    def delete_data(self, item):
        pass


class ReportDatabaseB:
    def __init__(self, db: Database) -> None:
        self.__db = db

    def add_report(self, item):
        self.__db.insert_data(item)

    def update_report(self, item):
        self.__db.update_data(item)

    def delete_report(self, item):
        self.__db.delete_data(item)
