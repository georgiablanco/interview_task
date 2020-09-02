"""
 Example program to show using an array to back a grid on-screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/mdTeqiWyFnc
"""


class GridCreator:
    def __init__(self, width, height, margin):
        self.width = width
        self.height = height
        self.margin = margin

    def create_2d_array(self):

        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        grid = []
        for row in range(10):
            # Add an empty array that will hold each cell
            # in this row
            grid.append([])
            for column in range(10):
                grid[row].append(0)  # Append a cell

        # Set row 1, cell 5 to one. (Remember rows and
        # column numbers start at zero.)
        grid[1][5] = 1

        return grid




if __name__ == "__main__":
    grid = GridCreator(20, 20, 5).create_2d_array()
    print(grid)