#user define function
def BMI():
    weight=int(input(("Enter Value of Weight:")))
    height=float(input("Enter Value for Height:"))
    BMI=weight/height**2
    print(f"The BMI value is:{BMI}")
    return BMI

def patient():
    name='Moses'
    Hospital="Kenyatta"
    print(f"After the lab test at{Hospital}hospital,{name}had a BMI value of {BMI()}")


# functions with parameters and arguments
def medical_records(p_id,condition):
    statement=f"patient with id number {p_id} has been diagnised with {condition}"
    print(statement)
medical_records (p_id="Z0967",condition="Malaria")
medical_records(896454,"Diabetes")