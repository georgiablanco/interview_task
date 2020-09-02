"""
Class for the colour changing
"""
import pygame
from array_backed_grid import Grid


class ColourChangerGame:
    def __init__(self, width, height, margin, window_size):
        self.width = width
        self.height = height
        self.margin = margin
        self.window_size = window_size

    # def loop(self):

    def play(self):
        grid = Grid()

        colors = {
            "white": (0, 0, 0),
            "black": (255, 255, 255),
            "green": (0, 255, 0),
            "red": (255, 0, 0),
        }

        # Initialize pygame
        pygame.init()

        # Set the HEIGHT and WIDTH of the screen
        screen = pygame.display.set_mode(self.window_size)

        # Set title of screen
        pygame.display.set_caption("Array Backed Grid")

        # Loop until the user clicks the close button.
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # -------- Main Program Loop -----------
        while not done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (self.width + self.margin)
                    row = pos[1] // (self.height + self.margin)
                    # Set that location to one
                    grid.update_cell(row, column)
                    print("Click ", pos, "Grid coordinates: ", row, column)

            # Set the screen background
            screen.fill(colors["black"])

            # Draw the grid
            for row in range(10):
                for column in range(10):
                    color = colors["white"]
                    if grid.check_cell(row, column) == 1:
                        color = colors["green"]
                    pygame.draw.rect(screen,
                                     color,
                                     [(self.margin + self.width) * column + self.margin,
                                      (self.margin + self.height) * row + self.margin,
                                      self.width,
                                      self.height])

            # Limit to 60 frames per second
            clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
        pygame.quit()


if __name__ == "__main__":
    ColourChangerGame(20, 20, 5, [255, 255]).play()
