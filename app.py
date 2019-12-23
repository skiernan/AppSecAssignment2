from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import Form, StringField, PasswordField, validators
from wtforms.validators import InputRequired, Length
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Itissecret'
session.cookie_httponly = 1

class RegistrationForm(FlaskForm):
	username = StringField('Username', id='uname', validators=[InputRequired(), Length=(min=4, max=16)])
	password = PasswordField('Password', id='pword', validators=[InputRequired(), Length=(min=8, max=80)]),validators.EqualTo('confirm', message='Passwords must match')])
	twofa = StringField(‘Phone', id='2fa', validators=[InputRequired()])
	submit = SubmitField('Register')

class LoginForm(FlaskForm):
	username = StringField('Username', id='uname', validators=[InputRequired(), Length=(min=4, max=16)])
	password = PasswordField('Password', id='pword', validators=[InputRequired(), Length=(min=8, max=80)]), validators.EqualTo('confirm', message='Passwords must match')])
	twofa = StringField(‘Phone', id='2fa', validators=[InputRequired()])
	submit = SubmitField('Login')

class SpellCheckForm(FlaskForm):
  input = TextAreaField("Input Word", id='input', validators=[DataRequired()])
	ouput = TextAreaField("Ouput Word", id='textout')
	misspelled = TextAreaField("Misspelled Word", id='misspelled')
	submit = SubmitField('Spell Check')

@app.route('/')
def index():
    return 'index'
                      
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.password.data, form.twofa.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login.html'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
form = LoginForm()
return render_template('login.html', form=form)  
                      error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_in_user(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

@app.route("/spell_check", methods=['GET','POST'])
def spell_check():
  
  return render_template('checker.html', error=error)

if __name__ == "__main__":
  app.run(debug=True)
