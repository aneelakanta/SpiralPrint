import numpy as np
import matplotlib.pyplot as plt

def print_spiral():
    theta = np.radians(np.linspace(0, 360 * 4, 800))
    r = theta ** 2
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    plt.plot(x, y)
    plt.title("Spiral")
    plt.axis([-600, 600, -600, 600])
    plt.show()

if __name__ == '__main__':
    print_spiral()