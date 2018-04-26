import numpy as np
from numpy import dot
from numpy.linalg import inv
from mpl_toolkits.mplot3d import axes3d
import matplotlib as mpl
import matplotlib.pyplot as plt
from functools import reduce

def mdot(*args):
    return reduce(np.dot, args)


if __name__=='__main__':
    fig1 = plt.figure()
    fig2 = plt.figure()
    
    xs = []
    ys = []
    
    for i in range(1,5):
        in_data = np.loadtxt('./provided_files/Data{}.csv'.format(i), comments='x')
        x = in_data[:, 0]
        y = in_data[:, 1]
        
        xs.append(x)
        ys.append(y)
        
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
        

        ax1 = fig1.add_subplot(220 + i)
        ax1.set_xlabel('x_{}'.format(i))
        ax1.set_xlim(0, 20)
        ax1.set_ylabel('y_{}'.format(i))
        ax1.set_ylim(0, 13)
        ax1.scatter(x, y)
        ax1.scatter(mean_x, mean_y, c='red')
        ax1.scatter(var_x, var_y, c='green')
        ax1.plot(line_x, line_y, c='orange')


    ax2 = fig2.add_subplot(211)
    ax2.set_ylabel('x')
    ax2.set_xlabel('Datasets')
    ax2.boxplot(xs)
    
    ax2 = fig2.add_subplot(212)
    ax2.set_ylabel('y')
    ax2.set_xlabel('Datasets')
    ax2.boxplot(ys)
    
    plt.show()
    
    
