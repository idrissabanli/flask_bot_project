from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login/', methods=['GET', 'POST'])
def login_page():

    return render_template('auth/login.html')


@auth.route('/register/', methods=['GET', 'POST'])
def register_page():
    
    return render_template('auth/register.html')

