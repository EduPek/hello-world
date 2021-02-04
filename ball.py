#Program for computing the height of a ball in vertical motion  


import numpy as np  
import matplotlib.pyplot as plt 
from math import * 


v0 = 5 #Initial velocity  
g = 9.81 #Acceleration of gravity  
t = np.linspace(0, 1.01, 1001) # Time

y = v0*t - 0.5*g*t**2 #Vertical position  

print t
print y

plt.plot(t, y) 
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.show()



x = 10 #Horizontal position  
y = 10 #Vertical position  

angle = atan(y/x)  

print (angle/pi)*180 


L = 4 # Side of the Cube
V = L**3

print 'Volume of a Cube of side', L ,' is equal to ' ,V 

L = np.linspace(1,3,30)
V = L**3

plt.plot(L,V)
plt.show()
