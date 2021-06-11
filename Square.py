#sqare shape
#Calculate the CG of a square.

import math

#insert the inuts of your shape:
unit = "mm"

#insert the dimensions of your shape:
Height = 10;
Length = 200;

#Software do the calculations
Area = Height*Length;

Cgx = Height/2;
Cgy = Length/2;

Ix= (Length*Height**3)/12;
Iy= (Height*Length**3)/12;

#Software print the results:
print("");
print(" ");
print("Welcome to the Square Properties Calculator");
print("-----------------");
print("Area: "+str(Area)+unit+"^2");
print("-----------------");
print("CGx: "+str(Cgx)+unit);
print("CGy: "+str(Cgy)+unit);
print("-----------------");
print("Moment of inertia:");
print("X axix: "+str(Ix)[0:7]+unit+"^4");
print("Y axix: "+str(Iy)[0:9]+unit+"^4");
