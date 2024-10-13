class User:
    def __init__(self, id: int, family_id: int, first_name: str, last_name: str, age: float, password: str = '000000', status: float = 0.0):
        self.id = id
        self.family_id = family_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.password = password
        self.status = status

    def __repr__(self) -> str:
        return f'\n\
id: {self.id},\
 first name: {self.first_name},\
 last name: {self.last_name},\
 age: {self.age},\
 status: {self.status}\n'
