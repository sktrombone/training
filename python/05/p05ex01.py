from math import sin,cos,tan,pi
for i in range(91):
    s=i*pi/180
    print("{0:3d},{1:9f},{2:9f},{3:9f}".format(i,sin(s),cos(s),tan(s)))
