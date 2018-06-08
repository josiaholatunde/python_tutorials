def calculator():
   
    def get_user_input(msg):
        user_input = float(input("Enter the "+ msg+ " number: "))
        return user_input

        
    def add(x,y):
        return x + y

    def sub(x,y):
        return x - y
    
    def divide(x,y):
        if y == 0:
            return "Invalid Result...Division by zero"
        else:
            return x / y
    
    def multiply(x,y):
        return x * y
    
    while True:
        print("Options")
        print("Enter 'add' to add two numbers")
        print("Enter 'subtract' to subtract two numbers")
        print("Enter 'divide' to divide two numbers")
        print("Enter 'multiply' to multiply two numbers")
        print("Enter 'quit' to exit the calculator")

        user_operator = input(':')

   

        if user_operator == 'add':
            #global user_input1,user_input2
            user_input1 = get_user_input('first')
            user_input2 = get_user_input('second')
            result = add(user_input1,user_input2)
            print("The sum of "+str(user_input1)+" and "+str(user_input2)+" is "+str(result))
            
        elif user_operator == 'subtract':
            user_input1 = get_user_input('first')
            user_input2 = get_user_input('second')
            result = sub(user_input1,user_input2)
            print("The difference of "+str(user_input1)+" and "+str(user_input2)+" is "+str(result))

        elif user_operator == 'divide':
            user_input1 = get_user_input('first')
            user_input2 = get_user_input('second')
            result = divide(user_input1,user_input2)
            print(str(user_input1)+" / "+str(user_input2)+" is "+str(result))


        elif user_operator == 'multiply':
            user_input1 = get_user_input('first')
            user_input2 = get_user_input('second')
            result = multiply(user_input1,user_input2)
            print(str(user_input1)+" * "+str(user_input2)+" is "+str(result))
            
        elif user_operator == 'quit':
            print("Exiting calculator...")
            break;
        else:
            print("Invalid User Input");


        print("\n")




       

        
           


calculator()        
    
