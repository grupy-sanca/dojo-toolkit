import time

WARNING_COLOR = '\033[93m'
DEFAULT_COLOR = '\033[0m'


try:
    input = raw_input
except NameError:
    pass


def print_warning_message(message):
    """
    print a message using yellow color
    """
    print('{}{}{}'.format(WARNING_COLOR, message, DEFAULT_COLOR))


def dojo_timer(notifier, round_time, sound_player):
    """Wait the defined and then shows notification and waits
    for replace
    """
    is_start = True
    while True:
        if not is_start:
            notifier.notify('Time Up', timeout=15 * 1000)
            sound_player.play_timeup()
        print_warning_message('Press Enter when replaced')
        input()
        sound_player.play_start()
        print_warning_message('Round Start!')
        time.sleep(round_time * 60)
        is_start = False
