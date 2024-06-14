from datetime import datetime, timedelta
import time
import threading

# Store events in a dictionary
events = {}


def add_event(name, event_datetime):
    """
    Adds an event to the calendar.
    :param name: Name of the event.
    :param event_datetime: datetime object of the event.
    """
    events[name] = event_datetime
    print(f"Event '{name}' added for {event_datetime}")


def notify_event(name, event_datetime):
    """
    Notifies when an event is due.
    :param name: Name of the event.
    :param event_datetime: datetime object of the event.
    """
    now = datetime.now()
    if now >= event_datetime:
        print(f"Notification: Event '{name}' is happening now!")
        return True
    return False


def check_events():
    """
    Check all events to see if they are due and notify.
    """
    while True:
        for name, event_datetime in events.items():
            notify_event(name, event_datetime)
        time.sleep(60)  # Check every minute


# Adding threading to run check_events in the background
event_checker_thread = threading.Thread(target=check_events)
event_checker_thread.daemon = True
event_checker_thread.start()

# Example of adding an event
event_time = datetime.now() + timedelta(seconds=10)  # 10 seconds from now
add_event('Sample Event', event_time)

# Keep the script running
while True:
    time.sleep(1)
