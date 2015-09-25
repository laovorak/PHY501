# This example is meant to be used from within the CadQuery module of FreeCAD.
import cadquery
from Helpers import show
import math
import numpy as np

radius = 25.0
helicalPeriod = 50.0
helicalRadius = 30.0
steps = 50
height = 2*helicalPeriod
stepSize = height/steps

X = np.array([helicalRadius*math.cos(2*math.pi*n/helicalPeriod*stepSize) for n in range(steps)])
Y = np.array([helicalRadius*math.sin(2*math.pi*n/helicalPeriod*stepSize) for n in range(steps)])
deltaX = np.diff(X)
deltaY = np.diff(Y)

result = cadquery.Workplane("XY").circle(radius)

#create bunches of vertically offset planes
#center is relative to the previous point
for n in range(steps-1):
    result = result.center(deltaX[n],deltaY[n]).workplane(offset=stepSize).circle(radius)


#loft once at the end
result = result.loft(combine=True)

show(result)
