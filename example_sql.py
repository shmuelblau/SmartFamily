import copy
class User:
    def __init__(self, id, family_id, first_name, last_name, password, age):
        self.id = id
        self.family_id = family_id
        # self.titel = titel
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.age = age


class Family:
    def __init__(self, id, family_name, password='0000'):
        self.id = id
        self.family_name = family_name[0].upper()+family_name[1:]
        self.password = password


class Task:
    def __init__(self, id, user_id, titel):
        self.id = id
        self.user_id = user_id
        self.titel = titel


class Sort:

    def __init__(self, familys, users, tasks):
        self.__familys = familys
        self.__users = users
        self.__tasks = tasks

    def get_family_by_id(self, id):
        family = [family for family in self.__familys if family.id == id]
        return family[0]
     
    def get_user_by_id(self, id):
        user = [user for user in self.__users if user.id == id]
        return user[0]

    def get_users_by_family_id(self, id):
        return [user for user in self.__users if user.family_id == id]

    def get_task_by_id(self, id):
        task = [task for task in self.__tasks if task.id == id]
        return task[0]

    def get_tasks_by_user_id(self, id):
        return [task for task in self.__tasks if task.user_id == id]
    
    

    pass


# temp databaes =>
def temp():
    names = ['david', 'nissim', 'pinhas', 'shmuel', 'haim', 'izthak', 'shlomo', 'yair', 'meir', 'natan']
    familys_names = ['levi', 'khen', 'israel', 'blao']
    tasks_names = ['add', 'throw', 'sleep']
    familys_names = []
    familys = []
    users = []
    tasks = []
    i = j = k = 1

    for family in familys_names:
        familys.append(Family(i, family, 1436*i))

        for name in names:
            users.append(User(j, i, name, family, (1234*i)+j, 34//j))

            for task in tasks_names:
                tasks.append(Task(k, j, task))

                k += 1
            j += 1
        i += 1

    return familys, users, tasks


familys, users, tasks = temp()
sort = Sort(familys, users, tasks)


def sssss():
    for fam in familys:
        print(fam.id, fam.family_name, fam.password)



# your_project/
# ├── app.py
# ├── static/
# │   ├── css/
# │   │   └── style.css
# │   ├── js/
# │   │   └── script.js
# │   └── images/
# │       └── your_image.png
# └── templates/
#     └── home.html
