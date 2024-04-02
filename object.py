#oop in python (object oriented program). we deal with real time object and its entities

# class Room: #blueprint of object.
#     l = int(input("enter the length : "))
#     w = int(input("enter the width : "))

#     def area(self):
#         print("area of room is ",self.l*self.w)

#         area_of_room = Room()
#         print(area_of_room.area())


# class Room():
#  l = int(input("enter the length : "))
# w = int(input("enter the width : "))
# h = int(inpout("enter the height :"))

# def volume(self):
#     print("volume of room is",self.l*self.w,self.h)

#     room = Room()
    

class calculator:
   length = 20
   def __init__(self, num1,num2):
       self.num1 = num1
       self.num2 = num2

   def add(self,*args,**kwargs):
       self.num1 = args[0]
       total = 0
       for n in args:
         total+= n
       return total
   def substrct(self,*args):
    total = args[0]
    total -= n
    return total

    def multiply(self,num1,num2):
        return num1*num2

    def divide(self,num1,num2):
        try:
            return num1/num2
        except ZeroDivisionError:
            print("error:division by zero !")

cal = calculator(1,2)
print(cal.num1)
addition = cal.add(2,3)
print(addition)




