from numpy import *
from numpy.linalg import eig

I = array([[2./3,-1./4],[-1./4,2./3]])

print('I = \n', I)

Es, evectors = eig(I)

print('Eigenvalues = ',Es, '\n Eigenvector Matrix = \n',evectors)

Vec = np.array([ evectors[0,0], evectors[1,0]])

LHS = np.dot(I,Vec)

RHS = Es[0]*Vec

print('LHS - RHS = ',LHS - RHS)
