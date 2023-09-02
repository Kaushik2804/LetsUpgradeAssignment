def area(side):
    return side * side


side = int(input("Enter the value of side:"))

if side == 0:
    print("Not a valid value for side")
else:
    area_of_square = area(side)
    print("Area of square:", area_of_square)
