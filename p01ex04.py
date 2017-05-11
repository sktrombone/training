x,y=17528,1482
#y=

for (z,a) in zip([x*y,x/y,x+y,x-y,x%y],["*","/","+","-","%"]):
    print(x,a,y,"=",z)

