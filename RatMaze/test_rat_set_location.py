import a2
import unittest

class TestRatSetLocation(unittest.TestCase):
    """ Test class for Rat.set_location method of a2 module. """

    def test_rat_set_location_1(self):
        """
        Test if the rat.row and rat.col do not change if set
        with current values.
        """
        rat_name = a2.RAT_1_CHAR
        rat_row = 1
        rat_col = 4
        rat = a2.Rat(rat_name, rat_row, rat_col)

        rat.set_location(rat_row, rat_col)

        self.assertEqual((rat_row, rat_col), (rat.row, rat.col))


    def test_rat_set_location_2(self):
        """
        Test if the rat.row changes and rat.col don't.
        """
        rat_name = a2.RAT_1_CHAR
        old_row = 1
        old_col = 4
        rat = a2.Rat(rat_name, old_row, old_col)

        new_row = 2
        rat.set_location(new_row, old_col)

        self.assertEqual((new_row, old_col), (rat.row, rat.col))


    def test_rat_set_location_3(self):
        """
        Test if the rat.col changes and rat.row don't.
        """
        rat_name = a2.RAT_1_CHAR
        old_row = 1
        old_col = 4
        rat = a2.Rat(rat_name, old_row, old_col)

        new_col = 2
        rat.set_location(old_row, new_col)

        self.assertEqual((old_row, new_col), (rat.row, rat.col))


    def test_rat_set_location_4(self):
        """
        Test if the rat.col and rat.row changes at same time.
        """
        rat_name = a2.RAT_1_CHAR
        old_row = 1
        old_col = 4
        rat = a2.Rat(rat_name, old_row, old_col)

        new_row = 3
        new_col = 2
        rat.set_location(new_row, new_col)

        self.assertEqual((new_row, new_col), (rat.row, rat.col))


if __name__ == "__main__":
    unittest.main(exit=False)
