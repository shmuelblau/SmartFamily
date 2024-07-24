from flask import Flask, render_template, request, jsonify, url_for, redirect, session
from sql_maneger import families,users,tasks
from static.database.sql_management import sql


app = Flask(__name__)


@app.route('/')
def start():
    return redirect(url_for('home'))


@app.route('/home', methods=['POST', 'GET'])
def home():
    
    if request.method == 'POST':
        family_name = request.form['family_name']
        print(family_name)
        code1 = request.form['code1']
        code2 = request.form['code2']
        families.add_family(str(family_name),'11111')
        users.add_user(sql.fetch_last_one(families.table_name)[0],'Father', family_name, 27, code1)
        users.add_user(sql.fetch_last_one(families.table_name)[0],'Mather', family_name, 28, code2)

        return redirect(url_for('home'))

    return render_template('home.html', families=families.families_list)


@app.route('/family/<idfamily>', methods=['POST', 'GET'])
def family(idfamily):

    this_family = families.get_family_by_id(idfamily)
    users_family = users.get_users_by_family_id(idfamily)
    family_tasks = tasks.get_tasks_by_family_id(this_family.id)
    
    
    if request.method == 'POST':
         this_family = families.get_family_by_id(idfamily)
         users_family = users.get_users_by_family_id(idfamily)
         family_tasks = tasks.get_tasks_by_family_id(this_family.id)
#         print('post')
         print(request.form['user_name'])
         print(request.form['code'])
         for user in users_family:
             print(user.first_name,'   ',request.form['user_name'])
             print(user.password,'   ',request.form['code'])
#            print(2222, request.form['nam'])
#            print(request.form['code'], str(user.password))
             if request.form['user_name'].lower() == user.first_name.lower() and request.form['code'] == str(user.password):
                 print("עבר ראשון")
                 if user.first_name.lower()=='Father'.lower() or user.first_name.lower()=='Mather'.lower():
                      print("עבר שנין")
                      return redirect(url_for('parents', user_id=user.id))

                 return redirect(url_for('kids', user_id=user.id))

            
    return render_template('family.html', this_family=this_family,  users_family=users_family,  family_tasks=family_tasks)



@app.route('/parents/<user_id>', methods=['POST', 'GET'])
def parents(user_id):
    this_user=users.get_user_by_id(user_id)
    users_family=users.get_users_by_family_id(this_user.family_id)
    family_tasks=tasks.get_tasks_by_family_id(this_user.family_id)
    
    return render_template('parents.html', this_user=this_user,  users_family=users_family,  family_tasks=family_tasks)

@app.route('/kids/<user_id>', methods=['POST', 'GET'])
def kids(user_id):
    this_user=users.get_user_by_id(user_id)
    
    user_tasks=tasks.get_tasks_by_user_id(user_id)

    open_user_tasks=[task for task in user_tasks if task.status == False]

    return render_template('kids.html',this_user=this_user,user_tasks=user_tasks,open_user_tasks=open_user_tasks)


@app.route('/add_kids/<user_id>', methods=['POST'])
def add_kids(user_id):
    user=users.get_user_by_id(user_id)
    
    family=families.get_family_by_id(user.family_id)
    users.add_user(family.id,request.form['name'],family.family_name, request.form['age'],request.form['password'])
    

    return redirect(url_for('parents',user_id=user_id))
    
@app.route('/add_task/<user_id>', methods=['POST'])
def add_task(user_id):

    tasks.add_task(request.form['name'],request.form['task_name'],request.form['data'],0)


    return redirect(url_for('parents',user_id=user_id))


@app.route('/mark_as_done/<task_id>/<user_id>', methods=['POST'])
def mark_as_done(task_id,user_id):
    print(tasks.get_task_by_id(task_id).status, "לפני")

    tasks.update_task(task_id,"status",1)
    print(tasks.get_task_by_id(task_id).status, "אחרי")

    return redirect(url_for('kids',user_id=user_id))




# @app.route('/kids/<user>', methods=['POST', 'GET'])
# def kids(user):
#     print(user, 2)
#     return render_template('kids.html', user=user, i=22)


if __name__ == ('__main__'):
    app.run(debug=True)
