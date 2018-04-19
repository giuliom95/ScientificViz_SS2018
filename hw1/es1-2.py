import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as aa

DATA_RES = 200
VIZ_RES = 400
BASE_PLANE = -5
COLOR_MAP = mpl.cm.coolwarm

if __name__=='__main__':
    domain = np.linspace(-1,1,DATA_RES)**3
    domain_size = len(domain)
    
    #colormap = mpl.colors.LinearSegmentedColormap('RED', {'red': [(0,1,1), (1,1,1)], 'green': [(0,1,0), (1,1,1)], 'blue': [(0,1,0), (1,1,1)]})
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('x')
    ax.set_xticks(np.linspace(-1,1,5))
    ax.set_ylabel('y')
    ax.set_yticks(np.linspace(-1,1,5))
    ax.set_zlabel('z')
    ax.set_zticks(np.linspace(-1,1,5))
    ax.set_zlim(BASE_PLANE+.1, 1)

    X, Y = np.meshgrid(domain, domain)
    Z = np.sin(6*np.cos(np.sqrt(X**2+Y**2))+5*np.arctan2(Y,X))
    
    cfset = ax.contourf(X,Y,Z, levels=np.linspace(-1,1,VIZ_RES), cmap=COLOR_MAP, antialiased=False)
    ax.contour(X,Y,Z, offset=BASE_PLANE, cmap=COLOR_MAP)
    
    cb = plt.colorbar(cfset, aspect=5, shrink=.5)
    cb.set_ticks(np.linspace(-.75,.75,7))#.set_ticks(np.linspace(-1,1,5))
    
    plt.show()
    
    
