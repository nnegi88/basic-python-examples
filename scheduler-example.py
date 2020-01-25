from datetime import datetime
import threading

def print_message(message):
    print('{} @ {}'.format(message, datetime.now().time()))

WAIT_SECONDS = 1

ticker = threading.Event()
while not ticker.wait(WAIT_SECONDS):
    print_message('Hello Scheduler!...')