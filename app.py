from flask import Flask
app = Flask(__name__)


@app.route('/')
def concierge_service():
    return 'python app.py ... concierge_service()'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
