from flask import Flask
from math import sqrt

app = Flask(__name__)


@app.route('/')
def hello_world():
    num = (13**3) * sqrt(3)
    return '13^3 * sqrt(3) = ' + str(num)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
