import abc

# Without Interface segregation


class CloudProvider(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def store_file(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_file(self):
        raise NotImplementedError

    @abc.abstractmethod
    def create_server(self):
        raise NotImplementedError

    @abc.abstractmethod
    def stop_server(self):
        raise NotImplementedError


class Amazon(CloudProvider):
    def store_file(self):
        return 'implemented'

    def get_file(self):
        return 'implemented'

    def create_server(self):
        return 'implemented'

    def stop_server(self):
        return 'implemented'


class DropBox(CloudProvider):
    def store_file(self):
        return 'implemented'

    def get_file(self):
        return 'implemented'

    def create_server(self):
        return "Not implemented because doesn't exists in DropBoX "

    def stop_server(self):
        return "Not implemented because doesn't exists in DropBoX "


# With Interface Segregation Principle


class StorageProvider(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def store_file(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_file(self):
        raise NotImplementedError


class CloudServerProvider(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_server(self):
        raise NotImplementedError

    @abc.abstractmethod
    def stop_server(self):
        raise NotImplementedError


class Amazon(StorageProvider, CloudServerProvider):
    def store_file(self):
        return 'implemented'

    def get_file(self):
        return 'implemented'

    def create_server(self):
        return 'implemented'

    def stop_server(self):
        return 'implemented'


class DropBox(StorageProvider):
    def store_file(self):
        return 'implemented'

    def get_file(self):
        return 'implemented'
