import time

class Timer:
    def __init__(self):
        self.reset()

    def reset(self):
        self.old_time = time.time()

    def has_elapsed(self, seconds):
        return time.time() - self.old_time >= seconds
