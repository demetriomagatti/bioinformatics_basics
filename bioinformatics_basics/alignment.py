import numpy as np
import matplotlib.pyplot as plt


class ManhattanSolver():
    def __init__(self,*args,**kwargs):
        # Set default parameters
        self.MaxScore = 10
        self.nrows = 10
        self.ncols = 10
        # Update with provided parameters
        self.__dict__.update(kwargs)
        # Actual initialization
        self.MoveEast = np.floor(self.MaxScore*np.random.rand(self.nrows,self.ncols-1))
        self.MoveNord = np.floor(self.MaxScore*np.random.rand(self.nrows-1,self.ncols))
        self.Score = np.zeros((self.nrows,self.ncols))
        self.Moves = {}
        self.Path = {}
    
    
    def run(self):
        # Fill first column
        for i in range(1,self.nrows):
            self.Score[i,0] = self.Score[i-1,0] + self.MoveNord[i-1,0]
            self.Moves[str(i) + ',0'] = i*['Nord']
        # Fill first row
        for j in range(1,self.ncols):
            self.Score[0,j] = self.Score[0,j-1] + self.MoveEast[0,j-1]
            self.Moves['0,' + str(j)] = j*['East']
        # Iteratively fill the Score Matrix; save moves that maximize score to all vertexes
        for i in range(1,self.nrows):
            for j in range(1,self.ncols):
                self.Score[i,j] = max(self.Score[i-1,j] + self.MoveNord[i-1,j],
                                      self.Score[i,j-1] + self.MoveEast[i,j-1])
                if (self.Score[i-1,j] + self.MoveNord[i-1,j] > self.Score[i,j-1] + self.MoveEast[i,j-1]):
                    self.Moves[str(i) + ',' + str(j)] = self.Moves[str(i-1) + ',' + str(j)] + ['Nord']
                else:
                    self.Moves[str(i) + ',' + str(j)] = self.Moves[str(i) + ',' + str(j-1)] + ['East']

    
    def makePath(self):
        for key in solver.Moves.keys():
            path = [[0,0]]
            for i in range(len(solver.Moves[key])):
                path.append([solver.Moves[key][:i+1].count('East'),solver.Moves[key][:i+1].count('Nord')])
            self.Path[key] = path
    
    
    def visualize(self):
        fig,ax = plt.subplots()
        # Plain grid plot
        x,y = np.meshgrid(np.arange(self.ncols),np.arange(self.nrows))
        ax.plot(x,y,'o',markersize=5,color='black')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        # Steps and scores
        for xpos in np.unique(x):
            for ypos in np.unique(y)[:-1]:
                ax.arrow(xpos,ypos+0.2,0,0.6,width=0.02,color='lightblue')
                ax.text(xpos,ypos+0.5,str(np.transpose(self.MoveNord)[xpos,ypos]))
        for xpos in np.unique(x)[:-1]:
            for ypos in np.unique(y):
                ax.arrow(xpos+0.2,ypos,0.6,0,width=0.02,color='lightblue')
                ax.text(xpos+0.5,ypos,str(np.transpose(self.MoveEast)[xpos,ypos]))
        ax.plot(np.transpose(self.Path[list(self.Path.keys())[-1]])[0],
                np.transpose(self.Path[list(self.Path.keys())[-1]])[1],'o',markersize=5,color='red')
        return ax