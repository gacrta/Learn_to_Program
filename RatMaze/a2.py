# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.

    def __init__(self, symbol, row, col):
        """(Rat,str,int,int)->NoneType

        Inits Rat object with a name and at position (row, col)
        >>> ratName = "R"
        >>> ratRow = 1
        >>> ratCol = 4
        >>> rat = Rat(ratName, ratRow, ratCol)
        >>> ratName==rat.symbol and ratRow==rat.row and \
            ratCol==rat.col and rat.num_sprouts_eaten == 0
        True
        """

        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def __str__(self):
        """(Rat)->str
        Return a string representation of the rat.

        >>> ratName = "R"
        >>> ratRow = 1
        >>> ratCol = 4
        >>> rat = Rat(ratName, ratRow, ratCol)
        >>> rat.eat_sprout()
        >>> rat.eat_sprout()
        >>> str(rat)
        "R at (1, 4) ate 2 sprouts."
        """

        rat_str = "{0} at ({1}, {2}) ate {3} sprouts."
        return rat_str.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)


    def set_location(self, row, col):
        """(Rat,int,int)->NoneType

        Sets a new location of (row, col) for this Rat.

        >>> ratName = "R"
        >>> old_row = 1
        >>> old_col = 4
        >>> rat = Rat(ratName, old_row, old_col)
        >>> new_row = 3
        >>> new_col = 2
        >>> rat.set_location(new_row, new_col)
        >>> rat.row == new_row && rat.col == new_col
        True
        """

        self.row = row
        self.col = col


    def eat_sprout(self):
        """(Rat)->NoneType

        Increments the number of sprouts eaten.

        >>> ratName = "R"
        >>> ratRow = 1
        >>> ratCol = 4
        >>> rat = Rat(ratName, ratRow, ratCol)
        >>> rat.eat_sprout()
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten == 2
        True
        """

        self.num_sprouts_eaten += 1


class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.


