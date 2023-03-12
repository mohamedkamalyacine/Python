# ======================= Q1 ======================= #
"""
class Rectangular:

    def __init__(self) -> None:
        self.width = 0
        self.hight = 0

    def area(self, width, hight):
        return width * hight


rect_1 = Rectangular()
print(f"Rect Area = {rect_1.area(5,10)}")
"""

# ======================= Q2 ======================= #
"""
from math import pi
class Circle:
    def __init__(self) -> None:
        radius = 0
    
    def circumference(self, radius):
        return 2 * pi * radius

cir_1 = Circle()
print(f"{cir_1.circumference(5)}")
"""

# ======================= Q3 ======================= #
"""
class Employee:
    def __init__(self) -> None:
        name = ""
        age = 0
        salary = 0
    
    def raiseSalary(self, salary, percentage):
        return salary + (salary * (percentage/100))

emp_1 = Employee()
print(f"Employee's new salary = {emp_1.raiseSalary(5000, 10)}")
"""

# ======================= Q4 ======================= #
"""
class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  def display(self):
    print(f"Book Title: {self.title}\nAuthor: {self.author}")

b1 = Book("Salah El-din", "Kamal")
b1.display()
"""

# ======================= Q5 ======================= #
"""
class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
    
    def drive(self, amount):
        return self.mileage + amount

car_1 = Car("BMW", "BN15987", 2023, 220)
print(f"{car_1.drive(80)}")
"""
# ======================= Q6 ======================= #
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Intilizations has been successfully\nName: {self.name}\nAge : {self.age}")

    def __del__(self):
        print(f"The object has been destructed")

p1 = Person("Kamal", 25)
"""

# ======================= Q7 ======================= #
"""
class BankAccount:
    def __init__(self, accountNumber, balance):
        self.accountNum = accountNumber
        self.balance = balance
        print(f"Initialization has been successfully\nAccount Number: {self.accountNum}\nBalance: {self.balance}")
    
    def __del__(self):
        print(f"The object has been destructed")

acc_1 = BankAccount("100200300", 10000)
"""

# ======================= Q8 ======================= #
"""
class Vehicle:
    def __init__(self, speed) -> None:
        self.speed = speed

class Car(Vehicle):
    def __init__(self, speed, brand) -> None:
        super().__init__(speed)
        self.brand = brand
    
    def getCarDetails(self):
        return {"Speed":self.speed, "Brand": self.brand}

myCar = Car(280, "BMW")
print(f"My car --> {myCar.getCarDetails()}")
"""

# ======================= Q9 & Q10 ======================= #
"""
class Animal:
    def __init__(self, name):
        self.name = name

class Pet:
    def __init__(self, owner):
        self.owner = owner

class Dog(Animal, Pet):
    def __init__(self, name, owner, breed):
        # super().__init__(name)
        Animal.__init__(self, name)
        Pet.__init__(self, owner)
        self.breed = breed

    def getDogDetails(self):
        return {"name": self.name, "owner": self.owner, "Breed": self.breed}

myDog = Dog("Anfield", "Kamal", "German")
print(f"My Dog details: {myDog.getDogDetails()}")
"""

# ======================= Q11 ======================= #
"""
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        self.salary = salary    

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

    def getManagerInfo(self):
        return {"Name": self.name, "Salary": self.salary, "Department": self.department}

man_1 = Manager("Kamal", 1000000, "Electronics")
print(f"ManagerData: {man_1.getManagerInfo()}")
"""

# ======================= Q12 & Q13 ======================= #
"""
from math import pi
class Shape:
    def __init__(self, color):
        self.color = color

class Rectangular(Shape):
    def __init__(self, color, width, height):
        Shape.__init__(self, color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, color, radius):
        Shape.__init__(self, color)
        self.radius = radius
    
    def area(self):
        return pi * (self.radius**2)


rect = Rectangular("RED", 5, 10)
circ = Circle("Blue", 5)

print(f"Rectangle Areal: {rect.area()}\nCircle Area: {circ.area()}")
"""

# ======================= Q14 ======================= #
"""
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        self.__balance -= amount
    
    def getBalance(self):
        return self.__balance

myAcc = BankAccount(5000)
print(f"My Balance: {myAcc.getBalance()}")
myAcc.deposit(800)
print(f"My Balance After Deposit: {myAcc.getBalance()}")
myAcc.withdraw(1800)
print(f"My Balance After Withdraw: {myAcc.getBalance()}")
"""

# ======================= Q15 ======================= #
"""
import abc
class Animal:
    @abc.abstractmethod
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("Meaw, Meaw")

class Dog(Animal):
    def speak(self):
        print("I can bite you")

myCat = Cat()
myDog = Dog()
myCat.speak()
myDog.speak()
"""

# ======================= Q16 ======================= #
class Calculator:
    @classmethod
    def sum(cls, num1, num2):
        return num1 + num2


print(f"Sum = {Calculator.sum(2,3)}")