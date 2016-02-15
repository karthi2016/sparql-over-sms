from flask import Flask
from connectors.asterisk import AsteriskConnector
import configparser

app = Flask(__name__)


@app.route('/')
def hello():
    return "Semantic M2M is up-and-running"


@app.route('/sms')
def sms():
    contacts = configparser.ConfigParser()
    contacts.read('configuration/contacts.conf')

    config = configparser.ConfigParser()
    config.read('configuration/asterisk.conf')

    try:
        asterisk = AsteriskConnector(config, contacts)
        response = asterisk.send_sms('lyca01', 'hello world')
        return response.content
    except Exception as e:
        return e

if __name__ == "__main__":
    app.run()
