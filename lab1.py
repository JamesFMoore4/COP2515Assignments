#The code for this project represents my own, independent work. I have neither given nor received help on this assignment from otherstudents.

#James Moore

#Code to estimate the area of a circle with circumference 100

circumference_circle = 100
pi = 3.1416
r = circumference_circle / (2 * pi)
area_circle = pi * r ** 2

print(area_circle)

#Code to estimate the area of a flower with radius 4.5

pi = 3.1416
radius_total = 4.5
radius_semi = (1 / 2) * radius_total
area_semi = (1 / 2) * pi * radius_semi ** 2
area_square = (2 * radius_semi) ** 2
area_flower = (4 * area_semi) + area_square

print(area_flower)

#Code that outputs area of a flower with a user-given radius

pi = 3.1416
radius_total = float(input("Enter the radius of a flower: "))
radius_semi = (1 / 2) * radius_total
area_semi = (1 / 2) * pi * radius_semi ** 2
area_square = (2 * radius_semi) ** 2
area_flower = (4 * area_semi) + area_square

print(area_flower)

#Code that outputs the dollar value of a loan after a certain amount of time

principle = float(input("Enter the principle: "))
interest_rate= float(input("Enter the interest rate: "))
time= float(input("Enter the time (in years): "))

e= 2.718
value_loan = principle * e ** (interest_rate * time)

print(value_loan)



