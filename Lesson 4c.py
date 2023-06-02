def Area_circle(pi=3.142):
    radius=21
    Area=pi*radius**2
    print("the area of the circle is",Area)
Area_circle()

def Division(num1,num2):
    division=num1/num2
    print(f"the division of{num1}and{num2}is {division}")
Division(num2=10, num1=50)

def Simple_Interest(p,r,t):
    SI=p*t*r /100
    print(SI)
Simple_Interest(30000,4,2)
# create a program to grade students based on their performance,use marks,name as parameter

        
def Performance(marks,name):
    

    if marks>=0 and  marks<40:
        print(f'marks ={marks}:','Failed')
    elif marks>=40 and marks <50:
        print(f'marks ={marks}:','Grade D')   
    elif marks>=50 and marks<60:
        print(f'marks ={marks}:','Grade C') 
    elif marks >=60 and marks<70:
        print(f'marks ={marks}:','Grade B') 
    elif marks >=70 and marks <=100:
        print(f'marks ={marks}:','Grade A') 
    else:
        print('invalid input')
        
Performance(56,"Sam")

# with name
def performance(marks,name):
    if marks>=0 and  marks<40:
        print("Student name=",name)
        print("Student marks=",marks)
        print("Performance= Grade Failed")
    elif marks>=40 and marks <50:
        print("Student name=",name)
        print("Student marks=",marks)
        print("Performance= Grade D") 
    elif marks>=50 and marks<60:
        print("Student name=",name)
        print("Student marks=",marks)
        print("Performance =Grade C")
        
    elif marks >=60 and marks<70:
        print("Student name=",name)
        print("Student marks=",marks)
        print("Performance =Grade B")
    elif marks >=70 and marks <=100:
        print("Student name=",name)
        print("Student marks=",marks)
        print("Performance =Grade A")
    else:
        print('invalid input')
performance(80,"Kasyoki")