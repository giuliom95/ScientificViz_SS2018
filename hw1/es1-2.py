import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

fn = lambda x,y: np.sin(6*np.cos(np.sqrt(x**2+y**2))+5*np.arctan2(y,x))
d = np.linspace(-1,1,200)
d3 = np.linspace(-1,1,200)**3

def exercise1(domain, fn, zlim=(-3, 1), rcount=50, ccount=50):
    domain_size = len(domain)
    X, Y = np.meshgrid(domain, domain)
    Z = np.empty((domain_size, domain_size))
    
    for i in xrange(domain_size):
        for j in xrange(domain_size):
            Z[i, j] = fn(X[i,j], Y[i,j])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_zlim(zlim[0], zlim[1])
    ax.plot_surface(X,Y,Z, cmap=cm.coolwarm, linewidth=0, rcount=rcount, ccount=ccount)
    plt.show()
    

