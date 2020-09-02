"""
 Example program to show using an array to back a grid on-screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/mdTeqiWyFnc
"""


class Grid:
    def __init__(self):
        self.grid = self.create_2d_array()

    def create_2d_array(self):

        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(10):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(10):
                self.grid[row].append(0)  # Append a cell

        # Set row 1, cell 5 to one. (Remember rows and
        # column numbers start at zero.)
        self.grid[1][5] = 1

        print(self.grid)

        return self.grid

    def update_cell(self, row, column):
        self.grid[row][column] = 1

    def check_cell(self, row, column):
        return self.grid[row][column]


if __name__ == "__main__":

    print(Grid())