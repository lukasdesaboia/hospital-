from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Sistema Hospitalar Online"


@app.route("/pacientes")
def pacientes():
    return "Lista de pacientes"


if __name__ == "__main__":
    app.run(debug=True)
  #
  python app.py
#
http://127.0.0.1:5000
