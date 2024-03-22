from flask import Flask, render_template, url_for, flash, redirect
from forms import SignupForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '96e3ab3cdb6e61040b2d79b585d2cf8d'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f'Account created successfully', 'success')
        return redirect(url_for('home'))

    return render_template('signup.html', title='Sign Up', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #if
        flash('Logged in successfully', 'success')
        return redirect(url_for('home'))
        #else:
        #    flash('Invalid credentials', 'danger')

    return render_template('login.html', title='Log In', form=form)

if __name__ == '__main__':
    app.run(debug=True)