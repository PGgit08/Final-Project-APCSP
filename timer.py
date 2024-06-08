import time

class Timer:
    def __init__(self):
        self.reset()

    # reset the timer
    def reset(self):
        self.old_time = time.time()

    # check how much time has elapsed on the timer
    def has_elapsed(self, seconds):
        return time.time() - self.old_time >= seconds
