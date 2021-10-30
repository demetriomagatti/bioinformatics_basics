import numpy as np
import pandas as pd


class ManhattanSolver():
    def __init__(self,*args,**kwargs):
        #Set default parameters
        self.nrows = 10
        self.ncols = 10
        #Update with provided parameters
        self.__dict__.update(kwargs)
        #Actual initialization
        self.MoveEast = int(np.random.rand(self.nrows,self.ncols-1))
        self.MoveSouth = int(np.random.rand(self.nrows-1,self.ncols))
        self.Score = np.zeros((self.nrows,self.ncols))
    
    def run(self):
        for i in range(1,self.nrows):
            Score[i,0] = 
        return
