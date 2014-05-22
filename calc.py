__author__ = 'harpera'
#print("Hello World")

# milesDriven = int(input("Enter miles driven: "))
# gallonsUsed = int(input("Enter gallons used: "))
# mpg = milesDriven / gallonsUsed
# print("Miles per gallon: ", mpg)

# Calculate kinetic energy

print("This program calculates kinetic energy of a moving object.")
m = float(input("Enter the object's mass in kgs: "))
v = float(input("Enter the object's speed in metres/second: "))

e = 0.5 * m * v * v
print("The object has " + str(e) + " joules of energy.")