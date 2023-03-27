from flask import Flask


application=Flask(__name__)


@application.route('/')
def index():
    return "<h1>Hello world 2</h1>"


if __name__=="__main__":
    application.run(host="0.0.0.0",port=8000,debug=False)