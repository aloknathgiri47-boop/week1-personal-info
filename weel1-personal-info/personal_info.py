# Personal Information Manager
# Created by Aloknath Giri

print("=" * 40)
print("   PERSONAL INFORMATION MANAGER")
print("=" * 40)

name = "Aloknath Giri"
age = 18
city = "Palghar"
hobby = "Coding"

favorite_food = input("Enter your favorite food: ")

while favorite_food == "":
    print("Food cannot be empty!")
    favorite_food = input("Enter your favorite food: ")

favorite_color = input("Enter your favorite color: ")

while favorite_color == "":
    print("Color cannot be empty!")
    favorite_color = input("Enter your favorite color: ")

age_in_months = age * 12

print("\n" + "=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)

print(f"Name : {name}")
print(f"Age : {age} years ({age_in_months} months)")
print(f"City : {city}")
print(f"Hobby : {hobby}")
print(f"Favorite Food : {favorite_food}")
print(f"Favorite Color : {favorite_color}")

print("=" * 40)
print("Thanks for using the program!")
print("=" * 40)