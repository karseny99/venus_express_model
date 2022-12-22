# Importing Packages
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# venus Model
def model_2BP(state, t):
    mu = 3.24859E+05  # venus's gravitational parameter
    # [km^3/s^2]
    x = state[0]
    y = state[1]
    z = state[2]
    x_dot = state[3]
    y_dot = state[4]
    z_dot = state[5]
    x_ddot = -mu * x / (x ** 2 + y ** 2 + z ** 2) ** (3 / 2)
    y_ddot = -mu * y / (x ** 2 + y ** 2 + z ** 2) ** (3 / 2)
    z_ddot = -mu * z / (x ** 2 + y ** 2 + z ** 2) ** (3 / 2)
    dstate_dt = [x_dot, y_dot, z_dot, x_ddot, y_ddot, z_ddot]
    return dstate_dt


# Initial Conditions
X_0 = -2500  # [km]
Y_0 = -5500  # [km]
Z_0 = 3400  # [km]
VX_0 = 7.76  # [km/s]
VY_0 = 0.0  # [km/s]
VZ_0 = 4.82  # [km/s]
state_0 = [X_0, Y_0, Z_0, VX_0, VY_0, VZ_0]

# Time Array
t = np.linspace(0, 18 * 3600, 200)  # Simulates for a time period of 18 hours

# Solving ODE
sol = odeint(model_2BP, state_0, t)
X_Sat = sol[:, 0]  # X-coord [km] of satellite over time interval
Y_Sat = sol[:, 1]  # Y-coord [km] of satellite over time interval
Z_Sat = sol[:, 2]  # Z-coord [km] of satellite over time interval
# Setting up Spherical venus to Plot
N = 50
phi = np.linspace(0, 2 * np.pi, N)
theta = np.linspace(0, np.pi, N)
theta, phi = np.meshgrid(theta, phi)

r_venus = 6051.8  # Venus radius
X_venus = r_venus * np.cos(phi) * np.sin(theta)
Y_venus = r_venus * np.sin(phi) * np.sin(theta)
Z_venus = r_venus * np.cos(theta)

# Plotting venus and Orbit
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X_venus, Y_venus, Z_venus, color='red', alpha=0.7)
ax.plot3D(X_Sat, Y_Sat, Z_Sat, 'black')
ax.view_init(30, 145)  # Changing viewing angle (adjust as needed)
plt.title('Задача двух тел')
ax.set_xlabel('X [km]')
ax.set_ylabel('Y [km]')
ax.set_zlabel('Z [km]')
# Make axes limits
xyzlim = np.array([ax.get_xlim3d(), ax.get_ylim3d(),
                   ax.get_zlim3d()]).T
XYZlim = np.asarray([min(xyzlim[0]), max(xyzlim[1])])
ax.set_xlim3d(XYZlim)
ax.set_ylim3d(XYZlim)
ax.set_zlim3d(XYZlim * 3 / 4)
plt.show()
