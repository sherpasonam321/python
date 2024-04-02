capital = {
    "nepal":"Kathmandu",
    "india":"New delhi",
    "china":"Beijing"

}
print(capital)
print(len(capital))
print(type(capital))

print(capital.keys())#gives list of keys in the dictionary
print(capital.values())#gives list values in the dictionary

print(capital['nepal'])#give the values of given key
capital['japan'] ="Tokyo" #adds the value in the dictionary
print(capital)
print ['Bhutan'] ="Thimpu"
pop_element = capital.pop("bhutan")
print(pop_element)
print(capital)

a={1,2,3,4}
b=(1,2,3,4)



print(marks)
capital.update(marks)
print(capital)
a =(1,2,3,4)
b = (1,2,3,4)
c = ['a','b','c','e','f']
print(c.index('a'))#gives the index number of given data
c.sort()#ascending order
print(c)
mark ={
    "Maths": 80,
    "Science":80,
    "Nepali ":80, 
}
print(marks)

copy_capital = capital.copy()
print("this is a copy capital:",copy_capital)
clearcapital = capital.clear()
print(clearcapital)
