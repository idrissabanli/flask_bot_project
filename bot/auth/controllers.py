from flask import Blueprint, render_template, redirect, session, request
from .forms import RegisterForm, LoginForm
from .models import *

auth = Blueprint('auth', __name__)

@auth.route('/login/', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        user = check_user_exists(form.username.data, form.password.data)
        if user:
            session['logined'] = True
            session['id'] = user['id']
            session['username'] = user['username']
            next_page = request.args.get('next', '/')
            return redirect(next_page)
    context = {
        'login_form': form
    }
    return render_template('auth/login.html', **context)

# | session_code| session_data|
# | 12233434234 | {logined: True, id: 1, username: idris} |


@auth.route('/logout/')
def logout():
    session['logined'] = False
    return redirect('/login/')

@auth.route('/register/', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        create_user(form.username.data, form.email.data, form.name.data, form.surname.data, form.password.data)
        return redirect('/login/')
    context = {
        'register_form': form
    }
    return render_template('auth/register.html', **context)

