import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.

    def test_stock_price_summary_1(self):
        """
        Tests the general case where len(L) > 1 and was positive and negative values.
        """

        got = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(got, expected)

    def test_stock_price_summary_2(self):
        """
        Tests the minimal case where len(L) == 0. (0.0, 0.0) is expected
        """

        got = a1.stock_price_summary([])
        expected = (0.0, 0.0)
        self.assertEqual(got, expected)

    def test_stock_price_summary_3(self):
        """
        Tests the case where len(L) == 1 and positive value. (value, 0.0) is expected
        """

        got = a1.stock_price_summary([0.01])
        expected = (0.01, 0.0)
        self.assertEqual(got, expected)

    def test_stock_price_summary_4(self):
        """
        Tests the case where len(L) == 1 and negative value. (0.0, value) is expected
        """

        got = a1.stock_price_summary([-0.01])
        expected = (0.0, -0.01)
        self.assertEqual(got, expected)

    def test_stock_price_summary_5(self):
        """
        Tests the case where len(L) < 1 and has positive values. (sum_value, 0.0) is expected
        """

        got = a1.stock_price_summary([0.01, 0.03, 0, 0, 0.10])
        expected = (0.14, 0.0)
        self.assertEqual(got, expected)

    def test_stock_price_summary_6(self):
        """
        Tests the case where len(L) < 1 and has negative values. (0.0, sum_value) is expected
        """

        got = a1.stock_price_summary([-0.02, -0.14, -0.01])
        expected = (0.0, -0.17)
        self.assertEqual(got, expected)



if __name__ == '__main__':
    unittest.main(exit=False)
