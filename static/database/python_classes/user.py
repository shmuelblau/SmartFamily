class User:
    def __init__(self, id: int, family_id: int, first_name: str, last_name: str, age: float, password: str):
        self.id = id
        self.family_id = family_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.age = age

    def __repr__(self) -> str:
        return f'\
id: {self.id},\
 first name: {self.first_name},\
 last name: {self.last_name},\
 age: {self.age}\n'
