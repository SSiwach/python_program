import numpy as np



from scipy.integrate import solve_ivp   #import solution from the scipy
def deriv(t,u):
    # u = [y,v]
    # du = [dy,dv]
    du=[0,0]
    du[0] = u[1] #dy = v
    du[1] = 5.0*u[1] - 4.0*u[0] + np.exp(4.0*t) #dv = y''
    return du
u0 = np.array([0,1]) 
sol = solve_ivp( deriv, [0,10], u0, dense_output=True)
def y_exact(t):
    return 2.0/9.0*np.exp(4.0*t) - 2.0/9.0*np.exp(t) + t/3.0*np.exp(4.0*t)

t = np.linspace(0.0001, 10, 100) # not 0.0 for the log
u = sol.sol(t) 

import matplotlib.pyplot as plt
plt.plot(t, np.log(u[0]) - np.log(y_exact(t)),'-', label='diff_log(t)') 
plt.show()
