import Rhino.Geometry as rg
from Grasshopper import DataTree
from Grasshopper.Kernel.Data import GH_Path

# 保護 tol 輸入
if tol is None or tol == 0:
    tol = 1.0
tol = float(tol)

def get_xy_key(crv, tolerance):
    mid = crv.PointAtNormalizedLength(0.5)
    rx = round(mid.X / tolerance) * tolerance
    ry = round(mid.Y / tolerance) * tolerance
    return (rx, ry)

shape_map = {}
shape_counter = [0]

out = DataTree[object]()

for path in x.Paths:
    floor_idx = path.Indices[0]
    for crv in x.Branch(path):
        key = get_xy_key(crv, tol)
        if key not in shape_map:
            shape_map[key] = shape_counter[0]
            shape_counter[0] += 1
        sid = shape_map[key]
        out.Add(crv, GH_Path(sid, floor_idx))

a = out
