import copy
from static.database.sql_management import sql
from static.database.python_classes.family import Family
from static.database.python_classes.user import User
from static.database.python_classes.task import Task


class Families:

    def __init__(self):
        self.table_name = 'families'
        self.col_table_names = {
            'id' : 'INTEGER',
            'family_name': 'TEXT',
            'password': 'TEXT'
        }
        sql.add_table(self.table_name, self._create_columns_string_for_table())
        self.families_list = self.get_all_families()


    def _create_columns_string_for_table(self):
        return ','.join([
            f'{col} {type}' for col,type in self.col_table_names.items() if col != 'id'
            ]) 


    def get_all_families(self) -> list[Family]:
        if sql.is_table_exists(self.table_name):
            families = sql.fetch_all(self.table_name)
            if len(families) > 0:
                families_list = [
                    Family(family[0], family[1], family[2]) for family in families
                    ]
                return families_list
        return []

    def get_family_by_id(self, id: int) -> Family:
        """be aware: >>> \if family id don't exist the function return -> None type"""
        family = sql.fetch_by_id(self.table_name, id)
        if family == None:
            print('There is no family with this id...')
        else:
            return Family(family[0], family[1], family[2])


    def add_family(self, family_name: str, password: str) -> None:
        """ >>> \'the function automatically append to families_list\'"""
        sql.add_field(self.table_name, family_name, password)
        self.families_list.insert(
            Family(sql.fetch_last_one(self.table_name)[0], family_name, password)
            )

    def delete_family(self, id: int) -> None:
        """ >>> \'the function automatically refresh the families_list\'"""
        sql.delete_field(self.table_name, id)
        self.families_list = [
            family for family in self.families_list if family.id != id
            ]

    def update_family(self, id_value: int, column_name: str, new_value: any) -> None:
        """ >>> \'the function automatically refresh the families_list\'"""
        sql.update_field(self.table_name,id_value,column_name,new_value)
        self.families_list = self.get_all_families()


class Users:

    def __init__(self):
        self.table_name = 'users'
        self.col_table_names = {
            'id': 'INTEGER',
            'family_id': 'INTEGER',
            'first_name': 'TEXT',
            'last_name': 'TEXT',
            'age' : 'INTEGER',
            'password' : 'TEXT',
            'status': 'REAL'
        }
        sql.add_table(self.table_name, self._create_columns_string_for_table())
        self.users_list = self.get_all_users()

    
    def _create_columns_string_for_table(self):
        return ','.join([
            f'{col} {type}' for col,type in self.col_table_names.items() if col != 'id'
            ]) 


    def get_all_users(self) -> list[User]:
        if sql.is_table_exists(self.table_name):
            users = sql.fetch_all(self.table_name)
            if len(users) > 0:
                users_list = [
                    User(user[0], user[1], user[2], user[3], user[4], user[5], user[6]) for user in users
                    ]
                return users_list
        return []

    def add_user(self, family_id: int, first_name: str, last_name: str, age: int, password: str = '000000', status: float = 0.0) -> None:
        """ >>> \'the function automatically append to users_list\'"""
        sql.add_field(self.table_name, family_id, first_name,last_name, age, password, status)
        self.users_list.append(
            User(sql.fetch_last_one(self.table_name)[0], family_id, first_name, last_name, age, password,status)
        )

    def get_user_by_id(self, id: int) -> User:
        """be aware: >>> \if user id don't exist the function return -> None type"""
        user = sql.fetch_by_id(self.table_name, id)
        if user == None:
            print('There is no user with this id...')
        else:
            return User(
                user[0], user[1], user[2], user[3], user[4], user[5], user[6]
                )

    def get_users_by_family_id(self, id: int) -> list[User]:
        users = sql.fetch_all_by_foreign_key(self.table_name, 'family_id', id)
        if users == None:
            print('There is no user for this family...')
            return []
        else:
            return [
                User(user[0], user[1], user[2], user[3], user[4], user[5], user[6] ) for user in users
                ]

    def delete_user(self, id: int) -> None:
        """ >>> \'the function automatically refresh the users_list\'"""
        sql.delete_field(self.table_name, id)
        self.users_list = [user for user in self.users_list if user.id != id]

    # Attention! The update function only updates when a column name is provided
    def update_user(self, id_value: int, column_name: str, new_value: any) -> None:
        """ >>> \'the function automatically refresh the users_list\'"""
        sql.update_field(self.table_name,id_value,column_name,new_value)
        self.users_list = self.get_all_users()


