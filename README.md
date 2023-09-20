# conway
A implementation of Conway's life game on python, using numpy.

## build
### .env file
On the main folder create a .env file with the following enviorment varaibles
* ### GRID_WIDTH:
    the width of the grid on number of cells
* ### GRID_HEIGHT:
    the height of the grid on number of cells
* ### PERIOD
    the period of the program loop on seconds. Can be written in decimal values.
### alives file
  * Create a file called alives and save on it the position (row, column) base 0 of the alives cells on the first iteration.
  * Each line is a cell and the row and column values are separated by a space.
* #### e.g: This will generate a starship on a 10 x 10 grid of cells:
          5 8
          6 8
          7 8
          7 7
          6 6
      
