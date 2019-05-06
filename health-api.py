from flask import Flask
import json, time, os

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Health API'

@app.route('/api/v1/ls')
def get_ls():
    result = { 'command':'ls',
               'stdout': str(os.popen('ls -lah').read())
             }
    return json.dumps(result)

@app.route('/api/v1/ps')
def get_ps():
    result = { 'command':'ps aux',
               'stdout': str(os.popen('ps aux').read())
             }
    return json.dumps(result)
