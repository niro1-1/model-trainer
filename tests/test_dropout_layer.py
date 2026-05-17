import unittest
from dropout_layer import DropoutLayer

class TestDropoutLayer(unittest.TestCase):
    def test_dropout_behavior(self):
        layer = DropoutLayer(rate=0.5)
        input_data = [1.0, 2.0, 3.0]
        output_data = layer.forward(input_data)
        # Check that output is as expected (not all zeros)
        self.assertNotEqual(sum(output_data), 0)

    def test_batch_size_one(self):
        layer = DropoutLayer(rate=0.5)
        input_data = [1.0]
        output_data = layer.forward(input_data)
        # Check that output is the same as input when batch size is 1
        self.assertEqual(output_data, input_data)

if __name__ == '__main__':
    unittest.main()