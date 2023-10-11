from typing import Iterable

"""
Composition's Example
- AccountHistory has __data property
- Account has __history:AccountHistory property and manage history data

"""

class AccountHistory:
    def __init__(self) -> None:
        self.__data:Iterable[str] = []
    
    @property
    def data(self):            
        return f"Historical data: {self.__data}"

    def append_data(self,item:str):
        self.__data.append(item)


class Account:
    def __init__(self) -> None:
        self.__history = AccountHistory()
    
    @property
    def history(self):
        return self.__history.data
        
    def update_history(self,item):
        self.__history.append_data(item)


    