from flask import Flask, request, redirect


app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!doctype html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}


        </style>
    </head>
    <body>
        <form method= 'POST'>
            <style>
                .error {{color:red;}}
            </style>
            <h1>Signup</h1>
            <label> Username
            <input name="username" type="text" value='{username}' />
            </label>
            <p class="error">{error_username}</p>

            <br/>

            <label> Password
            <input name="password" type="password" value='{password}' />
            </label>
            <p class="error">{error_password}</p>
            <br/>
                       

            <label> Verify Password
            <input name="verify_password" type="password" value='{verify_password}' />
            </label>
            <p class="error">{error_verify_password}</p>

            <br/>

            <label>Email (optional)
            <input name="email" type="text" value='{email}' />
            </label>
            <p class="error">{error_email}</p>

            <br/>
            <input type="submit"  />
        
        </form>
    </body>
</html>
"""


@app.route("/")
def index():
    return form.format(username='', error_username='', password='', error_password='', verify_password = '', error_verify_password='', email='', error_email='')

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

    # need the if and for loop to validate email, need to have @ . and space
    #for i in email():
        #if i != "@" or i =! "." or i =! " ":
    #if "@" not in email" or "." not in email or " " in email:
        #error_email = "That's not a valid email"
        #email = ''

    if not error_username and not error_password and not error_verify_password and not error_email:
        return redirect('/welcome-form')

    else:
        return form.format(error_username=error_username, error_password=error_password, error_verify_password=error_verify_password, error_email=error_email)


        #return '<h1> Welcome, ' + username + '!</h1>'


@app.route('/welcome-form')
def welcome_form():
    return '<h1> Welcome, ' + username + '!</h1>'

    
app.run()
