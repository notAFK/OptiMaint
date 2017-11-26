from flask import Flask


APP = Flask(__name__)


@APP.route("/")
def index():
    return "hello world"


if __name__ == "__main__":
    APP.run(threaded=True, debug=True)