# 1. შექმენი წრის კლასი, რომელსაც ექნება მეთოდები საკუთარი პერიმეტრისა და ფართობის გამოსათვლელად.

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return self.radius * 2 * math.pi

    def area(self):
        return self.radius ** 2 * math.pi


circle1 = Circle(10)

print(circle1.perimeter())
print(circle1.area())




# 2. შექმენი კალკულატორის კლასი, საბაზისო არითმეტიკული ოპერაციების მეთოდებით.


class Calculator:
    def addition(self, num1, num2):
        assert type(num1) is int or float, "Parameters can only be integers or floats."
        assert type(num2) is int or float, "Parameters can only be integers or floats."
        return num1 + num2

    def subtraction(self, num1, num2):
        assert type(num1) is int or float, "Parameters can only be integers or floats."
        assert type(num2) is int or float, "Parameters can only be integers or floats."
        return num1 - num2

    def multiplication(self, num1, num2):
        assert type(num1) is int or float, "Parameters can only be integers or floats."
        assert type(num2) is int or float, "Parameters can only be integers or floats."
        return num1 * num2

    def division(self, num1, num2):
        assert type(num1) is int or float, "Parameters can only be integers ar floats."
        assert type(num2) is int or float, "Parameters can only be integers or floats."
        assert num2 != 0, "Can not divide by zero."
        return num1 / num2

    def exponentiation(self, num1, num2):
        assert type(num1) is int or float, "Parameters can only be integers ar floats."
        assert type(num2) is int or float, "Parameters can only be integers or floats."
        return num1 ** num2

    def floor_division(self, num1, num2):
        assert type(num1) is int or float, "Parameters can only be integers ar floats."
        assert type(num2) is int or float, "Parameters can only be integers or floats."
        assert num2 != 0, "Can not divide by zero."
        return num1 // num2

    def reminder_finder(self, num1, num2):
        assert type(num1) is int or float, "Parameters can only be integers ar floats."
        assert type(num2) is int or float, "Parameters can only be integers or floats."
        assert num2 != 0, "Can not divide by zero."
        return num1 % num2


math_operation = Calculator()
print(math_operation.addition(2, 3))
print(math_operation.subtraction(2, 3))
print(math_operation.multiplication(2, 3))
print(math_operation.division(2, 3))
print(math_operation.exponentiation(2, 3))
print(math_operation.floor_division(2, 3))
print(math_operation.reminder_finder(2, 3))




# 3. შექმენი შოფინგის კალათის კლასი, რომელსაც ექნება მეთოდები სასურველი ნივთის დასამატებლად და ამოსაშლელად,
# ასევე კალათაში არსებული პროდუქტების სიისა და ჯამური ღირებულების გამოსატანად.

class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, item_price):
        assert type(item_name) is str, "Item name must be a string."
        assert type(item_price) is int or float, "Price must be a number."
        self.items[item_name] = item_price

    def remove_item(self, item):
        assert item in self.items.keys(), "Item is not in the cart."
        del self.items[item]

    def list_items(self):
        return self.items

    def total_price(self):
        return sum(self.items.values())


shopping_list = Cart()
shopping_list.add_item("spinner", 8)
shopping_list.add_item("toaster", 35)
shopping_list.add_item("machete", 83)
shopping_list.add_item("torch", 24)
shopping_list.remove_item("torch")
print(shopping_list.list_items())
print(shopping_list.total_price())