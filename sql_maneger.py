import copy
from static.database import sql_management
from static.database.python_classes.family import Family
from static.database.python_classes.user import User
from static.database.python_classes.task import Task

Sql = sql_management.SqlManagement()


class Families:
    def __init__(self):
        self.table_name = 'families'
        self.col_table_names = {
            1: "id",
            2: 'family_name',
            3: 'password'
        }
        self.families_list = self.get_all_families()

    def get_all_families(self) -> list[Family]:
        Sql.open_db()
        if Sql.is_table_exists(self.table_name):
            families = Sql.fetch_all(self.table_name)
            if len(families) > 0:
                families_list = [Family(family[0], family[1], family[2]) for family in families]
                Sql.close_db()
                return families_list
        return []

    def add_family(self, family_name: str, password: str) -> None:
        Sql.add_field('families', family_name, password)
        self.families_list.append(
            Family(Sql.fetch_last_one('families')[0], family_name, password)
        )

    def get_family_by_id(self, id: int) -> Family:
        family = Sql.fetch_by_id('families', id)
        if family == None:
            print('the program crashed!\n  !!!  There is no family with this id...')
            exit()
        else:
            return Family(family[0], family[1], family[2])

    def delete_user(self, table_name: str, id: int) -> None:
        Sql.delete_field(table_name, id)
        self.families = [family for family in self.families if family.id != id]

    def update_field(self, table_name: str, id_value: int, column_name: str, new_value: any) -> None:
        pass


class Users:
    def __init__(self):
        self.table_name = 'users'
        self.col_table_names = {
            1: 'id',
            2: 'family_id',
            3: 'first_name',
            3: 'last_name',
            5: 'status',
            6: 'password'
        }
        self.users_list = self.get_all_users()

    def get_all_users(self) -> list[User]:
        Sql.open_db()
        if Sql.is_table_exists(self.table_name):
            users = Sql.fetch_all(self.table_name)
            if len(users) > 0:
                users_list = [User(user[0], user[1], user[2]) for user in users]
                Sql.close_db()
                return users_list
        return []

    def add_user(self, family_id: int, first_name: str, last_name: str, status: float, age: int, password: str) -> None:
        Sql.add_field(self.table_name, family_id, first_name,last_name, status, age, password)
        self.users_list.append(
            User(Sql.fetch_last_one(self.table_name)[0], family_id, first_name, last_name, age, password,)
        )

    def get_user_by_id(self, id: int) -> User:
        user = Sql.fetch_by_id(self.table_name, id)
        if user == None:
            print('the program crashed!\n  !!!  There is no user with this id...')
            exit()
        else:
            return User(user[0], user[1], user[2], user[3], user[4], user[5])

    def get_users_by_family_id(self, id: int) -> User:
        user = Sql.fetch_all_by_foreign_key(self.table_name, 'family_id', id)
        if user == None:
            print('the program crashed!\n  !!!  There is no user for this family...')
            exit()
        else:
            return User(user[0], user[1], user[2], user[3], user[4], user[5])

    def delete_user(self, table_name: str, id: int) -> None:
        Sql.delete_field(table_name, id)
        self.users_list = [user for user in self.users_list if user.id != id]

    def update_field(self, table_name: str, id_value: int, column_name: str, new_value: any) -> None:
        pass


class Tasks:
    def __init__(self):
        self.table_name = 'tasks'
        self.col_table_names = {
            1: 'id',
            2: 'user_id',
            3: 'task_name',
            4: 'description',
            5: 'category',
            6: 'status'
        }
        self.tasks_list = self.get_all_tasks()

    def get_all_tasks(self) -> list[Task]:
        Sql.open_db()
        if Sql.is_table_exists(self.tasks_table_name):
            tasks = Sql.fetch_all(self.tasks_table_name)
            if len(tasks) > 0:
                tasks_list = [Task(task[0], task[1], task[2]) for task in tasks]
                Sql.close_db()
                return tasks_list
        return []

    def add_task(self, user_id: int, task_name: str, description: str, category: int) -> None:
        Sql.add_field(self.table_name, user_id, task_name,description, category, False)
        self.tasks_list.append(
            Task(Sql.fetch_last_one(self.table_name)[0], user_id, task_name, description, category)
        )

    def get_task_by_id(self, id: int) -> Task:
        task = Sql.fetch_by_id(self.table_name, id)
        if task == None:
            print('the program crashed!\n  !!!  There is no task with this id...')
            exit()
        else:
            return Task(task[0], task[1], task[2], task[3], task[4], task[5])

    def get_tasks_by_user_id(self, id: int) -> Task:
        task = Sql.fetch_all_by_foreign_key(self.table_name, 'user_id', id)
        if task == None:
            print('There is no task for this user...')
            exit()
        else:
            return Task(task[0], task[1], task[2], task[3], task[4], task[5])

    def delete_task(self, id: int) -> None:
        Sql.delete_field(self.table_name, id)
        self.tasks_list = [task for task in self.tasks_list if task.id != id]

    def update_field(self, table_name: str, id_value: int, column_name: str, new_value: any) -> None:
        pass


Sql.open_db()
a = Sql.fetch_by_id('families', 4)
# Sql.add_table('families', 'family_name TEXT', 'password TEXT')
# Sql.add_field('families', 'abravanel', 'YZ1436E')
# Sql.delete_field('families',2)
Sql.close_db()
# for i in Families:
#     print(i)

# Sql.add_table('users', 'family_id INTEGER','family_name TEXT', 'password TEXT')
# Sql.add_table('tasks', 'user_id INTEGER', 'user_name TEXT', 'password TEXT')
# Sql.add_field('families', 'abravanel', 'YZ1436E')
# Sql.update_field('families',2,'password','TTTTT1')


# -> ready to delete >>>>>


# Sql.add_field('families', 'aabravanelich', 'YZ1436E')
# Sql.delete_field("families", 6)
# print(Sql.fetch())


# class Sort:

#     def __init__(self, familys, users, tasks):
#         self.__familys = familys
#         self.__users = users
#         self.__tasks = tasks

#     def get_family_by_id(self, id):
#         family = [family for family in self.__familys if family.id == id]
#         return family[0]

#     def get_user_by_id(self, id):
#         user = [user for user in self.__users if user.id == id]
#         return user[0]

#     def get_users_by_family_id(self, id):
#         return [user for user in self.__users if user.family_id == id]

#     def get_task_by_id(self, id):
#         task = [task for task in self.__tasks if task.id == id]
#         return task[0]

#     def get_tasks_by_user_id(self, id):
#         return [task for task in self.__tasks if task.user_id == id]


#     pass


# # temp databaes =>
# def temp():
#     names = ['david', 'nissim', 'pinhas', 'shmuel', 'haim', 'izthak', 'shlomo', 'yair', 'meir', 'natan']
#     familys_names = ['levi', 'khen', 'israel', 'blao']
#     tasks_names = ['add', 'throw', 'sleep']
#     familys_names = []
#     familys = []
#     users = []
#     tasks = []
#     i = j = k = 1

#     for family in familys_names:
#         familys.append(Family(i, family, 1436*i))

#         for name in names:
#             users.append(User(j, i, name, family, (1234*i)+j, 34//j))

#             for task in tasks_names:
#                 tasks.append(Task(k, j, task))

#                 k += 1
#             j += 1
#         i += 1

#     return familys, users, tasks


# familys, users, tasks = temp()
# sort = Sort(familys, users, tasks)


# def sssss():
#     for fam in familys:
#         print(fam.id, fam.family_name, fam.password)
