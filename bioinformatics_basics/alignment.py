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
        for key in self.Moves.keys():
            path = [[0,0]]
            for i in range(len(self.Moves[key])):
                path.append([self.Moves[key][:i+1].count('East'),self.Moves[key][:i+1].count('Nord')])
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
        if self.Path:
            ax.plot(np.transpose(self.Path[list(self.Path.keys())[-1]])[0],
                    np.transpose(self.Path[list(self.Path.keys())[-1]])[1],'o',markersize=5,color='red')
        return 
        

###################################################################################################################################################################################


class LongestCommonSubsequence():
    def __init__(self,*args,**kwargs):
        # Set default parameters
        self.L1 = 10
        self.L2 = 10
        self.replace = {0:'A', 1:'B', 2:'C', 3:'D'}
        self.Seq1 = np.array([])
        self.Seq2 = np.array([])
        # Update with provided parameters
        self.__dict__.update(kwargs)
        # Actual initialization
        if not self.Seq1.size:
            self.Seq1 = np.array(pd.Series(np.floor(4*np.random.rand(self.L1))).map(self.replace))
            self.Seq2 = np.array(pd.Series(np.floor(4*np.random.rand(self.L2))).map(self.replace))
        self.L1 = (len(self.Seq1))
        self.L2 = (len(self.Seq2))
        self.Score = np.zeros((self.L1+1,self.L2+1))
        self.Moves = {}
        
            
    def run(self):
        # Fill first column
        for i in range(0,self.L1):
            self.Score[i,0] = 0
            self.Moves[str(i) + ',0'] = i*['Nord']
        # Fill first row
        for j in range(0,self.L2):
            self.Score[0,j] = 0
            self.Moves['0,' + str(j)] = j*['East']
        # Iteratively fill the Score Matrix; save moves that maximize score to all vertexes
        for i in range(1,self.L1+1):
            for j in range(1,self.L2+1):
                match = (self.Seq1[i-1]==self.Seq2[j-1])
                max_score = max(self.Score[i-1,j],self.Score[i,j-1],match*(self.Score[i-1,j-1]+1))
                if max_score == self.Score[i-1,j]:
                    self.Moves[str(i) + ',' + str(j)] = self.Moves[str(i-1) + ',' + str(j)] + ['Nord']
                elif max_score == self.Score[i,j-1]:
                    self.Moves[str(i) + ',' + str(j)] = self.Moves[str(i) + ',' + str(j-1)] + ['East']    
                elif max_score == match*(self.Score[i-1,j-1]+1):
                    self.Moves[str(i) + ',' + str(j)] = self.Moves[str(i-1) + ',' + str(j-1)] + ['Diag']
                self.Score[i,j] = max_score
    
    def visualize(self):
        fig,ax = plt.subplots(figsize=(self.L2+1,self.L1+1))
        # Plain grid plot
        x,y = np.meshgrid(np.arange(self.L2+1),np.arange(self.L1+1))
        ax.plot(x,y,'o',markersize=5,color='black')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        for xpos in np.unique(x)[:-1]:
            ax.text(xpos+0.5,-0.5,self.Seq2[xpos])
        for ypos in np.unique(y)[:-1]:
            ax.text(-0.5,ypos+0.5,self.Seq1[ypos])
        # Steps and scores
        for key in self.Moves.keys():
            try:
                if self.Moves[key][-1] == 'Diag':
                    ystart = int(key.split(',')[0])
                    xstart = int(key.split(',')[1])
                    ax.arrow(xstart-0.9,ystart-0.9,0.8,0.8,width=0.02,head_width=0.2,length_includes_head=True,
                             color='lightblue')
                    ax.text(xstart-0.5,ystart-0.5,'+1')
            except:
                pass
        return ax