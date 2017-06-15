from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('signup_form.html')


@app.route('/signup')
def display_signup_form():
    return render_template('signup_form.html', username='', username_error='', password_error='')



@app.route('/signup', methods=['POST'])
def validate_signup():

    username = request.form['username']
    password = request.form['password']
    password_verify = request.form['password_verify']
    email = request.form['email']

    password_error = ''
    username_error = ''
    password_verify_error = ''
    email_error = ''

    if username == '':
        username_error = 'Field can not be left empty'


    if password == '':
        password_error = 'Password is empty'


    if len(username) < 3 or len(username) > 20:
        username_error = 'Invaild username'


    if len(password) < 3 or len(password) > 20:
        password_error = 'Invaild password'


    if password != password_verify:
        password_verify_error = 'Passwords do not match'

    if email == '':
        email = email
    else:
        if len(email) <3 or len(email) > 20:
         email_error = 'invaild email'
    
    if not username_error and not password_verify_error:
        # username = username
        return redirect('/vaild-signup?username={0}'.format(username))
    else:

        return render_template('signup_form.html', username=username, password_error=password_error, username_error=username_error, password=password, password_verify_error=password_verify_error) 
        


@app.route('/vaild-signup', methods=['GET'])
def vaild_signup():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()