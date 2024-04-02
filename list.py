
thislist = ["python","java","C++"]
print (thislist)
count = thislist.count('python')
print(count)

laptops = ['dell','hp','sony','lenovo','aser','mac']

laptops.append("microsoft")
print(laptops)
laptops.insert(2, "microsoft")
print(laptops)
laptops
laptops.remove("dell")
print(laptops)
remove_elemet = laptops.pop(3)
print('removed_element')
print(laptops)
a = [1,2,3,4,5]

laptops.extend(a)
print(laptops)

b= [1,2,3,4,5,6,7,8,9,]
laptops.extend(b)
print(laptops)

count = laptops.count("microsoft")
print(count)
copy_list = laptops.copy()
print("this is an orginal list ; " ,laptops)
print("this is a copy list :" ,copy_list)
copy_list.clear ()
print(copy_list)