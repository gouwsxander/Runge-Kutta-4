# Runge-Kutta 4 in Python

## About and Dependencies

Many differential equations cannot be solved analytically (mathematically), which is an issue due to their necessity in describing the world. To get by this, scientists turn to numerical methods to approximate solutions. 

The easiest is the **Forward Euler Method**, but it is often not used as its simplicity makes it prone to errors, which often propagate further into other computations. **Runge-Kutta 4** (RK4) is one of a family of methods that builds on the Euler Method - making it more accurate while still being fairly computationally efficient. RK4 is one of the most used numerical differential equation solvers in the world today.

This project is an implementation of RK4 in base Python, but the library [Matplotlib](https://matplotlib.org/) is used for plotting. The standard Python math library is also used to make constants and functions easy to call in code. This code was designed to be used as a standalone program for playing around with RK4, and for serious use-cases I recommend using [SciPy](scipy.org).



## Some Results

### Monotonic solution with small step-size

$$
y'(t) = \sqrt{t} - \frac{y}{t} \quad y(1)=0 \quad \Delta t = 0.001
$$

![Monotonic solution with small step-size](https://i.imgur.com/fOSNtCp.png)

As we can see, RK4 does seem to be implemented correctly here. This differential equation came from a problem in [Paul's online notes](http://tutorial.math.lamar.edu/Classes/DE/Bernoulli.aspx).



### Monotonic solution with large step-size

$$
y'(t) = \sqrt{t} - \frac{y}{t} \quad y(1)=0 \quad \Delta t = 0.1
$$

![Monotonic solution with large step-size](https://i.imgur.com/FLQynSs.png)

Even with relatively large step-sizes, RK4 is fairly accurate, and only begins to deviate (slightly) towards the end of the interval.



### Non-monotonic solution with small step-size

$$
y'(t) = \exp(-t) + \frac{1}{2} \cos(5t) - 2 \sin(2t) \quad y(0)=1 \quad \Delta t = 0.001
$$

![Non-monotonic solution with small step-size](https://i.imgur.com/N4FX4Wx.png)

With near-periodic functions, we can see that RK4 has no issues with small step-sizes.



### Non-monotonic solution with large step-size

$$
y'(t) = \exp(-t) + \frac{1}{2} \cos(5t) - 2 \sin(2t) \quad y(0)=1 \quad \Delta t = 0.1
$$

![Non-monotonic solution with large step-size](https://i.imgur.com/rSeYHty.png)

We can see (at least here) that non-monotonic functions are more accurate at large step-sizes than their monotonic counterparts. This makes sense since differential equations with monotonic solutions tend to result in compounding errors when solved analytically. However, here, a small upwards deviation will result in a stronger downward deviation, putting the solution 'back on track'.



## References/Further Reading

[Euler Method (Wikipedia)](https://en.wikipedia.org/wiki/Euler_method)

[Runge-Kutta Methods (Wikipedia)](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods)

