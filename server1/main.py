from flask import Flask, request


APP = Flask(__name__)

@APP.route("/", methods=['GET','POST'])
def hello_world():
    return "<p>Hello, World!</p>"


@APP.route("/sum/", methods=["POST"])
def return_sum():
    req = request.get_json(force=True)
    first_val = req.get('first_val')
    second_val = req.get('second_val')
    return str(first_val + second_val)

@APP.route("/subtract/", methods=["POST"])
def return_difference():
    req = request.get_json(force=True)
    first_val = req.get('first_val')
    second_val = req.get('second_val')
    return str(first_val - second_val)


@APP.route("/multiplication/", methods=["POST"])
def return_product():
    req = request.get_json(force=True)
    first_val = req.get('first_val')
    second_val = req.get('second_val')
    return str(first_val * second_val)


@APP.route("/division/", methods=["POST"])
def return_dividend():
    req = request.get_json(force=True)
    first_val = req.get('first_val')
    second_val = req.get('second_val')
    return str(first_val / second_val)

if __name__=="__main__":
    APP.run(debug=True)