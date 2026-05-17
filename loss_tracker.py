# Implementing deque for loss tracking

from collections import deque

class LossTracker:
    def __init__(self, max_len=100):
        self.losses = deque(maxlen=max_len)

    def add_loss(self, loss):
        self.losses.append(loss)

    def get_average_loss(self):
        return sum(self.losses) / len(self.losses) if self.losses else 0.0
