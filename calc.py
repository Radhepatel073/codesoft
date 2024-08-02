def add(x ,y):
    return x + y 

def mul(num1 ,num2):
            return num1 * num2
def div(num1 ,num2):
            return num1 / num2
def minus(num1 ,num2):
            return num1 - num2

def main():
    num1=float(input('enter the number 1'))
    num2=float(input('enter the number 2'))
#create main function
    print("1-add \n 2-minus \n 3-mul \n 4-div \n 5-exit")
    operation = int(input("enter the opration"))
    if operation == 1:
            print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operation == 2:
            print(f"{num1} - {num2} = {minus(num1, num2)}")
    elif operation == 3:
            print(f"{num1} * {num2} = {mul(num1, num2)}")
    elif operation == 4:
            print(f"{num1} / {num2} = {div(num1, num2)}")
    elif operation == 5:
                    
            print("Exiting the calculator. Goodbye!")
                    

main()