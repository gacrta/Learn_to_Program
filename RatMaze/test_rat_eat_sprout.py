import a2
import unittest

class TestRatEatSprout(unittest.TestCase):
    """ Test class for Rat.eat_sprout method of a2 module. """

    def test_rat_eat_sprout_1(self):
        """
        Test if rat.num_sprout_eaten increses.
        """
        rat_name = a2.RAT_1_CHAR
        rat_row = 1
        rat_col = 4
        rat = a2.Rat(rat_name, rat_row, rat_col)
        rat.eat_sprout()

        self.assertEqual(rat.num_sprouts_eaten, 1)


    def test_rat_eat_sprout_2(self):
        """
        Test if rat.num_sprout_eaten maps to correct value.
        """
        rat_name = a2.RAT_1_CHAR
        rat_row = 1
        rat_col = 4
        rat = a2.Rat(rat_name, rat_row, rat_col)

        for i in range(10):
            rat.eat_sprout()

        self.assertEqual(rat.num_sprouts_eaten, 10)


if __name__ == "__main__":
    unittest.main(exit=False)
