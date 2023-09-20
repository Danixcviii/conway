import scipy.signal as ss
import dotenv as de
import numpy as np
import time
import os


de.load_dotenv()

GRID_WIDTH = int(os.getenv('GRID_WIDTH'))
GRID_HEIGHT = int(os.getenv('GRID_HEIGHT'))
PERIOD = float(os.getenv('PERIOD'))
BOUNDARY = os.getenv('BOUNDARY')

def show_grid(grid: np.ndarray):
    os.system('cls')
    print(grid)

if __name__ == '__main__':  

    #board initialization
    #Generates a grid of a specific width and height width all cells at 0 but those which position is readed from data file. 
    with open(r'alives') as f:
        alives = np.array([r.split() for r in f.readlines()], dtype = np.int8)

    state = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype = np.int8)
    state[alives[:, 0], alives[:, 1]] = 1

    #Generates the kernel of the convolution
    kernel = np.ones((3, 3), dtype = np.int8); kernel[1, 1] = 0

    #main loop
    while True:
        #Counts the number of neigboors of each cell 
        count = ss.convolve2d(state, kernel, mode = 'same', boundary = BOUNDARY)

        # All Conway's game of life rules are checked with this logical line
        # 1. Any live cell with two or three live neighbors survives.
        # 2. Any dead cell with three live neighbors becomes a live cell.
        # 3. All other live cells die in the next generation due to underpopulation (fewe than two live neighbors)
        #    or overcrowding (more tha three live neighbors)
        # 4. Dead cells with fewer than three live neighbors remain dead, and dead cells with more than three live neighbors stay dead 
        #
        # Logical: A cell lives or survives if has 3 neighbors, also if is alive survives if it has 2 neighbors
        # (count == 3) or ((state == 1) and (count == 2))
        state = np.where(np.logical_or(count == 3, np.logical_and(state == 1, count == 2)), 1, 0)

        show_grid(state)
        time.sleep(PERIOD) # complete a loop


 