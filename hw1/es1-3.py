#!/bin/python

# The maximum is on x=4, y=3 and has value 1

import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib as mpl
import matplotlib.pyplot as plt

def load_data(filename):
    data = []

    fd = open('Data', 'r')
    for line in fd.readlines():
        elems = line.split()
        if len(elems) == 3:
            data.append([float(elems[0]), float(elems[1]), float(elems[2])])

    return np.array(data)


def find_max(data):
    return data[data.argmax(0)[2]]
    
    
def plot(data):
    xs = data[:,0]
    ys = data[:,1]
    zs = data[:,2]
    X = np.reshape(xs, (24,24))
    Y = np.reshape(ys, (24,24))
    Z = np.reshape(zs, (24,24))
    
    minZ = Z.min()
    maxZ_tuple = find_max(data)
    maxZ = maxZ_tuple[2]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.contourf(X,Y,Z, levels=np.linspace(minZ,maxZ,300))
    
    x,y,z = maxZ_tuple
    ax.text(x, y, z+0.05, ' Max (x={}, y={}, z={})'.format(x,y,z))
    ax.scatter([x],[y],[z], c='red')
    ax.plot([x, x],[y, y],[z-.1, z+.1], c='red')

    ax.view_init(20, 30)
    plt.show()


if __name__=='__main__':
    data = load_data('./Data') 
    plot(data)
    



