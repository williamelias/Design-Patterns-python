import typing as tp


"""
Aggregation's Example

- Account is associated with Client
- Bank knows about Accounts (aggregation here)

"""

class Client:
    def __init__(self,name:str) -> None:
        self.name = name

class Account:
    def __init__(self,client:Client) -> None:
        self.client = client
    
class Bank:
    def __init__(self) -> None:
        self.accounts:tp.List[Account] = []
    def add_account(self,account:Account) -> None:
        self.accounts.append(account)
    
    def remove_account(self,account:Account) -> None:
        self.accounts.remove(account)