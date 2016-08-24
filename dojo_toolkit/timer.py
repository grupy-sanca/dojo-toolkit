import time


try:
    input = raw_input
except NameError:
    pass


def dojo_timer(notifier, round_time, song_player):
    """Wait the defined and then shows notification and waits
    for replace
    """
    while True:
        notifier.notify('Time Up', timeout=15 * 1000)
        song_player.play_timeup()
        print('Press Enter when replaced')
        input()
        time.sleep(round_time * 60)
