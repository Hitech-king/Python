def triangle_area():
    base = float(input("Enter base of the triangle: "))
    height = float(input("Enter height of the triangle: "))
    return 0.5 * base * height

def rectangle_area():
    length = float(input("Enter length of the rectangle: "))
    width = float(input("Enter width of the rectangle: "))
    return length * width

def circle_area():
    radius = float(input("Enter radius of the circle: "))
    return 3.14 * radius ** 2

print("Choose a shape to calculate area:")
print("1. Triangle")
print("2. Rectangle")
print("3. Circle")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    print(f"Area of Triangle: {triangle_area():.2f}")
elif choice == "2":
    print(f"Area of Rectangle: {rectangle_area():.2f}")
elif choice == "3":
    print(f"Area of Circle: {circle_area():.2f}")
else:
    print("Invalid choice!")
