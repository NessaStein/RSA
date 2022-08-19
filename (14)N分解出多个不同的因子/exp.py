#!/usr/bin/python
#coding:utf-8

import gmpy2
from Crypto.Util.number import long_to_bytes

n= 544187306850902797629107353619267427694837163600853983242783
e= 39293
c= 439254895818320413408827022398053685867343267971712332011972
p1 = 67724172605733871
p2 = 11571390939636959887
p3 = 694415063702720454699679
phi = (p1-1)*(p2-1)*(p3-1)  
d = gmpy2.invert(e, phi)  
m = pow(c, d, n)  
print long_to_bytes(m) 