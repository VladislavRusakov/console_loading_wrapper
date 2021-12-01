import itertools
import threading
import time
import sys


def loading(function):
    def wrapper():
        done = False

        def animate():
            SPEED = 2
            LINE = '\rLoading '

            for frame in itertools.cycle(
                    ["⡏ ", "⡗ ", "⡧ ", "⣇ ", "⣸ ", "⢼ ", "⢺ ", "⢹ "]):
                if done:
                    break
                sys.stdout.write(LINE + frame)
                sys.stdout.flush()
                time.sleep(SPEED / 10)
            sys.stdout.write('\rDone!' + ' ' * (len(LINE) + 2))

        thread = threading.Thread(target=animate)
        thread.start()

        function()

        done = True
    return wrapper


@loading
def sleeps():
    # YOUR FUNCTION HERE
    time.sleep(5)


sleeps()
