# exception ->an event that occurs to disrupt the normal flow of operation
# try:
#   age=int(input())
#   print(age)
# except:
#     print('please provide numnberic value')

# print('xavier college ')

# try:
#     a =int(input('enter a value'))
#     b = int(input('enter a value'))
#     c = a+b
# except ValueError:
#     print('please provide your value')
# except ZeroDivisionError:
#     print('zero will not divide any other number ')
# else:
#     print("The value of c is ",c)

user1 = 'admin'
pass1  = 'admin'
try:
    username = input("enter a username = ")
    password = input("enter a password = ")

    if user1 != username:
        raise ZeroDivisionError
    elif pass1 != password:
            raise ValueError

except ZeroDivisionError:
    print("user is invaild")
except ValueError:
    print("password is invaild")
else:
    print("login successful")
finally: 
 print("home")

 login()
    



