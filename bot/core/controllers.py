from flask import Blueprint, render_template, request, redirect, abort, session
from bot.core.models import QuestionsAnswers
from bot.login_utils import login_required



core = Blueprint('core', __name__)

@core.route('/')
@login_required
def index():
    questions_answers_con = QuestionsAnswers()
    context = {
        'questions_answers': questions_answers_con.all(),
        'name': 'Idris'
    }
    return render_template('core/index.html', **context)

@core.route('/about/')
def about():
    return render_template('core/about.html')

@core.route('/create/', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        ques_anw_con = QuestionsAnswers()
        ques_anw_con.create(**request.form)
        return redirect('/')
    return render_template('core/create.html', )


@core.route('/update/<id>/', methods=['GET', 'POST'])
def update(id):
    if 'logined' not in  session or session['logined'] != True:
        return redirect('/login/')
    ques_anw_con = QuestionsAnswers()
    ques_anw = ques_anw_con.get(id)
    if ques_anw == None:
        abort(404)
    if request.method == 'POST':
        ques_anw_con.update(id=id, **request.form)
        return redirect('/')
    context = {
        'ques_anw': ques_anw
    }
    return render_template('core/update.html', **context)


@core.route('/delete/<id>/', methods=['GET'])
def delete(id):
    ques_anw_con = QuestionsAnswers()
    ques_anw = ques_anw_con.get(id)
    if ques_anw == None:
        abort(404)
    ques_anw_con.delete(id)
    return redirect('/')