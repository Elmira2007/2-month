# Множественное наследование и Магические методы

# class Parents:
#     def init(self, name, color_eyes):
#         self.name = name
#         self.color_eyes = color_eyes 

#     def str(self):
#         return f"{self.name}, {self.color_eyes}"

# class Father(Parents):
#     def init(self, name, color_eyes, power):
#         Parents.init(self, name, color_eyes)
#         self.power = power

#     def work(self):
#         print("Работа")

#     def str(self):
#         return super().str() + f" сила по 10-шкале {self.power}"
    
# dad = Father("Ким", "Черные", 10)
# print(dad)

# class Mother(Parents):
#      def init(self, name, color_eyes, beauty):
#          Parents.init(self, name, color_eyes)
#          self.beauty = beauty

#      def cook(self):
#          print("Готовка")

#      def str(self):
#         return super().str() + f" Внешность по 10-шкале {self.beauty}"
     
# mom = Mother("Лиса", "Карие", 10)
# print(mom)

# class Child(Father, Mother ):
#     def init(self, name, color_eyes, power, beauty):
#         Father.init(self, name, color_eyes, power)
#         Mother.init(self, name, color_eyes, beauty)
 
#     def info(self):
#         print(f"{self.name}, цвет глаз - {self.color_eyes}, {self.power}, {self.beauty}")

#     def str(self):   # print == str
#         return super().str()

# child = Child("Тэхён", "Карие", 8, 100)
# print(child)
# child.info()
# child.work()
# child.cook()