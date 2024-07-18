import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def ellipse_points(a, b, num_frames):
    t = np.linspace(0, 2 * np.pi, num_frames)
    x = a * np.cos(t)
    y = b * np.sin(t)
    return x, y

def init_plot(ax, a, b):
    ax.set_xlim(-a-1, a+1)
    ax.set_ylim(-b-1, b+1)
    ax.set_aspect('equal')
    ax.set_title('Ball Moving on an Ellipse')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    return plt.plot([], [], 'ro', markersize=8)[0]

def update_ball(i, x, y, ellipse):
    ellipse.set_data(x[i], y[i])
    return ellipse,

def create_animation(x, y, num_frames):
    fig, ax = plt.subplots()
    ellipse = init_plot(ax, a, b)

    ani = animation.FuncAnimation(
        fig, update_ball, frames=num_frames,
        fargs=(x, y, ellipse), interval=20, blit=True
    )
    return ani

# Parameters
a = 5  # Semi-major axis
b = 3  # Semi-minor axis
num_frames = 200

# Generate ellipse points
x, y = ellipse_points(a, b, num_frames)

# Create and display animation
ani = create_animation(x, y, num_frames)
plt.show()
