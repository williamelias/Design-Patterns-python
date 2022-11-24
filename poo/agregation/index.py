

class Client:
    def __init__(self,name:str) -> None:
        self.name = name

class Account:
    def __init__(self,client:Client) -> None:
        self.client = client
    