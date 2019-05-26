# Sandpile model
# 2 dimensional

import numpy as np
import random
import matplotlib.pyplot as plt

def change_lattice(lattice,x,y):
    lattice[x][y] += 1
    return lattice
    
def search_lattice(lattice,n):
    points = []
    counter = 0
    for i in range(n):
        for j in range(n):
            if lattice[i][j] > 3:
                points.append(([i],[j]))
                counter += 1
    return points, counter
    
iteration_number = 50
n = 15  # lattice size
timer = 0.1
lattice = np.round(3*np.random.random((n,n)))

p = 0        
plt.ion()
plt.imshow(lattice, interpolation='none',cmap='hot')
plt.clim(0,4)
plt.colorbar()
#plt.savefig("C:\Users\Daniel\Desktop\\video\img%d.png" % p)
plt.pause(timer)

for j in range(iteration_number):
    x = random.randint(0,n-1)
    y = random.randint(0,n-1)
    lattice = change_lattice(lattice,x,y)
    plt.imshow(lattice, interpolation='none',cmap='hot')
    plt.clim(0,4)
    p += 1
    #plt.savefig("desired_save_location!!!!!!!\img%d.png" % p)
    plt.pause(timer)

    points, counter = search_lattice(lattice,n)

    while counter != 0:
        for i in range(counter):
            x = points[i][0][0]
            y = points[i][1][0]
            if y+1 == n:
                y = -1
            if x+1 == n:
                x = -1
            lattice[x][y] = 0
            lattice[x-1][y] += 1
            lattice[x+1][y] += 1
            lattice[x][y-1] += 1
            lattice[x][y+1] += 1
            # print lattice
            plt.imshow(lattice, interpolation='none',cmap='hot')
            plt.clim(0,4)
            p += 1
            #plt.savefig("desired_image_save_location\img%d.png" % p)
            plt.pause(timer)  
        points, counter = search_lattice(lattice,n)
        
plt.close()