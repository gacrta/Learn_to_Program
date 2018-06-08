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

    def __init__(self, template, rat_1, rat_2):
        """(Maze, list of list of str, Rat, Rat)->NoneType

        Inits a instance of Maze using a template and two rats

        >>>template = [['#', '#', '#', '#', '#', '#', '#'], 
                       ['#', '.', '.', '.', '.', '.', '#'], 
                       ['#', '.', '#', '#', '#', '.', '#'], 
                       ['#', '.', '.', '@', '#', '.', '#'], 
                       ['#', '@', '#', '.', '@', '.', '#'], 
                       ['#', '#', '#', '#', '#', '#', '#']]
        >>>rat_1 = Rat('J', 1, 1)
        >>>rat_2 = Rat('P', 1, 4)
        >>>rat_maze=Maze(maze, rat_1, rat_2)
        """

        self.maze = template
        self.rat_1 = rat_1
        self.rat_2 = rat_2

##        # Check if rat_1 or rat_2 were added into a SPROUT and eat it if it does.
##        if self.template[self.rat_1.row][self.rat_1.row] == SPROUT:
##            self.template[self.rat_1.row][self.rat_1.row] = HALL
##            self.rat_1.eat_sprout
##
##        if self.template[self.rat_2.row][self.rat_2.row] == SPROUT:
##            self.template[self.rat_2.row][self.rat_2.row] = HALL
##            self.rat_2.eat_sprout

        # Counts the number of sprouts at the remaining
        num_sprouts_left = 0
        for row in range(1, len(self.maze)-1):
            for col in range(1, len(self.maze[row])-1):
                if self.maze[row][col] == SPROUT:
                    num_sprouts_left += 1

        self.num_sprouts_left = num_sprouts_left


    def is_wall(self, row, col):
        """(Maze,int,int)->bool

        Returns true if the position (row, col) of Maze instance contains a wall.

        >>>template = [['#', '#', '#', '#', '#', '#', '#'], 
                       ['#', '.', '.', '.', '.', '.', '#'], 
                       ['#', '.', '#', '#', '#', '.', '#'], 
                       ['#', '.', '.', '@', '#', '.', '#'], 
                       ['#', '@', '#', '.', '@', '.', '#'], 
                       ['#', '#', '#', '#', '#', '#', '#']]
        >>>rat_1 = Rat('J', 1, 1)
        >>>rat_2 = Rat('P', 1, 4)
        >>>rat_maze=Maze(maze, rat_1, rat_2)
        >>>rat_maze.is_wall(0, 0)
        True
        >>>rat_maze.is_wall(1, 1)
        False
        """

        return self.get_character(row, col) == WALL


    def get_character(self, row, col):
        """(Maze,int,int)->str

        Returns the value at position (row, col) of the Maze object

        >>>template = [['#', '#', '#', '#', '#', '#', '#'], 
                       ['#', '.', '.', '.', '.', '.', '#'], 
                       ['#', '.', '#', '#', '#', '.', '#'], 
                       ['#', '.', '.', '@', '#', '.', '#'], 
                       ['#', '@', '#', '.', '@', '.', '#'], 
                       ['#', '#', '#', '#', '#', '#', '#']]
        >>>rat_1 = Rat('J', 1, 1)
        >>>rat_2 = Rat('P', 1, 4)
        >>>rat_maze=Maze(maze, rat_1, rat_2)
        >>>rat_maze.get_character(0, 0)
        '#'
        >>>rat_maze.get_character(1, 1)
        '.'
        >>>rat_maze.get_character(4, 1)
        '@'
        """
        return self.maze[row][col]


    def move(self, rat, vert_delta, horz_delta):
        """(Maze,Rat,int,int)->bool
        precondition: vert_delta is one of (UP, NO_CHANGE or DOWN)
                      horz_delta is one of (LEFT, NO_CHANGE or RIGHT)

        Returns True if it is possible to move rat to its position
        plus the vert and horz deltas and eats a SPROUT if it is in
        the new position. If it is a wall, returns False and do not move rat.

        >>>template = [['#', '#', '#', '#', '#', '#', '#'], 
                       ['#', '.', '.', '.', '.', '.', '#'], 
                       ['#', '.', '#', '#', '#', '.', '#'], 
                       ['#', '.', '.', '@', '#', '.', '#'], 
                       ['#', '@', '#', '.', '@', '.', '#'], 
                       ['#', '#', '#', '#', '#', '#', '#']]
        >>>rat_1 = Rat('J', 1, 1)
        >>>rat_2 = Rat('P', 1, 4)
        >>>rat_maze=Maze(maze, rat_1, rat_2)
        >>>rat_maze.move(self.rat_1, UP, NO_CHANGE)
        False
        >>>rat_maze.move(self.rat_1, DOWN, RIGHT)
        False
        >>>rat_maze.move(self.rat_1, DOWN, NO_CHANGE)
        True
        >>>rat_maze.move(self.rat_1, DOWN, NO_CHANGE)
        True
        >>>rat_maze.move(self.rat_1, DOWN, NO_CHANGE)
        True
        >>>rat_maze.move(self.rat_1, DOWN, NO_CHANGE)
        True
        >>>self.rat_1.num_sprouts_eaten()
        1
        >>>rat_maze.get_character(4, 1)
        '.'
        """
        # Evaluate the possible new rat position
        new_row = rat.row + vert_delta
        new_col = rat.col + horz_delta

        # Check if it is a valid space and eat SPROUT if it is the case
        if not self.is_wall(new_row, new_col):
            rat.set_location(new_row, new_col)
            if self.get_character(new_row, new_col) == SPROUT:
                rat.eat_sprout()
                self.num_sprouts_left -= 1
                self.maze[new_row][new_col] = HALL
            return True
        return False


    def __str__(self):
        """(Maze)->str
        >>>template = [['#', '#', '#', '#', '#', '#', '#'], 
                       ['#', '.', '.', '.', '.', '.', '#'], 
                       ['#', '.', '#', '#', '#', '.', '#'], 
                       ['#', '.', '.', '@', '#', '.', '#'], 
                       ['#', '@', '#', '.', '@', '.', '#'], 
                       ['#', '#', '#', '#', '#', '#', '#']]
        >>>rat_1 = Rat('J', 1, 1)
        >>>rat_2 = Rat('P', 1, 4)
        >>>rat_maze=Maze(maze, rat_1, rat_2)
        >>>print(rat_maze)
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """
        maze_str = ''
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.rat_1.row == row and self.rat_1.col == col:
                    maze_str += self.rat_1.symbol
                elif self.rat_2.row == row and self.rat_2.col == col:
                    maze_str += self.rat_2.symbol
                else:
                    maze_str += self.get_character(row, col)
            maze_str += '\n'
        maze_str = maze_str + str(self.rat_1) + '\n' + str(self.rat_2)
        return maze_str
                    
