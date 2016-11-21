import math
#1
for i in range(20, 9, -1):
    print(i)

#2
a = [i for i in range(20, 9, -1)]
print(a)
print("Hello")

#3
for i in range(20, 9, -1):
    if i % 2 == 0:
        print(i)
print("World")

#4
b = [i for i in range(20, 9, -1) if i % 2 == 0]
print(b)

#5
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):          #only need to test from 3 to the square root of n
        if n % i == 0:
            return False
    return True

print is_prime(2) #True
print is_prime(4) #False
print is_prime(7) #True
print is_prime(13) #True

#6
def fifth(file):                              #counter idea from Wolflab, thanks Paul!
    with open(file) as handle:
        counter = 1
        for line in handle:
            if counter == 5:                  #If we are on the 5th line
                print(line[4])                #Print the 5th element (python indexing starts at 0)
            counter+=1                        #+= is shorthand for counter = counter + 1
                                              #Having a counter is just an easy way to loop across the lines until you get to a certain line.
print(fifth("simple.txt"))

#7
for i in range(1, 20):
    if i % 5 == 0:
        print("GOOD: " + str(i))
        if is_prime(i) == True:
            print("JOB: " + str(i))

#8
def gompertz(a, b, c, t): #check on TI-89
    y = a*math.exp(-b*math.exp(-c*t))           #If you don't import math, ** will raise to a power
    return(y)

d = gompertz(100, 50, 9, 10)
print(d)

#9
def box(length, width):                         #Inspiration from marleyhaupt1 and Wolflab
    for i in range(0,length):                   #some people are using range(0, length, 1) but you don't need the by = 1, because that is the default value.
        if i == 0 or i == (length-1):           #creates the top and bottom of the box. I like how marleyhaupt1 uses an if statement combined with "or" so that she needs one less line of code.
            print("*" * width)                  #prints *'s to form the top and (eventually) the bottom of the box.
        else:                                   #if we are in the middle section of the box
            print("*" + " " * (width-2) + "*")  #print "* " (which is the left edge of the box) then a certain amount of spaces (the width minus two, because the other two are the *'s that make up the edges of the box,) then one more "*" (which is the right edge of the box.)
f = box(5, 10)
print(f)

#10
class Point: #upper case in Python
    def __init__(self, x, y):                   #always start with "self" argument
        self.x = x
        self.y = y
#11
    def distance(self, point1):                #distance is a method of class Point
        dist= math.sqrt((self.x-point1.x)**2+(self.y-point1.y)**2)
        return(dist)

point_1 = Point(1, 1)                     #setting this up so that the distance should be 1
point_2 = Point(1, 2)                     #point_2 is an instance of class Point
print(point_1.distance(point_2))          #I learned how to call the function this way from bweedop

#12
class Line(Point):
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
line = Line(point_1, point_2)
print(line)
