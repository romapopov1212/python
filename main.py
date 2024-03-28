from flask import Flask, render_template, request, redirect, flash, url_for, session
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "940de518c4678b186e152b3becd8cf0f"
posts = [
    {
        'author': 'Popov Roman',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'May 20, 2024'
    }
]


@app.route("/")
def index():
    return render_template("home.html", posts = posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/regist", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for("index"))
    return render_template("regist.html", form = form)


@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'popovrromma@gmail.com' and form.password.data == '12345678':
            flash("you have been loggen in!", 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid', 'danger')
    return render_template("login.html", form = form)


if __name__ == "__main__":
    app.run(debug=True)