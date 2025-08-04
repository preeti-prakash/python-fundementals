# namedtuple - simple and easy to create lightweight object type like struct

from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
# print(pt)           (x=1, y=-4)
# print(pt.x, pt.y)      1 -4
