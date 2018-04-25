import numpy as np
from numpy import dot
from numpy.linalg import inv
from mpl_toolkits.mplot3d import axes3d
import matplotlib as mpl
import matplotlib.pyplot as plt

def mdot(*args):
    return reduce(np.dot, args)


if __name__=='__main__':
    fig = plt.figure()
    
    for i in range(1,5):
        in_data = np.loadtxt('./provided_files/Data{}.csv'.format(i), comments='x')
        x = in_data[:, 0]
        y = in_data[:, 1]
        
        mean_x = np.mean(x)
        mean_y = np.mean(y)
    
        var_x = np.var(x)
        var_y = np.var(x)
        
        corr = (sum((x-mean_x)*(y-mean_y)))/np.sqrt(sum((x-mean_x)**2)*sum((y-mean_y)**2))
        
        print(corr)
        
        x_cap = np.column_stack([np.ones(len(x)), x])
        beta = mdot(inv(dot(x_cap.T, x_cap)), x_cap.T, y)
        
        line_x = np.array([0,20])
        line_y = beta[0] + line_x*beta[1]
        
        
        ax = fig.add_subplot(220 + i)
        ax.set_xlabel('x_{}'.format(i))
        ax.set_xlim(0, 20)
        ax.set_ylabel('y_{}'.format(i))
        ax.set_ylim(0, 13)
        ax.scatter(x, y)
        ax.scatter(mean_x, mean_y, c='red')
        ax.scatter(var_x, var_y, c='green')
        ax.plot(line_x, line_y, c='orange')
    
    plt.show()
    
    
