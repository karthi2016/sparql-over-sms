import services

from flask import request
from injector import inject
from webapi import app
from webapi.helpers.responses import *


@inject(configmanager=services.ConfigManager)
@app.route('/configurations', methods=['GET'])
def retreive_configurations(configmanager):
    names = configmanager.get_configurations()
    return ok(names)


@inject(configmanager=services.ConfigManager)
@app.route('/configuration/<name>', methods=['GET'])
def retreive_configuration(configmanager, name):
    config = configmanager.get_configuration(name)
    return ok(config)


@inject(configmanager=services.ConfigManager)
@app.route('/configuration/<name>/<section>', methods=['GET'])
def retreive_configurationsection(configmanager, name, section):
    section = configmanager.get_configurationsection(name, section)
    return ok(section)


@inject(configmanager=services.ConfigManager)
@app.route('/configuration/<name>/<section>', methods=['PUT'])
def update_configuration(configmanager, name, section):
    keyvaluepairs = request.get_json()
    configmanager.update_configuration(name, section, keyvaluepairs)

    return nocontent()


