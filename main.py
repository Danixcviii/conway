import scipy.signal as ss
import dotenv as de
import numpy as np
import time
import os


de.load_dotenv()

GRID_WIDTH = int(os.getenv('GRID_WIDTH'))
GRID_HEIGHT = int(os.getenv('GRID_HEIGHT'))
PERIOD = float(os.getenv('PERIOD'))

if __name__ == '__main__':  

    #board initialization
    #Generates a grid of a specific width and height width all cells at 0 but those which position is readed from data file. 
    with open(r'data') as f:
        alives = np.array([r.split() for r in f.readlines()], dtype = np.int8)

    state = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype = np.int8)
    state[alives[:, 0], alives[:, 1]] = 1

    #Generates the kernel of the convolution
    kernel = np.ones((3, 3), dtype = np.int8); kernel[1, 1] = 0

    #main loop
    while True:
        #Counts the number of neigboors of each cell 
        count = ss.convolve2d(state, kernel, mode = 'same', boundary='wrap')

        # (count == 3) or ((state == 1) and (count == 2))
        state = np.where(np.logical_or(count == 3, np.logical_and(state == 1, count == 2)), 1, 0)

        os.system('cls')
        print(state)
        time.sleep(PERIOD)


 