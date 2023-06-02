#while loop
#executes a block of code as long as the condition is true
count=0
while count<10:
 print(count,'is less than 10')
    #   incriment value of count)
 count=count+1

 number=10
while number <20:
    if number ==15:
     print('number at 15')
    print(number)
    number+=1
    # break and continue
marks =101
while marks >=0 and marks<=100:
    if marks>=0 and  marks<40:
        print(f'marks ={marks}:','Failed')
        break

    elif marks>=40 and marks <50:
        print(f'marks ={marks}:','Grade D')  
        break 
    elif marks>=50 and marks<60:
        print(f'marks ={marks}:','Grade C') 
        break
    elif marks >=60 and marks<70:
        print(f'marks ={marks}:','Grade B') 
        break
    elif marks >=70 and marks <=100:
        print(f'marks ={marks}:','Grade A') 
        break
else:
       print('invalid input')

            
