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
    y = y + xprev[-1] - y[0]
    return x[1:], y[1:]

def snowflake_interval(n):
    if n == 0:
        return np.array([0, 0]), np.array([1, 0])
    x0, y0 = snowflake_interval(n-1)
    x1, y1 = scale(x0, y0, 1/3)
    x2, y2 = startat(x1, y1, x1, y1)
    x2, y2 = rotate(x2, y2, np.pi / 3)
    x3, y3 = startat(x1, y1, x2, y2)
    x3, y3 = rotate(x3, y3, -np.pi / 3)
    x4, y4 = startat(x1, y1, x3, y3)
    return np.concatenate([x1, x2, x3, x4]), np.concatenate([y1, y2, y3, y4])

x, y = snowflake_interval(1)
print(x, y)
fig = p.figure(figsize=(8, 8))
p.fill(x, y)
p.axis('off')
fig.show(True)
p.pause(3)
