# 1. მოცემულ კლასს მოარგე Single Responsibility პრინციპი და შესაბამისად შეცვალე კოდი.
# (კერძოდ დაშალე 4 კლასად User,  Storage,  HttpConnection,  Logger)

# class User:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def save(self):
#         ...
#
#     def send(self):
#         ...
#
#     def log(self):
#         ...


class User:
    def __init__(self, name):
        self.name = name


class GetName(User):
    def get_name(self):
        return self.name


class Save(User):
    def save(self):
        print(f"Saving user {self.name} info...")


class Send(User):
    def send(self):
        print(f"Sending user {self.name} info...")


class Log(User):
    def log(self):
        print(f"Logging user {self.name} info to console...")




# 2. მოცემული გვაქვს Discount კლასი.  Open-Closed პრინციპის გამოყენებით საჭიროა,
# სწორად დავნერგოთ 40%_იანი ფასდაკლების ფუნქციონალი VIP კლიენტებისთვის.

# class Discount:
#   def __init__(self, customer, price):
#       self.customer = customer
#       self.price = price
#
#   def give_discount(self):
#       if self.customer == 'favourite':
#           return self.price * 0.2
#       if self.customer == 'vip':
#           return self.price * 0.4


from abc import ABC, abstractmethod


class Discount(ABC):

    @abstractmethod
    def give_discount(self):
        print("Abstract Discount")


class Customer:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price


class DiscountForFavourite(Customer, Discount):

    def __init__(self, customer, price):
        super().__init__(customer, price)
        self.discount_rate = 0.2

    def give_discount(self):
        if self.customer == 'favourite':
            return self.price * self.discount_rate


class DiscountForVIP(Customer, Discount):

    def __init__(self, customer, price):
        super().__init__(customer, price)
        self.discount_rate = 0.4

    def give_discount(self):
        if self.customer == 'vip':
            return self.price * self.discount_rate
