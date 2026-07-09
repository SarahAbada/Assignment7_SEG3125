import unittest
from countdown import CountdownTimer

class TestCountdownTimer(unittest.TestCase):

    # Cycle 1 - Float Input
    def test_float_input_raises_error(self):
        timer = CountdownTimer()
        with self.assertRaises(TypeError):
            timer.start(3.7)

    # Cycle 2 - Very Large Number
    def test_large_number_countdown(self):
        timer = CountdownTimer()
        result = timer.start(1000000)
        self.assertEqual(result[0], 1000000)   # starts at 1000000
        self.assertEqual(result[-1], 0)         # ends at 0
        self.assertEqual(len(result), 1000001)  # correct length

if __name__ == "__main__":
    unittest.main()