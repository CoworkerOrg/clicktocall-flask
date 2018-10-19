from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import url_for
from flask_sslify import SSLify

from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client

# Declare and configure application
app = Flask(__name__, static_url_path='/static')
sslify = SSLify(app)
app.config.from_pyfile('local_settings.py')

# Route for Click to Call demo page.
@app.route('/')
def index():
    return render_template('index.html',
                           configuration_error=None)

@app.route('/data-use')
def data_use():
    return render_template('data-use.html',
                           configuration_error=None)

# Voice Request URL
@app.route('/call', methods=['POST'])
def call():
    # Get phone number that was submitted in the form
    phone_number = request.form.get('phoneNumber', None)

    try:
        twilio_client = Client(app.config['TWILIO_ACCOUNT_SID'],
                               app.config['TWILIO_AUTH_TOKEN'])
    except Exception as e:
        msg = 'Missing configuration variable: {0}'.format(e)
        return jsonify({'error': msg})

    try:
        twilio_client.calls.create(from_=app.config['TWILIO_CALLER_ID'],
                                   to=phone_number,
                                   url=url_for('.outbound',
                                               _external=True))
    except Exception as e:
        app.logger.error(e)
        return jsonify({'error': str(e)})

    return jsonify({'message': 'Call incoming!'})


@app.route('/outbound', methods=['POST'])
def outbound():
    script = "We're connecting you right now."
    dial_to = "+15555555555"

    response = VoiceResponse()
    response.say(script, voice='alice')
    response.dial(dial_to)
    return str(response)
