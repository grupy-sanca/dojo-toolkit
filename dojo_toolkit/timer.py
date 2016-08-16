import time


def dojo_timer(notifier, round_time):
    """Wait the defined and then shows notification and waits
    for replace
    """
    while True:
        notifier.notify('Time Up', timeout=15 * 1000)
        print("\033c")
        print('Press Enter when replaced')
        raw_input()
        time.sleep(round_time * 60)
