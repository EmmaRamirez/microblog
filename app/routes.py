from flask import render_template, flash, redirect, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
  user = { 'username': 'Emma' }
  posts = [
    {
      'author': {'username': 'Emma' },
      'body': 'Beautiful Day in Boulder!'
    },
    {
      'author': {'username': 'Susan'},
      'body': 'The Avengers Movie was OK'
    }
  ]
  return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requrested for user {}, remember_me={}'.format(
      form.username.data, form.remember_me.data
    ))
    return redirect(url_for('index'))
  return render_template('login.html', title='Sign In', form=form)