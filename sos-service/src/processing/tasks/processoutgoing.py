from processing import app

@app.task
def example(messageid):
    return messageid * messageid