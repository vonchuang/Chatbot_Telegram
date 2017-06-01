import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '322599923:AAHIazqINym8NneZTc6Q_lc35ACURQp-3FE'
WEBHOOK_URL = 'https://dd3bfba1.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'initial','final',
        'picture1','picture2','picture3','picture4','picture5','picture6',
        'audio1','audio2','audio3', 'audio4','audio5',
        'background1'
    ],
    transitions=[
        #picture
        {
            'trigger': 'advance',
            'source': 'initial',
            'dest': 'picture1',
            'conditions': 'is_going_to_picture1'
        },
        {
            'trigger': 'advance',
            'source': 'picture1',
            'dest': 'picture2',
            'conditions': 'is_going_to_picture2'
        },
        {
            'trigger': 'advance',
            'source': 'picture2',
            'dest': 'picture3',
            'conditions': 'is_going_to_picture3'
        },
        {
            'trigger': 'advance',
            'source': 'picture3',
            'dest': 'picture4',
            'conditions': 'is_going_to_picture4'
        },
        {
            'trigger': 'advance',
            'source': 'picture4',
            'dest': 'picture5',
            'conditions': 'is_going_to_picture5'
        },
        {
            'trigger': 'advance',
            'source': 'picture5',
            'dest': 'picture6',
            'conditions': 'is_going_to_picture6'
        },
        {
            'trigger': 'advance',
            'source': 'picture6',
            'dest': 'final',
            'conditions': 'is_going_to_final'
        },
        #audio
        {
            'trigger': 'advance',
            'source': 'initial',
            'dest': 'audio1',
            'conditions': 'is_going_to_audio1'
        },
        {
            'trigger': 'advance',
            'source': 'audio1',
            'dest': 'audio2',
            'conditions': 'is_going_to_audio2'
        },
        {
            'trigger': 'advance',
            'source': 'audio2',
            'dest': 'audio3',
            'conditions': 'is_going_to_audio3'
        },
        {
            'trigger': 'advance',
            'source': 'audio3',
            'dest': 'audio4',
            'conditions': 'is_going_to_audio3'
        },
        {
            'trigger': 'advance',
            'source': 'audio4',
            'dest': 'audio5',
            'conditions': 'is_going_to_audio3'
        },

        {
            'trigger': 'advance',
            'source': 'audio5',
            'dest': 'final',
            'conditions': 'is_going_to_final'
        },

        #background
        {
            'trigger': 'advance',
            'source': 'initial',
            'dest': 'background1',
            'conditions': 'is_going_to_background1'
        },
        {
            'trigger': 'advance',
            'source': 'background1',
            'dest': 'background2',
            'conditions': 'is_going_to_final'
        },

        #go back
        {
            'trigger': 'advance',
            'source': [
                'picture1','picture2','picture3','picture4','picture5','picture6',
                'audio1','audio2','audio3', 'audio4','audio5',
                'background1'
            ],
            'dest': 'initial',
            'conditions': 'is_going_back'
        }
    ],
    initial='initial',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
    machine.get_graph().draw('fsm_state_diagram.png', prog='dot')

