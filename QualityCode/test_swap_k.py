import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_1(self):
        """
        Tests the empty list case. Expect empty list
        """
        test_list = []
        a1.swap_k(test_list, 0)
        expected_list = []
        self.assertEqual(test_list, expected_list)

    def test_swap_k_2(self):
        """
        Tests the len(list) = 1 case. Expect same list
        """
        test_list = [1]
        a1.swap_k(test_list, 0)
        expected_list = [1]
        self.assertEqual(test_list, expected_list)

    def test_swap_k_3(self):
        """
        Tests the case when len(list) is even and k = len(list) // 2
        """
        test_list = [1, 2, 3, 4]
        a1.swap_k(test_list, 2)
        expected_list = [3, 4, 1, 2]
        self.assertEqual(test_list, expected_list)

    def test_swap_k_4(self):
        """
        Tests the case which len(list) is odd and k = len(list) // 2
        """
        test_list = [1, 2, 3, 4, 5]
        a1.swap_k(test_list, 2)
        expected_list = [4, 5, 3, 1, 2]
        self.assertEqual(test_list, expected_list)

    def test_swap_k_2(self):
        """
        Tests the general case
        """
        test_list = [1, 2, 3, 4, 5, 6]
        a1.swap_k(test_list, 2)
        expected_list = [5, 6, 3, 4, 1, 2]
        self.assertEqual(test_list, expected_list)


if __name__ == '__main__':
    unittest.main(exit=False)
