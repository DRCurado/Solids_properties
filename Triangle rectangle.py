#triangle shape
#Calculate the CG of a triangle rectangle.

import math

#insert the inuts of your shape:
unit = "mm"

#insert the dimensions of your shape:
base = 100;
heigth = 100

#Software do the calculations
Area = base*heigth/2;

Cgx = base/3;
Cgy = heigth/3;

Ix= (base*heigth**3)/36;
Iy= (heigth*base**3)/36;

#Software print the results:
print("");
print(" ");
print("Welcome to the Triangle Rectangle Properties Calculator");
print("-----------------");
print("Area: "+str(Area)+unit+"^2");
print("-----------------");
print("CGx: "+str(Cgx)+unit);
print("CGy: "+str(Cgy)+unit);
print("-----------------");
print("Moment of inertia:");
print("X axix: "+str(Ix)+unit+"^4");
print("Y axix: "+str(Iy)+unit+"^4");
