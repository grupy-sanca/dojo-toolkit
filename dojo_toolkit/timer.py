import time


try:
    input = raw_input
except NameError:
    pass


def dojo_timer(notifier, round_time, sound_player):
    """Wait the defined and then shows notification and waits
    for replace
    """
    is_start = True
    while True:
        if not is_start:
            notifier.notify('Time Up', timeout=15 * 1000)
            sound_player.play_timeup()
            print('Press Enter when replaced')
            input()
        time.sleep(round_time * 60)
        is_start = False
