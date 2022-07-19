from matplotlib import pyplot as p
from matplotlib.lines import Line2D
import numpy as np
import time

def rotate(x, y, theta):
    x0 = x[0]
    y0 = y[0]
    xa = x - x0
    ya = y - y0
    xb = xa * np.cos(theta) - ya * np.sin(theta)
    yb = xa * np.sin(theta) + ya * np.cos(theta)
    xc = xb + x0
    yc = yb + y0
    return xc, yc

def scale(x, y, s):
    x0 = x[0]
    y0 = y[0]
    xa = x - x0
    ya = y - y0
    xb = x * s
    yb = y * s
    xc = xb + x0
    yc = yb + y0
    return xc, yc

def startat(x, y, xprev, yprev):
    x = x + xprev[-1] - x[0]
    y = y + yprev[-1] - y[0]
    return x, y

def join(x, y):
    x0 = x[:-1]
    x1 = x[1:]
    y0 = y[:-1]
    y1 = y[1:]
    dist = np.sqrt((x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1))
    preserve = np.concatenate(([True], 1e-12 < dist))
    return x[preserve], y[preserve]

def snowflake_interval(n):
    if n == 0:
        return np.array([0, 1]), np.array([0, 0])
    x0, y0 = snowflake_interval(n-1)
    x1, y1 = scale(x0, y0, 1/3)
    x2, y2 = startat(x1, y1, x1, y1)
    x2, y2 = rotate(x2, y2, np.pi / 3)
    x3, y3 = startat(x1, y1, x2, y2)
    x3, y3 = rotate(x3, y3, -np.pi / 3)
    x4, y4 = startat(x1, y1, x3, y3)
    return join(np.concatenate([x1, x2, x3, x4]), np.concatenate([y1, y2, y3, y4]))

def run():
    x1, y1 = snowflake_interval(6)
    x2, y2 = startat(x1, y1, x1, y1)
    x2, y2 = rotate(x2, y2, -2 * np.pi / 3)
    x3, y3 = startat(x2, y2, x2, y2)
    x3, y3 = rotate(x3, y3, -2 * np.pi / 3)
    x, y = join(np.concatenate([x1, x2, x3]), np.concatenate([y1, y2, y3]))
    
    #x, y = snowflake_interval(6)
    print(x, y)
    fig = p.figure(figsize=(8, 8))
    y += np.sqrt(3) / 2
    scale = np.sqrt(3) / 2
    x *= scale
    y *= scale
    x += (1 - np.sqrt(3)/2) / 2
    print(np.max(x))
    p.xlim(0, 1)
    p.ylim(0, 1)
    p.fill(x, y, c='black', lw=0)
    p.axis('off')
    p.savefig("snowflake.pdf")
    fig.show(True)
    p.pause(3)

if __name__ == "__main__":
    run()
    pass
