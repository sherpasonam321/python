#functiuon is a block of code . we used function to reuse the code . two types of function 
#1. building function
#2 .user defined function

#def function_name ():
     #function body 

    # function() 
#def helloworld():
   # print("hello world!")
#helloworld()
# def hello(name,course_name):
#     print("hello",name,"Welcome to web development traning")
#     print(course_name)

#     hello('ram','python with django')#argument

# def hello(name, course_name): #parameter

#     print('Hello', name, "welcome to web develpoment traning")
#     print(course_name)
#     hello(name='sonam',course_name='python with data science')#arguments

# def sum(*args):
#     total = 0
#     for n in args:
#      total+=n

#     return total #return gives result of function and stop the execution of function 
#     result = sum(2,3,5)
    # print(result)

# l = float(input('enter a length :'))
# w = float(input('enter a width:'))

def area():
     h= float(input("enter the area"))
     global area_of_object
     area_of_object = l*w
     return area_of_object

     result=area()
     result_volume = volumne()
     print(result)

# def volume():
#     h= float(input("enter the height"))
#     v=l*w*h
#     return v 


# result = area()
# result_volume = volume()
# print(result)

# print(result_volume)

x = lambda a, b: a+b
area = x (2,3)
print(area)


# recursive function - function calling itsself again and again 
def factorical(n):
    if n == 0:
        return 1 
    else:
        return n*factorical(n-1)
        



    # filter()
    # map()

    

