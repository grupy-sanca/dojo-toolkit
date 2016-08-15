import time


def dojo_timer(notifier, round_time):
    """Wait the defined and then shows notification and waits
    for replace
    """
    while True:
        notifier.notify('Time Up', timeout=15 * 1000)
        print("\033c")
        input('Press Enter when replaced')
        time.sleep(round_time * 60)
