from flask import Blueprint, render_template
from .forms import RegisterForm
from .models import *

auth = Blueprint('auth', __name__)

@auth.route('/login/', methods=['GET', 'POST'])
def login_page():
    return render_template('auth/login.html')


@auth.route('/register/', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        create_user(form.username.data, form.email.data, form.name.data, form.surname.data, form.password.data)
    context = {
        'register_form': form
    }
    return render_template('auth/register.html', **context)

