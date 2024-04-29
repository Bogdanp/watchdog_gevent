import os
import subprocess
import time

from threading import Thread
from watchdog.events import (
    FileModifiedEvent,
    FileSystemEventHandler,
)
from watchdog_gevent import Observer


def rel(*path):
    return os.path.normpath(os.path.join(os.path.abspath(os.path.dirname(__file__)), *path))


def test_can_watch_for_changes_with_gevent():
    # Given a gevent-based thread that counts stuff and sleeps every second
    count = 0

    def counter():
        nonlocal count
        while True:
            count += 1
            time.sleep(1)

    counter_thread = Thread(target=counter, daemon=True)
    counter_thread.start()

    # And an event handler that gets notified when this file changes
    events = []

    class Handler(FileSystemEventHandler):
        def on_any_event(self, event):
            events.append(event)

    # And an observer that dispatches to that handler
    try:
        observer = Observer()
        observer.schedule(Handler(), rel(), recursive=True)
        observer.start()

        # When I touch this file
        subprocess.run(["touch", __file__])

        # And wait a second
        time.sleep(1)

        # Then the counter should have incremented
        assert count >= 2

        # And the event should have been observed
        assert events == [FileModifiedEvent(__file__)]
    finally:
        observer.stop()
        observer.join()
