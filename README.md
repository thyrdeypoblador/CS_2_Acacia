# CS_2_Acacia
This program calculates the distance between two points on a Cartesian plane.

## How to run the program
1. Open program
2. Enter Values 
3. Get Results
4. Close Program After Use

## Input 
- Enter required value for x1
- Enter required value for x2
- Enter required value for y1
- Enter required value for y2

## Sample Output
import math
x1 = float(input("Enter x1 value"))
x2 = float(input("Enter x2 value"))
y1 = float(input("Enter y1 value"))
y2 = float(input("Enter y2 value"))

x = x2 - x1
y = y2 - y1
xsqrt = math.pow(x, 2)
ysqrt = math.pow(y, 2)
d = math.sqrt(xsqrt + ysqrt)

print("The distance between the two points is", d)

## Author
Name: Thyrdey Aiden James B. Poblador
Section: Grade 8 - Acacia
