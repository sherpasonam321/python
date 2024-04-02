# class person:
#     def person_info(self,name,age):
#         print('inside person class')
#         self.name = name
#         print('name :',name,'age: ',age)

# class company:
#     def company_info(self,company_name,location):
#         print('inside company class')
#         print('name',company_name, 'location',location)

# class employee(person, company):
#     def employee_info(self,salary,skill):
#      super().person_info('sonam',20)
#      print('inside empoloyee')




class vehicle:
     def __init__(self,name,color,price):
        self.name = Name
        self.color = color
        self.price = price

     def show(self):
        print('details:',self.name,self.color,self.price)

     def max_speed(self):
        print("vehicle max speed is 150")

     def change_gear(self):
        print('vechicle change 6 gear')
    
class car(vehicle):
     def max_speed(self):
        print('car max speed is 240')

     def change_gear(self):
        print('vechicle change 6 gear')

car = car('car x1','red',200000)

car.show()
car.max_speed()
car.change_gear()

#calculatng the area of different shapes.we'll create a base class shape with an area()method,and then create sub class
# 



import math

class shape:
    def area(self):
      raise NotImplementedError("subclaasses must implement this method")

class rectangle(shape):
   def __init__(self,width,height):
      self.width = width
      self.height = height
   
def area(self):
   return self.width *self.height

class circle(shape):
   def __init__(self,rsdius):
      self.radius = radius

   def are(self):
      return math.pi * self.radius **2
class triangle(shape):
   def __init__(self,base, height):
      self.base = Base
      self.height =height

   def area(self):
      return 0.5 *self.base * self.height

      # create instance of different shapes

      rectangle = Rectangle(5,4)
      circle = circle(3)
      triangle = triangle(6 ,8)

      print("area of rectangle:",rectangle.area())
      print("area of circle:",circle.area())
      print("area of triangle:",triangle.area())


