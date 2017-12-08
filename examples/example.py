from gevent import monkey; monkey.patch_all()  # noqa

import logging
import time

from watchdog_gevent import Observer
from watchdog.events import LoggingEventHandler

from threading import Thread

logging.basicConfig(level=logging.DEBUG)

running = True


def printer():
    global running
    logger = logging.getLogger("printer")
    while running:
        logger.info("Ping!")
        time.sleep(1)


try:
    pinger = Thread(target=printer)
    pinger.start()

    observer = Observer()
    observer.schedule(LoggingEventHandler(), ".", recursive=True)
    observer.start()

    while True:
        time.sleep(1)
except KeyboardInterrupt:
    running = False
    observer.stop()

observer.join()
