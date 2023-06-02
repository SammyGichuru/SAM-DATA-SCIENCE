# conditional statements
marks=int(input('enter marks:'))
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
        
