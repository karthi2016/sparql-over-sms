from flask import render_template
from webapi import app


@app.route('/')
def status():
    return render_template('system_status.html')




