
import math


# ===========================================================================
# Function to check collisions between two circles
# ===========================================================================
def collision2Circles(center1, radius1, center2, radius2):
    x1, y1 = center1
    x2, y2 = center2
    dx = x2 - x1
    dy = y2 - y1
    sr = radius1 + radius2
    return (dx*dx+dy*dy) < (sr*sr)


# ===========================================================================
# Function to check collisions between two axis-aligned bounding box (AABB)
# ===========================================================================
def collision2AABB(topLeft1, bottomRight1, topLeft2, bottomRight2):
    x1, y2 = topLeft1
    x2, y1 = bottomRight1
    x3, y4 = topLeft2
    x4, y3 = bottomRight2
    # Horizontal and vertical collisions
    hc = (x4 >= x1) and (x3 <= x2)
    vc = (y4 >= y1) and (y3 <= y2)
    return (hc and vc)


# ===========================================================================
# Function to check collisions between one AABB and one point
# ===========================================================================
def collisionPointAABB( topLeft, bottomRight, pos ):
    x1, y2 = topLeft
    x2, y1 = bottomRight
    x, y   = pos
    return (x1 <= x <= x2) and (y1 <= y <= y2)

# ===========================================================================
# Function to check collisions between one Circle and one point
# ===========================================================================
def collisionPointCircle(center, radius, pos):
    return collision2Circles(center, radius, pos, 0)


# ===========================================================================
# Function to check collisions between one Circle and one AABB
# ===========================================================================
def __segmentProjection(center, corner1, corner2):
    Cx, Cy = center
    Ax, Ay = corner1
    Bx, By = corner2
    dACx = Cx - Ax
    dACy = Cy - Ay
    dABx = Bx - Ax
    dABy = By - Ay
    dBCx = Cx - Bx
    dBCy = Cy - By
    k1 = (dACx * dABx) + (dACy * dABy)
    k2 = (dBCx * dABx) + (dBCy * dABy)
    return k1*k2 <= 0

def collisionCircleAABB( topLeft, bottomRight, center, radius ):
    # first check the circle AABB collision
    if not collision2AABB(topLeft, bottomRight, (center[0]-radius, center[1]+radius), (center[0]+radius, center[1]-radius)):
        return False
    # Now check one of the corner is in the circle
    tl = collisionPointCircle(center, radius, topLeft)
    br = collisionPointCircle(center, radius, bottomRight)
    tr = collisionPointCircle(center, radius, (bottomRight[0], topLeft[1]))
    bl = collisionPointCircle(center, radius, (topLeft[0], bottomRight[1]))
    if tl or br or tr or bl:
        return True
    # Now check the center of the circle is in the AABB
    if collisionPointAABB(topLeft, bottomRight, center):
        return True
    # Check projection on the AABB
    # Horizontal
    hor = __segmentProjection(center, (topLeft[0], bottomRight[1]), (topLeft[0], topLeft[1]))
    # Vertical
    ver = __segmentProjection(center, (topLeft[0], bottomRight[1]), (bottomRight[0], bottomRight[1]))
    if hor or ver:
        return True
    # Ok there is no collision
    return False


# ===========================================================================
# Function to check collisions between one Ellipse and one AABB
# ===========================================================================
def collisionEllipseAABB( topLeft, bottomRight, center, radiusX, radiusY ):
    x0, y1 = topLeft
    x1, y0 = bottomRight
    cx, cy = center
    # change 2d space
    x0 = (x0 - cx) / radiusX
    x1 = (x1 - cx) / radiusX
    y0 = (y0 - cy) / radiusY
    y1 = (y1 - cy) / radiusY
    return collisionCircleAABB((x0,y1), (x1,y0), (0,0), 1)

# ===========================================================================
# Function to check collisions between one Ellipse and one Circle
# ===========================================================================
def ellipsePointFromAngle(center, radiusX, radiusY, ang):
    c = math.cos(ang)
    s = math.sin(ang)
    ta = s / c  ## tan(a)
    tt = ta * radiusX / radiusY  ## tan(t)
    d = 1. / math.sqrt(1. + tt * tt)
    x = center[0] + math.copysign(radiusX * d, c)
    y = center[1] - math.copysign(radiusY * tt * d, s)
    return x, y

def collisionCircleEllipse( center1, radius1, center2, radius2X, radius2Y ):
    dx = center1[0] - center2[0]
    dy = center1[1] - center2[1]
    angle = math.atan2(-dy, dx)
    x, y = ellipsePointFromAngle(center2, radius2X, radius2Y, angle)
    distance  = math.hypot(x - center1[0], y - center1[1])
    distance2 = math.hypot(center2[0] - center1[0], center2[1] - center1[1])
    return distance <= radius1 or distance2 <= radius1

# ===========================================================================
# Function to check collisions between two Ellipses
# ===========================================================================
def collision2Ellipses(center1, rx1, ry1, center2, rx2, ry2):
    cx1, cy1 = center1
    cx2, cy2 = center2
    # change 2d space
    rx2 /= rx1
    ry2 /= ry1
    cx2 = (cx2 - cx1) / rx1
    cy2 = (cy2 - cy1) / ry1
    return collisionCircleEllipse( (0,0), 1, (cx2,cy2), rx2, ry2 )
