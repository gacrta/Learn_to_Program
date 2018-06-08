import a2
import unittest

class TestMazeGetCharacter(unittest.TestCase):
    """ Test class for Maze.get_character method of a2 module. """


    def test_maze_get_character_1(self):
        """
        Test if the maze object returns a wall value.
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

        self.assertEqual(maze.get_character(0, 0), a2.WALL)


    def test_maze_get_character_2(self):
        """
        Test if the maze object returns a hall value.
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

        self.assertEqual(maze.get_character(1, 1), a2.HALL)


    def test_maze_get_character_3(self):
        """
        Test if the maze object returns a sprout value.
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

        self.assertEqual(maze.get_character(4, 1), a2.SPROUT)


if __name__ == "__main__":
    unittest.main(exit=False)
