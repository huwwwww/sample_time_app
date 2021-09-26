from flask import Flask
from time import gmtime, strftime
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def getTime():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
