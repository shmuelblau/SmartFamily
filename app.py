from flask import Flask, render_template, request, jsonify, url_for, redirect, session
from example_sql import *


app = Flask(__name__)


@app.route('/')
def start():
    return redirect(url_for('home'))


@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        name_family = request.form['name_family']
        code1 = request.form['code1']
        code2 = request.form['code2']
        familys.append(Family(len(familys)+1, name_family))
        users.append(User(len(users)+1, len(familys),'אבא', name_family, code1))
        users.append(User(len(users)+1, len(familys),'אמא', name_family, code2))

    return render_template('home.html', familys=familys)


@app.route('/family/<idfamily>', methods=['POST', 'GET'])
def family(idfamily):

    this_family = sort.get_family_by_id(idfamily)
    users_family = sort.get_users_by_family_id(idfamily)
    family_tasks = sort.get_tasks_by_user_id(idfamily)
    if request.method == 'POST':
        print('post')
        print(request.form['nam'])
        print(request.form['code'])

        for user in users_family:
            print(2222, request.form['nam'])
            print(request.form['code'], str(user.password))
            if request.form['nam'] == user.Fname and request.form['code'] == str(user.password):
                print('pass')
                return redirect(url_for('kids', user=user))
            
    return render_template('family.html', this_family=this_family,  users_family=users_family,  family_tasks=family_tasks)


@app.route('/kids/<user>', methods=['POST', 'GET'])
def kids(user):
    print(user, 2)
    return render_template('kids.html', user=user, i=22)


if __name__ == ('__main__'):
    app.run(debug=True)
