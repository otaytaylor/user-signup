from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('user-signup.html')

@app.route("/signup", methods=['POST'])
def validation():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''


    if len(username) > 20 or len(username) < 3 or username =='':
        username_error = 'Invalid username. Please enter a username between 3-20 characters with no spaces.'
        username = ''
    else:
        username = username

    if len(password) > 20 or len(password) < 3 or password=='' or '' in password:
        password_error = 'Invalid Password. Please enter a password between 3-20 characters with no spaces.'


    if verify_password != password or verify_password == '':
        verify_password_error = 'Password Must match!'


    if email != '':
        if '@' not in email or '.' not in email:
            email_error = "Invalid email address.  Please re-enter"
            email = ''
        if len(email) < 6:
            email_error = "Invalid email address.  Please re-enter."
            email = ''
        else:
            email = email

    if not username_error and not password_error and not verify_password_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('user-signup.html',
                                username = username,
                                username_error=username_error,
                                password_error=password_error,
                                verify_password_error=verify_password_error,
                                email_error=email_error,
                                email=email)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', user=username)



app.run()
