import a2
import unittest

class TestRatInit(unittest.TestCase):
    """ Test class for Rat.__init__ method of a2 module. """


    def test_rat_symbol(self):
        """
        Test if the rat object receives the correct symbol.
        """
        rat_name = a2.RAT_1_CHAR
        rat_row = 1
        rat_col = 4
        rat = a2.Rat(rat_name, rat_row, rat_col)

        self.assertEqual(rat.symbol, rat_name)


    def test_rat_row(self):
        """
        Test if the rat object receives the correct row.
        """
        rat_name = a2.RAT_1_CHAR
        rat_row = 1
        rat_col = 4
        rat = a2.Rat(rat_name, rat_row, rat_col)

        self.assertEqual(rat.row, rat_row)


    def test_rat_col(self):
        """
        Test if the rat object receives the correct col.
        """
        rat_name = a2.RAT_1_CHAR
        rat_row = 1
        rat_col = 4
        rat = a2.Rat(rat_name, rat_row, rat_col)

        self.assertEqual(rat.col, rat_col)


    def test_rat_num_sprouts_eaten(self):
        """
        Test if the rat object inits with zero sprouts eaten.
        """
        rat_name = a2.RAT_1_CHAR
        rat_row = 1
        rat_col = 4
        rat = a2.Rat(rat_name, rat_row, rat_col)

        self.assertEqual(rat.num_sprouts_eaten, 0)


if __name__ == "__main__":
    unittest.main(exit=False)
