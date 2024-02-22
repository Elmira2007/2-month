# class Phone:
#     def init(self, battery):
#         self.battery = battery

#     def str(self):
#         return f"Емкость баттареи {self.battery}"

#     # Магические методы для арифметических действии
#     def add(self, other):  # Операция сложение == (+)
#         new_battery = self.battery + other.battery
#         return Phone(new_battery)
    
#     def sub(self, other):   # Операция вычитание == (-)
#         new_battery = self.battery - other.battery
#         return Phone(new_battery)
    
#     def mul(self, other):   # Операция умножение == (*)
#         new_battery = self.battery * other.battery
#         return Phone(new_battery)
    
#     def floordiv(self, other):  # Операция деление без остатка == (//)
#         new_battery = self.battery // other.battery
#         return Phone(new_battery)
    
#     def truediv(self, other):   # Операция деление с остатком == (/)
#         new_battery = self.battery / other.battery
#         return Phone(new_battery)
    
#     # Магические методы для оператора сравнение
#     def gt(self, other):   # Больше чем == (>)
#         return self.battery > other.battery
    
#     def it(self, other):   # Меньше чем == (<)
#          return self.battery < other.battery
    
#     def eq(self, other):   # Равно == (==)
#          return self.battery == other.battery
    
#     def ne(self, other):   # Не равно == (!=)
#          return self.battery != other.battery
    
#     def ge(self, other):   # Больше или равно == (>=)
#          return self.battery >= other.battery
    
#     def ge(self, other):   # Меньше или равно == (<=)
#          return self.battery >= other.battery
    
#     # Магический метод call
#     def call(self):
#         print("Hello World")
#         print(self.battery <= 7)

# phone = Phone(2000)
# phone_2 = Phone(3000)
# print(phone)

# # Магические методы для арифметических действии
# print(phone + phone_2)
# print(phone - phone_2)
# print(phone * phone_2)
# print(phone // phone_2)
# print(phone / phone_2)

# # Магические методы для оператора сравнение
# print(phone > phone_2)
# print(phone < phone_2)
# print(phone == phone_2)
# print(phone != phone_2)
# print(phone >= phone_2)
# print(phone <= phone_2)

# phone() # call