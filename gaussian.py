import numpy as np

if __name__ == '__main__':
    px = np.linspace(-1, 1, 100) * 200
    py = np.linspace(-1, 1, 200) * 200
    mesh = np.meshgrid(px, py)
    rho = 0.5
    sxy = [10.0, 20.0]
    wxy = [10.0, 20.0]

    sg = np.matrix([
        [wxy[0]**2, rho * wxy[0] * wxy[1]],
        [rho * wxy[0] * wxy[1], wxy[1]**2]
    ])

    #
    # sg
    # Return the standard deviation of the array elements along the given axis.
    # Returns the variance of the matrix elements, along the given axis.
    # Return the product of the array elements over the given axis.
    #
    print(sg)
    print(sg.std())
    print(np.linalg.inv(sg))
    print(np.linalg.det(sg))
