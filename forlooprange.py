#range()to get range of number
for i in range(1,21):
    if i % 3 ==0 and i % 5 ==0:
          print("fizzbuzz")
    elif i  % 3 ==0:
          print("fizz")
    elif i % 5 ==0:
          print("buzz")
    else:
          print(i)



#nested loop is loop inside loop
for i in range(1,11):
     print("Multiplkication table : ", i)  
     for j in range(1,11):
      print(i,"*",j,"=",i*j) 



a=['red','white','pink','black']
b=['football','basetball','volleyball']  
for i in a:
    for j in b:
     print(i,j, end=" ") 

     x = 0
     while x<=10:

        j=0
        while j <=10:
            j +=1
            print(x,"*",j,"=",x*j)
            j +=1
        x +=1
        for i in range(1,11):
            print("multiplfication:",i)
            j = 1
            while j <=10:
                print(i,"*",j,"=",i*j)

    

