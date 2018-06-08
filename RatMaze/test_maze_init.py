import a2
import unittest

class TestMazeInit(unittest.TestCase):
    """ Test class for Maze.__init__ method of a2 module. """


    def test_maze_template(self):
        """
        Test if the maze object receives the correct maze template.
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

        self.assertEqual(maze.template, maze_template)


    def test_maze_rat_1(self):
        """
        Test if the maze object receives the correct first Rat object.
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

        self.assertEqual(maze.rat_1, rat_J)


    def test_maze_rat_2(self):
        """
        Test if the maze object receives the correct first Rat object.
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

        self.assertEqual(maze.rat_2, rat_P)


if __name__ == "__main__":
    unittest.main(exit=False)
