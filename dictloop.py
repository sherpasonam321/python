dictionary = {}

dictionary ['name']="ram"
dictionary['age']=18
dictionary['subject']=['maths','science','nepali']
dictionary['education'] = {
    'school':{
    'name':'xavier school',
    'address' : 'kalopul,kathmandu'
    },
'high school':{'name':'DAV college',
                'address':'jawalakhel' 'lalitpur'},
'bachlor level':{
         'name':'xavier college',
         'address':'baudha,kathmandu'
           }
}
print(dictionary)

for i in dictionary.keys():

 print(i)
 
#accessing elements of nested dictionary form the loop
for i,j in dictionary['education']['school'].items ():
    print(i, "=",j)

    print(dictionary['education']['school']['name'])

   



