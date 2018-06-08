import a2
import unittest

class TestMazeStr(unittest.TestCase):
    """ Test class for Maze.__str__ method of a2 module. """


    def test_maze_str_1(self):
        """
        Test if the maze object identifies a wall and denys movement.
        """
        maze_template = [['#', '#', '#', '#', '#', '#', '#'], 
                         ['#', '.', '.', '.', '.', '.', '#'], 
                         ['#', '.', '#', '#', '#', '.', '#'], 
                         ['#', '.', '.', '@', '#', '.', '#'], 
                         ['#', '@', '#', '.', '@', '.', '#'], 
                         ['#', '#', '#', '#', '#', '#', '#']]
        rat_J = a2.Rat(a2.RAT_1_CHAR, 1, 1)
        rat_P = a2.Rat(a2.RAT_2_CHAR, 1, 4)

        maze = a2.Maze(maze_template, rat_J, rat_P)

        maze_str = "#######\n#J..P.#\n#.###.#\n#..@#.#\n#@#.@.#\n#######\nJ at (1, 1) ate 0 sprouts.\nP at (1, 4) ate 0 sprouts."

        self.assertEqual(str(maze), maze_str)


if __name__ == "__main__":
    unittest.main(exit=False)
