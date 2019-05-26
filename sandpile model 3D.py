# Sandpile model
# 3 dimensional

import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def change_lattice(lattice,x,y,z):
    lattice[x][y][z] += 1             # bump the (x,y,z) position
    return lattice
    
def search_lattice(lattice,n):
    points = []
    counter = 0
    for i in range(n):
        for j in range(n):
            for h in range(n):
                if lattice[i][j][h] > 5:
                    points.append(([i],[j],[h]))
                    counter += 1
    return points, counter
    
iteration_number = 20
n = 6     # lattice size
ms = 100   # marker size
timer = 0.1
lattice = 1 + np.round(4*np.random.random((n,n,n)))

plt.ion()
x0,y0,z0 = (lattice==0).nonzero()
x1,y1,z1 = (lattice==1).nonzero()
x2,y2,z2 = (lattice==2).nonzero()
x3,y3,z3 = (lattice==3).nonzero()
x4,y4,z4 = (lattice==4).nonzero()
x5,y5,z5 = (lattice==5).nonzero()
x6,y6,z6 = (lattice>5).nonzero()
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(x0,y0,z0,zdir='z',c='blue',s=ms,marker='s',alpha=0)
ax.scatter(x1,y1,z1,zdir='z',c='blue',s=ms,marker='s',alpha=0.1)
ax.scatter(x2,y2,z2,zdir='z',c='blue',s=ms,marker='s',alpha=0.2)
ax.scatter(x3,y3,z3,zdir='z',c='blue',s=ms,marker='s',alpha=0.3)
ax.scatter(x4,y4,z4,zdir='z',c='blue',s=ms,marker='s',alpha=0.4)
ax.scatter(x5,y5,z5,zdir='z',c='orange',s=ms,marker='s',alpha=0.6)
ax.scatter(x6,y6,z6,zdir='z',c='red',s=ms,marker='s',alpha=0.8)
ax.set_xlim3d(0,n)
ax.set_ylim3d(0,n)
ax.set_zlim3d(0,n)
plt.pause(timer)

for i in range(iteration_number):
    x = random.randint(0,n-1)
    y = random.randint(0,n-1)
    z = random.randint(0,n-1)
    lattice = change_lattice(lattice,x,y,z)

    x0,y0,z0 = (lattice==0).nonzero()
    x1,y1,z1 = (lattice==1).nonzero()
    x2,y2,z2 = (lattice==2).nonzero()
    x3,y3,z3 = (lattice==3).nonzero()
    x4,y4,z4 = (lattice==4).nonzero()
    x5,y5,z5 = (lattice==5).nonzero()
    x6,y6,z6 = (lattice>5).nonzero()
    ax = fig.add_subplot(111, projection = '3d')
    ax.scatter(x0,y0,z0,zdir='z',c='blue',s=ms,marker='s',alpha=0)
    ax.scatter(x1,y1,z1,zdir='z',c='blue',s=ms,marker='s',alpha=0.1)
    ax.scatter(x2,y2,z2,zdir='z',c='blue',s=ms,marker='s',alpha=0.2)
    ax.scatter(x3,y3,z3,zdir='z',c='blue',s=ms,marker='s',alpha=0.3)
    ax.scatter(x4,y4,z4,zdir='z',c='blue',s=ms,marker='s',alpha=0.4)
    ax.scatter(x5,y5,z5,zdir='z',c='orange',s=ms,marker='s',alpha=0.6)
    ax.scatter(x6,y6,z6,zdir='z',c='red',s=ms,marker='s',alpha=0.8)
    ax.set_xlim3d(0,n)
    ax.set_ylim3d(0,n)
    ax.set_zlim3d(0,n)
    plt.pause(timer)

    points, counter = search_lattice(lattice,n)

    while counter != 0:
        for i in range(counter):
            x = points[i][0][0]
            y = points[i][1][0]
            z = points[i][2][0]
            
            if y+1 == n:
                y = -1
            if x+1 == n:
                x = -1
            if z+1 == n:
                z = -1
             
            lattice[x][y][z] = 0       
            lattice[x-1][y][z] += 1
            lattice[x+1][y][z] += 1
            lattice[x][y-1][z] += 1
            lattice[x][y+1][z] += 1
            lattice[x][y][z-1] += 1
            lattice[x][y][z+1] += 1
            
            x0,y0,z0 = (lattice==0).nonzero()
            x1,y1,z1 = (lattice==1).nonzero()
            x2,y2,z2 = (lattice==2).nonzero()
            x3,y3,z3 = (lattice==3).nonzero()
            x4,y4,z4 = (lattice==4).nonzero()
            x5,y5,z5 = (lattice==5).nonzero()
            x6,y6,z6 = (lattice>5).nonzero()
            ax = fig.add_subplot(111, projection = '3d')
            ax.scatter(x0,y0,z0,zdir='z',c='blue',s=ms,marker='s',alpha=0)
            ax.scatter(x1,y1,z1,zdir='z',c='blue',s=ms,marker='s',alpha=0.1)
            ax.scatter(x2,y2,z2,zdir='z',c='blue',s=ms,marker='s',alpha=0.2)
            ax.scatter(x3,y3,z3,zdir='z',c='blue',s=ms,marker='s',alpha=0.3)
            ax.scatter(x4,y4,z4,zdir='z',c='blue',s=ms,marker='s',alpha=0.4)
            ax.scatter(x5,y5,z5,zdir='z',c='orange',s=ms,marker='s',alpha=0.6)
            ax.scatter(x6,y6,z6,zdir='z',c='red',s=ms,marker='s',alpha=0.8)
            ax.set_xlim3d(0,n)
            ax.set_ylim3d(0,n)
            ax.set_zlim3d(0,n)
            plt.pause(timer)
            
        points, counter = search_lattice(lattice,n)
        
# plt.close()