class Tasks:

    def __init__(self):
        self.table_name = 'tasks'
        self.col_table_names = {
            'id': 'INTEGER',
            'user_id' : 'INTEGER',
            'task_name' : 'TEXT',
            'description' : 'TEXT', 
            'category' : 'TEXT',
            'status' : 'INTEGER'
        }
        sql.add_table(self.table_name,self._create_columns_string_for_table())
        self.tasks_list = self.get_all_tasks()

    def _create_columns_string_for_table(self):
        return ','.join([
            f'{col} {type}' for col,type in self.col_table_names.items() if col != 'id'
            ]) 


    def get_all_tasks(self) -> list[Task]:
        if sql.is_table_exists(self.table_name):
            tasks = sql.fetch_all(self.table_name)
            if len(tasks) > 0:
                tasks_list = [
                    Task(task[0], task[1], task[2], task[3], task[4], task[5] == 1) for task in tasks
                    ]
                return tasks_list
        return []

    def add_task(self, user_id: int, task_name: str, description: str, category: int,status: int = 0) -> None:
        """ >>> \'the function automatically append to the tasks_list\'"""
        sql.add_field(self.table_name, user_id, task_name,description, category, status)
        self.tasks_list.insert(
            Task(sql.fetch_last_one(self.table_name)[0], user_id, task_name, description, category)
        )

    def get_task_by_id(self, id: int) -> Task:
        """be aware: >>> \if task id don't exist the function return -> None type !"""
        task = sql.fetch_by_id(self.table_name, id)
        if task == None:
            print('There is no task with this id...')
        else:
            return Task(task[0], task[1], task[2], task[3], task[4], task[5] == 1)

    def get_tasks_by_user_id(self, id: int) -> Task:
        tasks = sql.fetch_all_by_foreign_key(self.table_name, 'user_id', id)
        if tasks == None:
            print('There is no task for this user...')
            return []
        else:
            return [
                Task(task[0], task[1], task[2], task[3], task[4], task[5] == 1) for task in tasks
                ]

    def delete_task(self, id: int) -> None:
        """ >>> \'the function automatically refresh the tasks_list\'"""
        sql.delete_field(self.table_name, id)
        self.tasks_list = [task for task in self.tasks_list if task.id != id]

    def update_task(self, id_value: int, column_name: str, new_value: any) -> None:
        """ >>> \'the function automatically refresh the tasks_list\'"""
        sql.update_field(self.table_name,id_value,column_name,new_value)
        self.tasks_list = self.get_all_tasks()

    def get_tasks_by_family_id(self,family_id: int) -> list[Task]:
        users_family_id = [user.id for user in users.users_list if user.family_id == family_id]
        tasks_in_family = []
        for id in users_family_id:
            for task in  self.tasks_list:
                if task.user_id == id:
                    tasks_in_family.append(task)
        return tasks_in_family


families = Families()
users = Users()
tasks = Tasks()



# families.add_family('abravanel', 'YZ1436E')
# users.add_user(1,'david','abravanel',25)
# users.add_user(1,'hadar','abravanel',23)
# tasks.add_task(user_id=1,task_name='be a dad',description='to be a good dad',category=1)
# tasks.add_task(1,'be a mam','to be a good mam',1)
# tasks.update_task(2,'user_id',2)
# tasks.delete_task()

# families.update_family(1,'password','TTTTT2')
print(families.families_list)



# sql.add_table('families', 'family_name TEXT', 'password TEXT')
# sql.add_table('users', 'family_id INTEGER','first_name TEXT','last_name TEXT','status ', 'password TEXT')
# sql.add_table('tasks', 'user_id INTEGER', 'user_name TEXT', 'password TEXT')