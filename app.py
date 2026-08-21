from flask import Flask

app = Flask(__name__)

@app.route('/status')
def status():
    return {'servico': 'OpsTrackAPI', 'status': 'online'}

@app.route('/tickets')
def tickets():
    return {'tickets': []}

if __name__ == "__main__":
    app.run(debug=True)