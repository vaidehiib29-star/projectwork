while True:
    print("Welcome to the pattern generator and number analyzer")
    print("""select the option
    1.Generate a pattern
    2.analyze a range of numbers
    3.exit""")
    a=int(input("Enter the option: "))
    if a==1:
        userinput=int(input("Enter the number of rows for the pattern :"))
        for i in range(0,userinput):
            for j in range(i):
                print("*",end="")
            print("")
    elif a==2:
        p=int(input("Enter the start of the range: "))
        q=int(input("Enter the end of the range: "))
        sum=0
        for i in range(p,q+1):
            sum+=i
            if i%2==0:
                print(f"{i} is an even number")
            else:
                print(f"{i} is an odd number")
        print(f"Sum of all numbers from {p} to {q} is {sum}")
    elif     a==3:
        print("Exiting the program ,goodbye!")
        break
    else:
        print("invalid option")


    