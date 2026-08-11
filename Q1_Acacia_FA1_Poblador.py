import math

# Enter Values
## Enter Value For x1
x1 = float(input("Enter x1 value"))
## Enter Value For x2
x2 = float(input("Enter x2 value"))
## Enter Value For y1
y1 = float(input("Enter y1 value"))
## Enter Value For y2
y2 = float(input("Enter y2 value"))
# Calculating
x = x2 - x1
y = y2 - y1
xsqrt = math.pow(x, 2)
ysqrt = math.pow(y, 2)
d = math.sqrt(xsqrt + ysqrt)
# Computed Distance Output
print("The distance between the two points is", d)

#Reflection prompts
#Why is using a library more practical than writing all calculations from scratch? Explain briefly using your activity as an example.
#To make the process easier and to make the code readable. In our activity, we used libraries to calculate the distance between two points in a Cartesian Plane using pow() and sqrt(), without the libraries, your code would be 10x bigger, and it made adding, subtracting, etc, different amounts much simpler. Would be better if you calculated on paper instead.


