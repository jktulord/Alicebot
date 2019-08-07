from flask import Flask, request
import os
from db import set_state, get_state, set_firstname, set_lastname, set_phonenumber

app = Flask(__name__)


@app.route('/', methods=['POST'])
def echo():
#    command = request.json["command"].split()
#    command_len = len(command.split())
#    response_text = ' '
#    if command_len == 0:
#    elif command_len == 1:
#        if command == command[::-1]:
#        response_text = 'Word is mirrorlike'
#    else:
#        response_text = 'Word is not mirrorlike'
#else:
#   response_text = 'too many words'


    response_text = 'I dont understand you!'



    user_id = request.json['session']['user_id']
    state = get_state(user_id)

    if state == 0:
        response_text = 'Hi! What is your FirstName?'
        set_state(user_id, 1)
    elif state == 1:
        set_firstname(user_id,request.json['command'])
        response_text = 'And what is your LastName?'
        set_state(user_id, 2)

    elif state == 2:
        set_lastname(user_id,request.json['command'])
        response_text = 'And what is your PhoneNumber?'
        set_state(user_id, 3)

    elif state == 3:
        set_phonenumber(user_id,request.json['command'])
        response_text = 'Thank for your time! Bye!'
        set_state(user_id, 4)

    elif state == 4:
        response_text = 'bye!bye!'

    response = {
        'version': request.json['version'],
        'session': request.json['session'],
        'response':{
            'text':response_text
        }
    }

    return response


app.run(host='0.0.0.0', post=os.getenv('PORT',5000))