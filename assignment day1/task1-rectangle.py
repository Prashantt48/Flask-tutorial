length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print("Area of rectangle:", area)

if length == width:
    print("It is a square.")
else:
    print("It is a rectangle.")