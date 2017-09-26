from flask import Flask, render_template

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return "Hi everybody!"

@my_app.route('/occupations')
def occupations():
    return "foo!"



if __name__ == '__main__':
    my_app.debug = True;
    my_app.run()
