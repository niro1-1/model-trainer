from collections import deque

class LossTracker:
    def __init__(self):
        self.losses = deque()

    def add_loss(self, loss):
        self.losses.append(loss)

    def get_losses(self):
        return list(self.losses)