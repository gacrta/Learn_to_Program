import a2
import unittest

class TestMazeIsWall(unittest.TestCase):
    """ Test class for Maze.__init__ method of a2 module. """


    def test_maze_is_wall_1(self):
        """
        Test if the maze object identifies a wall value.
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

        self.assertEqual(maze.is_wall(0, 0), True)


    def test_maze_is_wall_2(self):
        """
        Test if the maze object identifies a that a hall is not a wall.
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

        self.assertEqual(maze.is_wall(1, 1), False)


    def test_maze_is_wall_3(self):
        """
        Test if the maze object identifies a that a sprout is not a wall.
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

        self.assertEqual(maze.is_wall(4, 1), False)


if __name__ == "__main__":
    unittest.main(exit=False)
