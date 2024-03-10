import math
from re import I

pi = math.pi

x1, y1, x2, y2 = map(int, input().split())
tet = int(input())

if x1 == 0 or x2 == 0:
    r = abs(x1 - x2);
    h = abs(y2 - y1);
    v = (r * r * pi) * h;
    v = v * tet / 360;
elif((x1 > 0 and x2 < 0) or (x1 < 0 and x2 > 0)):
    if (tet > 180):
        h = abs(y2 - y1)
        rMax = max(abs(x1), abs(x2))
        rMin = min(abs(x1), abs(x2))
        tetMin = 360 - tet;
        v1 = rMax * rMax * tet 
        v2 = rMin * rMin * tetMin 
        v = (v1 + v2) * h * pi / 360
    else:
         h = abs(y2 - y1)
         rMax = max(abs(x1), abs(x2))
         rMin = min(abs(x1), abs(x2))
         v = ((rMax * rMax) + (rMin * rMin)) * pi * h * tet / 360
else:
    rMax = max(abs(x1), abs(x2))
    rMin = min(abs(x1), abs(x2))
    h = abs(y2 - y1)
    r = pow(rMax, 2) - pow(rMin, 2)
    v = (r * pi ) * h
    v = v * tet / 360

print(v);