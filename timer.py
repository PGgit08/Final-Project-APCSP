import time

class Timer:
    old_time = time.time()
    locked = False

    def __init__(self):
        self.reset()

    # stops the timer completely
    def lock(self):
        self.locked = True

    # reset the timer
    def reset(self):
        self.old_time = time.time()

    # check how much time has elapsed on the timer
    def has_elapsed(self, seconds):
        if self.locked:
            return False

        return time.time() - self.old_time >= seconds
