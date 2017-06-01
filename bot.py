import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = 'Your Telegram API Token'
WEBHOOK_URL = 'Your Webhook URL'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'initial',
        'sheng', 'dorm',
        'cheng', 'cheng1', 'cheng2', 'cheng3', 'cheng4', 'cheng5', 'cheng6', 'cheng7',
        'koan', 'koan1', 'koan2', 'koan3', 'koan4', 'koan5', 'koan6',
        'zi', 'zi1', 'zi2', 'zi3'
    ],
    transitions=[
        #sheng
        #=========== up ======================
        {
            'trigger': 'advance',
            'source': 'initial',
            'dest': 'sheng',
            'conditions': 'is_going_to_sheng'
        },
        {
            'trigger': 'advance',
            'source': 'sheng',
            'dest': 'initial',
            'conditions': 'sheng_back_to_initial'
        },
        {
            'trigger': 'advance',
            'source': 'sheng',
            'dest': 'dorm',
            'conditions': 'is_going_to_dorm'
        },

        #=========== down ======================
        {
            'trigger': 'advance',
            'source': 'dorm',
            'dest': 'sheng',
            'conditions': 'is_going_back_sheng'
        },


        #cheng
        #=========== up ======================
        {
            'trigger': 'advance',
            'source': 'initial',
            'dest': 'cheng',
            'conditions': 'is_going_to_cheng'
        },
        {
            'trigger': 'advance',
            'source': 'cheng',
            'dest': 'initial',
            'conditions': 'cheng_back_to_initial'
        },
        {
            'trigger': 'advance',
            'source': 'cheng',
            'dest': 'cheng1',
            'conditions': 'is_going_to_cheng1'
        },
        {
            'trigger': 'advance',
            'source': 'cheng1',
            'dest': 'cheng2',
            'conditions': 'is_going_to_cheng2'
        },
        {
            'trigger': 'advance',
            'source': 'cheng2',
            'dest': 'cheng3',
            'conditions': 'is_going_to_cheng3'
        },
        {
            'trigger': 'advance',
            'source': 'cheng3',
            'dest': 'cheng4',
            'conditions': 'is_going_to_cheng4'
        },
        {
            'trigger': 'advance',
            'source': 'cheng4',
            'dest': 'cheng5',
            'conditions': 'is_going_to_cheng5'
        },
        {
            'trigger': 'advance',
            'source': 'cheng5',
            'dest': 'cheng6',
            'conditions': 'is_going_to_cheng6'
        },
        {
            'trigger': 'advance',
            'source': 'cheng6',
            'dest': 'cheng7',
            'conditions': 'is_going_to_cheng7'
        },

        #=========== down ======================
        {
            'trigger': 'advance',
            'source': 'cheng1',
            'dest': 'cheng',
            'conditions': 'is_going_back_cheng'
        },
        {

            'trigger': 'advance',
            'source': 'cheng2',
            'dest': 'cheng1',
            'conditions': 'is_going_back_cheng1'
        },
        {
            'trigger': 'advance',
            'source': 'cheng3',
            'dest': 'cheng2',
            'conditions': 'is_going_back_cheng2'
        },
        {
            'trigger': 'advance',
            'source': 'cheng4',
            'dest': 'cheng3',
            'conditions': 'is_going_back_cheng3'
        },
        {
            'trigger': 'advance',
            'source': 'cheng5',
            'dest': 'cheng4',
            'conditions': 'is_going_back_cheng4'
        },
        {
            'trigger': 'advance',
            'source': 'cheng6',
            'dest': 'cheng5',
            'conditions': 'is_going_back_cheng5'
        },
        {
            'trigger': 'advance',
            'source': 'cheng7',
            'dest': 'cheng6',
            'conditions': 'is_going_back_cheng6'
        },



        #koan
        #=========== up ======================
        {
            'trigger': 'advance',
            'source': 'initial',
            'dest': 'koan',
            'conditions': 'is_going_to_koan'
        },
        {
            'trigger': 'advance',
            'source': 'koan',
            'dest': 'initial',
            'conditions': 'koan_back_to_initial'
        },
        {
            'trigger': 'advance',
            'source': 'koan',
            'dest': 'koan1',
            'conditions': 'is_going_to_koan1'
        },
        {
            'trigger': 'advance',
            'source': 'koan1',
            'dest': 'koan2',
            'conditions': 'is_going_to_koan2'
        },
        {
            'trigger': 'advance',
            'source': 'koan2',
            'dest': 'koan3',
            'conditions': 'is_going_to_koan3'
        },
        {
            'trigger': 'advance',
            'source': 'koan3',
            'dest': 'koan4',
            'conditions': 'is_going_to_koan4'
        },
        {
            'trigger': 'advance',
            'source': 'koan4',
            'dest': 'koan5',
            'conditions': 'is_going_to_koan5'
        },
        {
            'trigger': 'advance',
            'source': 'koan5',
            'dest': 'koan6',
            'conditions': 'is_going_to_koan6'
        },

        #=========== down ======================
        {
            'trigger': 'advance',
            'source': 'koan1',
            'dest': 'koan',
            'conditions': 'is_going_back_koan'
        },
        {
            'trigger': 'advance',
            'source': 'koan2',
            'dest': 'koan1',
            'conditions': 'is_going_back_koan1'
        },
        {
            'trigger': 'advance',
            'source': 'koan3',
            'dest': 'koan2',
            'conditions': 'is_going_back_koan2'
        },
        {
            'trigger': 'advance',
            'source': 'koan4',
            'dest': 'koan3',
            'conditions': 'is_going_back_koan3'
        },
        {
            'trigger': 'advance',
            'source': 'koan5',
            'dest': 'koan4',
            'conditions': 'is_going_back_koan4'
        },
        {
            'trigger': 'advance',
            'source': 'koan6',
            'dest': 'koan5',
            'conditions': 'is_going_back_koan5'
        },
      
        #zi
        #=========== up ======================
        {
            'trigger': 'advance',
            'source': 'initial',
            'dest': 'zi',
            'conditions': 'is_going_to_zi'
        },
        {
            'trigger': 'advance',
            'source': 'zi',
            'dest': 'initial',
            'conditions': 'zi_back_to_initial'
        },

         {
            'trigger': 'advance',
            'source': 'zi',
            'dest': 'zi1',
            'conditions': 'is_going_to_zi1'
        },
         {
            'trigger': 'advance',
            'source': 'zi1',
            'dest': 'zi2',
            'conditions': 'is_going_to_zi2'
        },
         {
            'trigger': 'advance',
            'source': 'zi2',
            'dest': 'zi3',
            'conditions': 'is_going_to_zi3'
        },
           
        #=========== down ======================
        {
            'trigger': 'advance',
            'source': 'zi1',
            'dest': 'zi',
            'conditions': 'is_going_back_zi'
        },
         {
            'trigger': 'advance',
            'source': 'zi2',
            'dest': 'zi1',
            'conditions': 'is_going_back_zi1'
        },
         {
            'trigger': 'advance',
            'source': 'zi3',
            'dest': 'zi2',
            'conditions': 'is_going_back_zi2'
        },

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

