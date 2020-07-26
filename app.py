from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = "ohsosecret1234"
debug = DebugToolbarExtension(app)


@app.route('/')
def get_words():
    """Shows Madlibs home page with form to ask for words"""
    prompts = story.prompts
    return render_template('form.html', prompts=prompts)


@app.route('/story')
def show_story():
    """Shows Madlibs story using form input"""
    answers = request.args

    story_text = story.generate(answers)
    return render_template('story.html', story_text=story_text)
