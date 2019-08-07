from flask import Flask, request
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def echo():
    command = request.json["command"].split()
    command_len = len(command.split())
    response_text = ' '
    if command_len == 0:
        response_text = 'Hi!'
    elif command_len == 1:
        if command == command[::-1]:
            response_text = 'Word is mirrorlike'
        else:
            response_text = 'Word is not mirrorlike'
    else:
        response_text = 'too many words'

    response = {
        'version': request.json['version'],
        'session': request.json['session'],
        'response':{
            'text':response_text
        }
    }

    return response


app.run(host='0,0.0.0',post=os.getenv('PORT',5000))