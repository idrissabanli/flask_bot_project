from flask import Blueprint, render_template
from bot.core.models import QuestionsAnswers

core = Blueprint('core', __name__)

@core.route('/')
def index():
    con = QuestionsAnswers()
    print(con.get_questions_answers())
    return render_template('core/index.html', name="Idris")

@core.route('/about/')
def about():
    return render_template('core/about.html')
