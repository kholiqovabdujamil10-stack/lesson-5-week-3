# 1
# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def make_sound(self):
#         print(f"{self.name} makes sound")
# class Dog(Animal):
#     def make_sound(self):
#         print(f"{self.name}: Woof!")
# class Cat(Animal):
#     def make_sound(self):
#         print(f"{self.name}: Moew!")
# class Bird(Animal):
#     def make_sound(self):
#         print(f"{self.name}: Tweet!")
# dog1 = Dog("Rex")
# cat1 = Cat("MOMO")
# bird1 = Bird("Kesha")

# lict = [dog1, cat1, bird1]

# for i in lict:
#     i.make_sound()


# 2
# from enum import *
# class Shape:
#     def area(self):
#         pass
# class Circle(Shape):
#     def area(self,r):
#         print("Circle:",3.1415 * r ** 2 )
# class Rectangle(Shape):
#     def area(self,a,b):
#         print("Rectangle:",a*b)
# class Square(Shape):
#     def area(self,a):
#         print("Square:",a**2)
# c = Circle()
# r = Rectangle()
# s = Square()

# c.area(5)
# r.area(4,5)
# s.area(3)

# 3
# class EmailSender:
#     def send(self, message):
#         return f"Email: {message}"
# class SMSSender:
#     def send(self, message):
#         return f"SMS: {message}"
# class TelegramSender:
#     def send(self, message):
#         return f"Telegram: {message}"
# def notify(sender, message):
#     print(sender.send(message))
# message = "Lesson starts at 18:00"
# senders = [EmailSender(),SMSSender(),TelegramSender()]

# for i in senders:
#     notify(i, message)

# 4
# class Calculator:
#     def add(self, *numbers):
#         if 2 <= len(numbers) <= 4:
#             return sum(numbers)
#         return "Invalid number of arguments"
# tests = [
#     (5),
#     (5, 10),
#     (1, 2, 3),
#     (1, 2, 3, 4),
#     (1, 2, 3, 4, 5)
# ]
# calculator = Calculator()
# for numbers in tests:
#     print(calculator.add(*numbers))


# 5
# from abc import *
# class Notification(ABC):
#     @abstractmethod
#     def send(self, message, recipient):
#         pass
# class EmailNotification(Notification):
#     def send(self, message, recipient):
#         print(f"Sent email to {recipient}: {message}")
# class SMSNotification(Notification):
#     def send(self, message, recipient):
#         print(f"Sent SMS to {recipient}: {message}")
# message = "Hello"
# notifications = [
#     (EmailNotification(), "kholiqovabdujamil10@mail.com"),
#     (SMSNotification(), "+992007113757")
# ]
# for notification, recipient in notifications:
#     notification.send(message, recipient)
# print("Notification is abstract")


# 6
# from abc import *
# class PaymentMethod(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass
#     @abstractmethod
#     def refund(self, amount):
#         pass
# class CardPayment(PaymentMethod):
#     def pay(self, amount):
#         if amount > 0:
#             print(f"Card payment: {amount}")
#     def refund(self, amount):
#         if amount > 0:
#             print(f"Card refund: {amount}")
# class CashPayment(PaymentMethod):
#     def pay(self, amount):
#         if amount > 0:
#             print(f"Cash payment: {amount}")
#     def refund(self, amount):
#         if amount > 0:
#             print(f"Cash refund: {amount}")
# class CryptoPayment(PaymentMethod):
#     def pay(self, amount):
#         if amount > 0:
#             print(f"Crypto payment: {amount}")
#     def refund(self, amount):
#         if amount > 0:
#             print(f"Crypto refund: {amount}")
# def process_payment(method, amount):
#     method.pay(amount)
# payments = [
#     (CardPayment(), 250),
#     (CashPayment(), 100),
#     (CryptoPayment(), 75)
# ]

# for a, b in payments:
#     process_payment(a, b)

# 7
# from abc import *

# class Exporter(ABC):
#     @abstractmethod
#     def export(self,name, age):
#         pass 
# class CSVExporter(Exporter):
#     def export(self,name, age):
#         print(f"CSV: name,age | {name}, {age}")
# class JSONExporte(Exporter):
#     def export(self,name, age):
#         print(f'JSON: name": {name}, "age": {age}')
# class XMLExporter(Exporter):
#     def export(self,name, age):
#         print(f'XML: <person><name>{name}</name><age>{age}</age></person>')
# name1= "Ali"
# age1 = 22
# E = [CSVExporter(), JSONExporte(), XMLExporter()]
# for i in E:
#     i.export(name1,age1)


# 9
# class Course:
#     def __init__(self, code, title, price=0):
#         self.code = code
#         self.title = title
#         self.price = price
#         self.students = []
#     def enroll(self, student_name):
#         if student_name in self.students:
#             print(f"Duplicate student: {student_name}")
#         else:
#             self.students.append(student_name)
#     def __len__(self):
#         return len(self.students)
# py = Course("PY", "Python", 500)
# dj = Course("DJ", "Django", 700)
# py.enroll("Ali")
# py.enroll("Sara")
# py.enroll("Ali")
# print(f"PY students: {py.students}")
# print(f"DJ students: {dj.students}")
# print(f"PY count: {len(py)}")
# print(f"DJ count: {len(dj)}")


10