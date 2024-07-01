from flask import Flask,render_template,request,jsonify, url_for , redirect,session
from example_sql import familys, passwords
app=Flask(__name__)

@app.route('/')
def start():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    
    return render_template('home.html')
    
if __name__ == ('__main__'):
    app.run(debug=True)

