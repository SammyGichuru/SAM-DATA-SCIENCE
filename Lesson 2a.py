#data types 
#list
#we define a list using square brackets list=[]
#list can contain multiple items
#allows duplicat entries 
#list is ordered
#list is changeable -edit,
#accepts items of all other data types
courses=['Economics','Computer Science','Information Technology','Business Aminstration','Economics']
print(courses)
print(type(courses))
#access items in a list using index
first_item=courses[0]
#print(courses[0])
print(first_item)
#change
courses[0]='Information Science'
print(courses)
#add items to the list
courses.append('Criminology')
print(courses)
count=len(courses)
#print(count)
print(len(courses))
list_2=['first_month,76473,90.87,5654j+7,True']
print(list_2)
print(type(list_2))

#List Constructor
fruits=list(('Mango','Berries','Pineapple'))
print(fruits)
print(type(fruits))

#add item to a secific index 
fruits.insert(1,'Apple')
print(fruits)


#add more than one item  into a list 
fruits_2=['Goose berries','water melon']
fruits.extend(fruits_2)
print(fruits)

#remove
fruits.remove('water melon')
print(fruits)

#pop
fruits.pop(2)
print(fruits)

#delete
del fruits[0]
print(fruits)
#clear
fruits.clear()
print(fruits)