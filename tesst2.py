# --> Import needed packages/functions.
import numpy as np
from scipy.integrate import solve_ivp

def pairwise_interactions(X):
    """Computation of the net forces resulting from pairwise interactions."""
    # --> Number of particles.
    n = len(X)
    
    # --> Gram matrix.
    d2 = -2 * X @ X.T
    
    # --> Squared pairwise distances.
    diag = -0.5 * np.einsum('ii->i', d2)
    d2 += diag + diag[:, None]
    
    # --> Prevent division by zero.
    np.einsum('ii->i', d2)[...] = 1
    
    # --> Net forces.
    F = np.nansum( (X[:, None, :] - X) * d2[..., None]**-1.5, axis=0)
    
    return F

def pairwise_interactions2(X):

    # --> Number of particles.
    n = len(X)
    
    # --> Initialize the force array.
    F = np.zeros_like(X)
    
    # --> Loop through all the particles.
    for i in range(n):
        for j in range(i+1, n):
                
            # --> Compute the difference vector.
            Δx = X[j] - X[i]
            
            # --> Add the ij contribution to the net force.
            F[i] += Δx / np.linalg.norm(Δx)**3
            
            # --> Add the ji contribution to the net force.
            F[j] -= F[i]
            
    return F

def nbody(t, u, ndim):
    """Right-hand side function for the N-Body simulation."""
    # --> Number of particles.
    n = len(u) // (2*ndim)
    
    # --> Initialize output vector.
    du = np.zeros_like(u)
    
    # --> Extract the positions and velocities.
    x, dx = u[:ndim*n], u[ndim*n:]
    
    # --> Compute the acceleration.
    ddx = pairwise_interactions2(x.reshape(n, ndim))

    # --> Return the time-derivatives for the ODE solver.
    du[:ndim*n] = dx
    du[ndim*n:] = ddx.ravel()
       
    return du
    
def simulation(x, dx, t):
    
    # --> Number of dimensions/Number of particles.
    assert x.shape == dx.shape
    n, ndim = x.shape

    # --> Initial condition for the simulation.
    u = np.r_[x.flatten(), dx.flatten()]
    
    # --> Parameters for the ODE solver.
    tspan = (t.min(), t.max())
    t_eval = t
    method = "RK45" #"DOP853"
    atol = rtol = 1e-10
    
    # --> Run the simulation.
    output = solve_ivp(
        lambda t, u : nbody(t, u, ndim),
        tspan,
        u,
        t_eval=t_eval,
        method=method,
        atol=atol,
        rtol=rtol
    )

    # --> Extract the positions and velocities of the n particles.
    x = output["y"][:n*ndim].reshape((n, ndim, -1))
    dx = output["y"][n*ndim:].reshape((n, ndim, -1))

    return x, dx


x0 = np.array([[0, 0], [0, 1], [1, 1], [1, 0.]])
dx0 = np.array([[1, 0], [0, -1], [ -1, 0], [0, 1]])
t = np.linspace(0, 20, 1000)

x, dx = simulation(x0, dx0, t)
print(x0)


import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.plot(x[0,0,:], x[0,1,:],)
plt.plot(x[1,0,:], x[1,1,:],)
plt.plot(x[2,0,:], x[2,1,:],)
plt.plot(x[3,0,:], x[3,1,:],)
plt.show()

# fig = plt.figure(figsize=(5, 4))
# ax = fig.add_subplot(autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2.))
# ax.set_aspect('equal')
# ax.grid()

# line, = ax.plot([], [], 'o-', lw=2)
# trace, = ax.plot([], [], '.-', lw=1, ms=2)
# time_template = 'time = %.1fs'
# time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


# def animate(i):
#     x_c = x[:,:,i]
#     thisx = [ x_c[0,0], x_c[1,0]]
#     thisy = [ x_c[0,1], x_c[1,1]]


#     line.set_data(thisx, thisy)
#     #trace.set_data(history_x, history_y)
#     time_text.set_text(time_template % (i))
#     return line, time_text


# ani = animation.FuncAnimation(
#     fig, animate, len(x), blit=True)

# plt.show()