from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    return render_template("index.html", username='', error_username='', password='', error_password='', verify_password = '', error_verify_password='', email='', error_email='')

@app.route("/", methods=['POST'])
def print_form_value():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    error_username = ''
    error_password = ''
    error_email = ''
    error_verify_password=''

    if len(username) < 3 or len(username) > 20:
        error_username = "That's not a valid username"
        username= ''
    
    if len(password) < 3 or len(password) > 20:
        error_password = "That's not a valid password"
        password = ''
    
    if password != verify_password:
        error_verify_password = "Passwords don't match"
        verify_password = ''

    if email.count("@")!=1 or email.count(".")!=1 or email.count(" ")!=0:
        error_email = "That's not a valid email"
        email = ''


    if not error_username and not error_password and not error_verify_password and not error_email:
        username = request.form['username']
        return render_template('welcome-page.html', username=username)


    else:
        return render_template("index.html", username=username, email=email,error_username=error_username, error_password=error_password, error_verify_password=error_verify_password, error_email=error_email)


       




    
app.run()
