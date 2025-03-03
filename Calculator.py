def Calculator():
    
    while True:
        num1 =int(input("Enter the first number:"))
        num2 =int(input("Enter the second number:"))
        
        print("1.Addition")
        print("2.Substraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")
        
        choice =int(input("Enter your choice:"))
        
        if choice == 1:
            print("Addition of",num1,"and",num2,"is",num1+num2)
        elif choice == 2:
            print("Substraction of",num1,"and",num2,"is",num1-num2)
        elif choice == 3:
            print("Multiplication of",num1,"and",num2,"is",num1*num2)
        elif choice == 4:
            if num2 != 0:        
                print("Division of",num1,"and",num2,"is",num1/num2)
            else:
                print("Error! Division by zero is not allowed")
        elif choice == 5:
            print("Exiting the calculator")
            break
        else:
            print("Invalid choice")

Calculator()



