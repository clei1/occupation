from flask import Flask, render_template
from utils import occupation

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return 'Hi everybody!'

@my_app.route('/occupations')
def occupations():
    return render_template('template.html', title="Occupations Generator", descriptive_heading="Occupations Generator", collection = occupation.dictionary(), occupation = occupation.occupationGenerator())

if __name__ == '__main__':
    my_app.debug = True;
    my_app.run()
