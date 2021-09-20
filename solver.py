import numpy as np
#mesh points in space
x = np.linspace(0, L, Nx+1)

dx = x[1] - x[0]

#mesh points in time
t = np.linspace(0, T, Nt+1)
dt = t[1] - t[0]

#define mesh Fourier number 
F = a*dt/dx**2

#unknown u at new time level
u = np.zeros(Nx+1)
u_n = np.zeros(Nx+1)

#set initial conditions u(x,0) = I(x)

for i in range(0, Nx+1):
    u_n[i] = I(x[i])
    