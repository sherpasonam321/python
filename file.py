import os, shutil
# file handling -> open file,close file,read file,write and maintain files

# my_file = open('test.txt')
# print(my_file)
# print(my_file.read())
# print(my_file.writable())
# my_file.close()

# print(my_file.read())

# my_another_file = open('test.txt','r+')
# print(my_another_file.readable())
# print(my_another_file.writable())
# print(my_another_file.read())
# my_another_file.write('ram \n')



# my_another_file = open('test.txt','w')
# print(my_another_file.readable())
# print(my_another_file.writable())

# my_another_file.write('ram')
# print(my_another_file.seek(1))
# print(my_another_file.read())



my_next_file = open('next.txt','a+')
print(my_next_file.readable())
print(my_next_file.writable)
print(my_next_file.write('hello \n world'))

print(my_next_file.seek(0))
print(my_next_file.read())
list1 = ['ram','shyam','hari']
print(my_next_file.writelines(list1))
print(my_next_file.seek(0))

print(my_next_file.readline())
print(my_next_file.readlines())

# shutil.copy('next.txt','next.txt')
# os.remove('next.txt')

shutil.move('test.txt','next1.txt')











