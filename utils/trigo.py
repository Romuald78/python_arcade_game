import math


# ===========================================================================
# Function to get a position of a rotated point
# ===========================================================================
def rotate(pos, pivot, angle):
    COS = math.cos(angle*math.pi/180)
    SIN = math.sin(angle*math.pi/180)
    x0, y0 = pos
    xp, yp = pivot
    x0 -= xp
    y0 -= yp
    x1 = (x0 * COS) - (y0 * SIN)
    y1 = (x0 * SIN) + (y0 * COS)
    x1 += xp
    y1 += yp
    return x1, y1