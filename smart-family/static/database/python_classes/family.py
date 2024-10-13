class Family:
    def __init__(self, id:int, family_name:str, password:str):
        self.id = id
        self.family_name = family_name[0].upper()+family_name[1:]
        self.password = password
    
    def __repr__(self) -> str:
        return f'\n\
id: {self.id},\
 family name: {self.family_name}\n'
