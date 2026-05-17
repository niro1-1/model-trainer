# Updated dropout layer to handle batch size of 1

class DropoutLayer:
    def __init__(self, rate=0.5):
        self.rate = rate

    def forward(self, inputs):
        if inputs.shape[0] == 1:
            return inputs  # No dropout for batch size of 1
        mask = np.random.binomial(1, 1 - self.rate, size=inputs.shape)
        return inputs * mask
