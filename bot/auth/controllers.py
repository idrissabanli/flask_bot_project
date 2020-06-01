from flask import Blueprint, render_template, redirect
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
            print('user data:', user)
    context = {
        'login_form': form
    }
    return render_template('auth/login.html', **context)


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

