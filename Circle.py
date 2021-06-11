#Circle shape
#Calculate the CG of a circle.

import math

#insert the inuts of your shape:
unit = "mm"

#insert the dimensions of your shape:
diameter = 100;

#Software do the calculations
Area = math.pi*(diameter/2)**2;

Cgx = diameter/2;
Cgy = diameter/2;

Ix= (math.pi*diameter**4)/64;
Iy= (math.pi*diameter**4)/64;

#Software print the results:
print("");
print(" ");
print("Welcome to the Circle Properties Calculator");
print("-----------------");
print("Area: "+str(Area)+unit+"^2");
print("-----------------");
print("CGx: "+str(Cgx)+unit);
print("CGy: "+str(Cgy)+unit);
print("-----------------");
print("Moment of inertia:");
print("X axix: "+str(Ix)+unit+"^4");
print("Y axix: "+str(Iy)+unit+"^4");
