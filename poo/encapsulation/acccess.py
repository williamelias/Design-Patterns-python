
# All atributes are accessibles and may be changed
class PublicUser:
    def __init__(self,name,age,gender) -> None:
        self.name = name 
        self.age = age
        self.gender = gender
    
    def __str__(self) -> str:
        return f"My name is {self.name}, I am {self.age} years old and {self.gender}"

# All atributes are accessibles and may be changed, but de __ before attributes indicates 
# dont must be changed
class PrivateUser:
    def __init__(self,name,age,gender) -> None:
        self.__name = name 
        self.__age = age
        self.__gender = gender
    
    def __str__(self) -> str:
        return f"My name is {self.__name}, I am {self.__age} years old and {self.__gender}"

class PrivateUserWithProperty:
    def __init__(self,name,age,gender) -> None:
        self.__name = name 
        self.__age = age
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        raise ValueError('Não é possível alterar o nome diretamente')
    
    @property
    def age(self):
        return self.__age

    
    @age.setter
    def age(self,new_age):
        self.__age = new_age

    @property
    def gender(self):
        return self.__gender
    
    def __str__(self) -> str:
        return f"My name is {self.name}, I am {self.age} years old and {self.gender}"