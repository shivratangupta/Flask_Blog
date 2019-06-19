from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '711d59da8f46a42fd155b7eb2e5cfea5'
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from models import User, Post



posts = [
		{
			'author' : 'Reyaan',
			'title' : 'Blog Post 1',
			'content' : 'First Post content',
			'date_posted' : 'June 15, 2019'
		},

		{
			'author' : 'Shriyan',
			'title' : 'Blog Post 2',
			'content' : 'Second Post content',
			'date_posted' : 'June 16, 2019'
		}
	]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts = posts)


@app.route("/about")
def about():
	return render_template('about.html', title = 'About')


@app.route("/register", methods = ['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title = 'Register', form = form)


@app.route("/login", methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if(form.validate_on_submit()):
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))

		else:
			flash('Wrong Username/Password!', 'danger')
			return redirect(url_for('login')	)
	return render_template('login.html', title = 'Login', form = form)



if __name__ == '__main__':
	app.run(debug = True)