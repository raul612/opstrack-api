from flask import Flask

app = Flask(__name__)


@app.route('/status')
def status():
    return {'servico': 'OpsTrackAPI', 'status': 'online'}


@app.route('/tickets')
def tickets():
    return {'tickets': []}


@app.route('/sobre')
def sobre():
    return {'nome': 'OpsTrack API'}


if __name__ == "__main__":
    app.run(debug=True)
