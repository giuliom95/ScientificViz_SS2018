import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__=='__main__':
    X = []
    Y = []
    Z = []

    max_tuple = (0,0,0)

    fd = open('Data', 'r')
    for line in fd.readlines():
        elems = line.split()
        if len(elems) == 3:
            x = float(elems[0])
            y = float(elems[1])
            z = float(elems[2])
            
            if z > max_tuple[2]:
                max_tuple = (x,y,z)
                
            X.append(x)
            Y.append(y)
            Z.append(z)

    minZ = min(Z)
    maxZ = max(Z)

    X = np.reshape(X, (24, 24))
    Y = np.reshape(Y, (24, 24))
    Z = np.reshape(Z, (24, 24))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.contourf(X,Y,Z, levels=np.linspace(minZ,maxZ,300))

    x,y,z = max_tuple
    ax.text(x, y, z+.1, 'Max (x={}, y={}, z={})'.format(x,y,z))
    ax.scatter([x],[y],[z+.01], c='red')


    plt.show()


