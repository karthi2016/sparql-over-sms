import configparser
import glob
import os

from webapi import app

# load configuration
configuration = glob.glob('configuration/*.conf')
for file in configuration:
    config = configparser.ConfigParser()
    config.read(file)

    # use filename as key
    key = 'c_{0}'.format(os.path.splitext(os.path.basename(file))[0])
    app.config[key] = config

# start application
app.run()
