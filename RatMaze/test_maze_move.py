import a2
import unittest

class TestMazeMove(unittest.TestCase):
    """ Test class for Maze.__init__ method of a2 module. """


    def test_maze_move_1(self):
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

        self.assertEqual(maze.move(rat_J, a2.UP, a2.NO_CHANGE), False)


    def test_maze_move_2(self):
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

        self.assertEqual(maze.move(rat_J, a2.DOWN, a2.RIGHT), False)


    def test_maze_move_3(self):
        """
        Test if the maze object identifies a Hall and allows movement.
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

        self.assertEqual(maze.move(rat_J, a2.DOWN, a2.NO_CHANGE), True)


    def test_maze_move_4(self):
        """
        Test if the maze object removes a eaten sprout.
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
        old_sprout_count = maze.num_sprouts_left

        maze.move(rat_J, a2.DOWN, a2.NO_CHANGE)
        maze.move(rat_J, a2.DOWN, a2.NO_CHANGE)
        maze.move(rat_J, a2.DOWN, a2.NO_CHANGE)

        self.assertEqual(maze.num_sprouts_left, old_sprout_count - 1)


    def test_maze_move_5(self):
        """
        Test if the maze object does not remove a sprout when movement fails.
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
        old_sprout_count = maze.num_sprouts_left

        maze.move(rat_J, a2.DOWN, a2.RIGHT)

        self.assertEqual(maze.num_sprouts_left, old_sprout_count)


    def test_maze_move_6(self):
        """
        Test if the maze object does not remove a sprout when movement
        suceeds but no sprout is eaten.
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
        old_sprout_count = maze.num_sprouts_left

        maze.move(rat_J, a2.DOWN, a2.NO_CHANGE)

        self.assertEqual(maze.num_sprouts_left, old_sprout_count)


if __name__ == "__main__":
    unittest.main(exit=False)
