from threading import Thread
from sos_server import run_server
from sos_worker import run_worker

if __name__ == '__main__':
    Thread(target = run_server).start()
    Thread(target = run_worker).start()