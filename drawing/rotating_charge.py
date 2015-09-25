import cadquery
from Helpers import show


outerRadius = 50
outerThick = 5
innerRadius = 2.5
innerThick = 80

# Create a 3D box based on the dimension variables above
result = cadquery.Workplane("XY").circle(outerRadius)

result = result.extrude(outerThick)

result = result.faces(">Z").circle(innerRadius)

result = result.extrude(innerThick)

# Render the solid
show(result)
