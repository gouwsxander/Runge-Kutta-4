from math import *
from matplotlib import pyplot as plt

# A differential equation y'(t) = f(t,y)
def f(t,y):
    return y**(1/2) - y/t

# Initial conditions
t0 = 1
y0 = 0.000001

# Time step and simulation endpoint
delta_t = 0.001
t_final = 10

# Updates y
def update(t, y):
    # Increments
    k1 = delta_t * f(t,y)
    k2 = delta_t * f(t + delta_t/2, y + k1 * delta_t/2)
    k3 = delta_t * f(t + delta_t/2, y + k2 * delta_t/2)
    k4 = delta_t * f(t + delta_t, y + k3 * delta_t)

    # y_(i+1)
    y_next = y + (k1 + 2*k2 + 2*k3 + k4)/6
    return y_next

if __name__ == "__main__":
    N = int((t_final - t0)/delta_t) + 1 # Time steps
    states = [[],[]] # State array

    # Set intial conditions
    states[0].append(t0)
    states[1].append(y0)

    # Main loop
    for i in range(N):
        # Sets current state
        t = states[0][i]
        y = states[1][i]

        # Calculates updated variables
        t_next = t + delta_t
        y_next = update(t, y)

        # Updates state array
        states[0].append(t_next)
        states[1].append(y_next)

    # Plots y over t
    plt.plot(states[0], states[1], 'k')
    plt.show()
