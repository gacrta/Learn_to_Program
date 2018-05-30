import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_num_buses_1(self):
        """
        Test the case where the number is higher than 50 but not
        divisible by 50.
        """

        got = a1.num_buses(75)
        expected = 2
        self.assertEqual(got, expected)

    def test_num_buses_2(self):
        """
        Test the case where the number is less than 50.
        """

        got = a1.num_buses(49)
        expected = 1
        self.assertEqual(got, expected)

    def test_num_buses_2(self):
        """
        Test the case where the number is equal to 50.
        """

        got = a1.num_buses(50)
        expected = 1
        self.assertEqual(got, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
