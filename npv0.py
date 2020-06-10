import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# Axes3D import has side effects, it enables using projection='3d' in add_subplot
import matplotlib.pyplot as plt
import random


# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

def fun(x, y):
    return x**2 + y


def PPV(V,D,P):
    ppv = V*D / (V*D + (100-D)*(100-P))
    #print(ppv)
    return ppv

def NPV(V,D,P):
    npv = P*(100-D) / (P*(100-D)+D*(100-V))
    return npv


def Prevalance(D,V,P):
    specificity = np.arange(1,99,1)
    sensitivity = np.arange(1,99,1)
    ppvs = []
    npvs = []
    for specs in specificity:
        yppv = []
        ynpv = []
        for sense in sensitivity:
            ppval = PPV(sense,D,specs)
            npval = NPV(sense,D,specs)
            yppv.append(ppval)
            ynpv.append(npval)
        ppvs.append(yppv)
        npvs.append(ynpv)

    return sensitivity, specificity, ppvs, npvs

xx, yy, zz, W = Prevalance(12,99,99)

X, Y = np.meshgrid(xx,yy)

print(len(X))
print(len(Y))
#print(len(Z))

fig = plt.figure()

Zs = np.array(NPV(1,np.ravel(X),np.ravel(Y)))
Z = Zs.reshape(X.shape)
#Z = Z.reshape(X.shape)
print(len(Z))

ax = fig.add_subplot(111, projection='3d')
"""
x = y = np.arange(-3.0, 3.0, 0.05)
X, Y = np.meshgrid(x, y)
zs = np.array(fun(np.ravel(X), np.ravel(Y)))
Z = zs.reshape(X.shape)
"""

ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
