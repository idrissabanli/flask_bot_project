from flask import redirect, session, request

def login_required(f):
    def wrapper(*args, **kwargs):
        print('urlllllll=', )
        if 'logined' not in  session or session['logined'] != True:
            return redirect(f'/login/?next={request.full_path}')
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper