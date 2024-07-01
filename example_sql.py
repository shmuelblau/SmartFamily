class User:
    def __init__(self, id, family_id, Fname, Lname, password, age):
        self.id = id
        self.family_id = family_id
        # self.titel = titel
        self.Fname = Fname
        self.Lname = Lname
        self.password = password
        self.age = age


class Family:
    def __init__(self, id, Fname, password='0000'):
        self.id = id
        self.Fname = Fname
        self.password = password


class Task:
    def __init__(self, id, user_id, titel):
        self.id = id
        self.user_id = user_id
        self.titel = titel


class sort:
    pass


# temp databaes =>

def temp():
    names = ['david', 'nissim', 'pinhas', 'shmuel', 'haim', 'izthak', 'shlomo', 'yair', 'meir', 'natan']
    familys_names = ['levi', 'khen', 'israel', 'blao']
    tasks_names = ['add', 'throw', 'sleep']

    famliys = []
    users = []
    tasks = []
    i = j = k = 1

    for family in familys_names:
        famliys.append(Family(i, family, 1436*i))
        for name in names:
            users.append(User(j, i, name, family, (1234*i)+j, 34//j))
            for task in tasks_names:
                tasks.append(Task(k,j,task))
                k += 1
            j += 1
        i += 1

    return famliys,users,tasks

famliys,users,tasks = temp()
