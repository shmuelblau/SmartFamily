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
    family_tasks = tasks.get_tasks_by_user_id(users_family[0][0])

    
#     if request.method == 'POST':
#         print('post')
#         print(request.form['nam'])
#         print(request.form['code'])

#         for user in users_family:
#             print(2222, request.form['nam'])
#             print(request.form['code'], str(user.password))
#             if request.form['nam'] == user.Fname and request.form['code'] == str(user.password):
#                 print('pass')
#                 return redirect(url_for('kids', user=user))
            
    return render_template('family.html', this_family=this_family,  users_family=users_family,  family_tasks=family_tasks)


# @app.route('/kids/<user>', methods=['POST', 'GET'])
# def kids(user):
#     print(user, 2)
#     return render_template('kids.html', user=user, i=22)


if __name__ == ('__main__'):
    app.run(debug=True)
