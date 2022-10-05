from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    name = request.args.get('nombre')
    if (name):
        message = "Hola '" + name + "' desde Python!"
    else:
        message = "Hola desde Python!"
    return message

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
