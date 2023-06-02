#dictionary
#use curly brackets
#keys and values
#changeable
#does not allow duplicates enteries
#ttake vales from any data type

car={
    'barnd':'ford',
    'model':'mustang',
    'year':1989,
    'year':1967,
    'colours':['red','blue','green'],
    'manual':True

    }
print(car)
print(type(car))
print(len(car))
#access the differebnt values
print(car['barnd'])
print(car.values())
#access the key 
print(car.keys())
#use constrctor to create a dictionary
personX =dict(name='mike',DOB='12/6/2000',nationality='Kenyan')
print(personX)
print(type(personX))

#change
personX['name']='Maureen'
personX.update({'Nationality':'American'})
print(personX)
print(personX.items())

#add item
personX['Profession']='Footballer'
print(personX)

#create an item in personX dict whose value is a list of different data types
personX.update({'colours':"'red',['131j','2456p'],'blue',(20,30,40,50)"})
print(personX)

personX.update({'Hobbies':"['reading','travelling','hiking'],('eating','sleeping','football'),'dancing',897"})
print(personX)

#countries
country={
    'Kenya':[['Nairobi','Makueni','Kajiado'],['Maasai Mara','Lake Naivasha','Nairobi national park']],
    'Uganda':'Kasese',
    'Tanzania':'Katanga'}
print(country['Kenya'])
#print first item in key 
print(country['Kenya'][0])
#access item in the first value
print(country['Kenya'][0][0])
country['Kenya'][0][0]='Kericho'
print(country['Kenya'][0][0])