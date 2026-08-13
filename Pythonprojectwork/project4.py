#Functional Treat
#Data Analyzer and Transformer Program


data = []
summary = {}

def inputdata():
    """
    Prompts the user to create either a 1D list or a 2D matrix.
    
    Returns:
        list: A 1D list of ints, a 2D nested list of ints, or an empty list.
    """
    global data
    print("1. 1D Array")
    print("2. 2D Array")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        userinput = input("Enter values with spaces: ")
        data = []
        for x in userinput.split():
            data.append(int(x))
        print("Data saved successfully!")
        print(data)
        
    elif choice == 2:
        rows = int(input("Enter rows: "))
        cols = int(input("Enter columns: "))
        data = []
        for i in range(rows):
            rowinput = input("Enter row " + str(i + 1) + " values: ")
            row = []
            for x in rowinput.split():
                row.append(int(x))
            data.append(row)
            
        print("2D Array:")
        for r in data:
            for item in r:
                print(item, end=" ")
            print()
    else:
        print("Invalid choice")

def getvalues():
    """
    Convert 1D OR 2D data into one flat list.
    
    Returns:
        list: A single 1D list containing all individual integer values,
            or an empty list if no data exists.
    """
    if len(data) == 0:
        return []
    if type(data[0]) == list:
        vals = []
        for row in data:
            for item in row:
                vals.append(item)
        return vals
    return data

def showsummary():
    """
    Display basic statistics using built-in functions.
    
    This function flattens the dataset, checks for valid items,
    and prints key statistical benchmarks directly to the console.
    """
    vals = getvalues()
    if len(vals) == 0:
        print("Please enter data first.")
        return
    print("Data Summary:")
    print("Total elements:", len(vals))
    print("Minimum value:", min(vals))
    print("Maximum value:", max(vals))
    print("Sum:", sum(vals))
    print("Average:", round(sum(vals) / len(vals), 2))

def showargs(*vals):
    """
    Display multiple values using *args.
    
    Args:
        *values: A variable-length argument list containing elements
            to be displayed side-by-side.
    """
    print("Values using *args:")
    for v in vals:
        print(v, end=" ")
    print()

def showkwargs(**vals):
    """
    Display dataset information using keyword arguments (**kwargs).
    
    Args:
        **values: Named key-value attributes passed to the function.
    """
    print("Dataset Summary using **kwargs:")
    for k, v in vals.items():
        print(k, ":", v)

def factorial(n):
    """
    Calculate the factorial of a given integer using mathematical recursion.
    
    Args:
        n (int): The target non-negative integer.
    Returns:
        int: The factorial product value.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def filterdata():
    """
    Filters out numeric elements using filter() paired with an inline lambda function.
    """
    vals = getvalues()
    if len(vals) == 0:
        print("Please enter data first.")
        return
    limit = int(input("Enter threshold value: "))
    result = list(filter(lambda x: x >= limit, vals))
    print("Values greater than or equal to", limit, ":")
    print(result)

def doublevalues():
    """
    Transforms the array elements by doubling each number using map() and lambda.
    """
    vals = getvalues()
    if len(vals) == 0:
        print("Please enter data first.")
        return
    result = list(map(lambda x: x * 2, vals))
    print("Original values:", vals)
    print("Doubled values:", result)

def storesummary():
    """
    Saves computed descriptive dataset calculations to the global summary dictionary.
    """
    global summary
    vals = getvalues()
    if len(vals) == 0:
        print("Please enter data first.")
        return
    summary["Total"] = len(vals)
    summary["Minimum"] = min(vals)
    summary["Maximum"] = max(vals)
    summary["Average"] = round(sum(vals) / len(vals), 2)
    print("Summary stored successfully.")

def getstats():
    """
    Calculates summary variables and bundles them into an unpacked tuple output.
    
    Returns:
        tuple: (minimum, maximum, total_sum, average)
    """
    vals = getvalues()
    if len(vals) == 0:
        return 0, 0, 0, 0
    mn = min(vals)
    mx = max(vals)
    tot = sum(vals)
    avg = tot / len(vals)
    return mn, mx, tot, avg

def sortdata():
    """
    Sorts elements. Modifies flat sequences sequentially using standard list sorting structures.
    """
    vals = getvalues()
    if len(vals) == 0:
        print("Please enter data first.")
        return
    print("1. Ascending")
    print("2. Descending")
    choice = int(input("Enter choice: "))
    if choice == 1:
        vals.sort()
        print("Ascending:", vals)
    elif choice == 2:
        vals.sort(reverse=True)
        print("Descending:", vals)
    else:
        print("Invalid choice.")

def show2d():
    """
    Validates array alignment configurations and prints multidimensional tables into grids.
    """
    if len(data) == 0:
        print("Please enter data first.")
        return
    if type(data[0]) != list:
        print("Current data is not a 2D array.")
        return
    print("2D Array Grid:")
    for row in data:
        for val in row:
            print(val, end=" ")
        print()

print("Welcome to Data Analyzer and Transformer")

while True:
    print("=== MAIN MENU ===")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Factorial")
    print("4. Filter Data using Lambda")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Display 2D Array")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        inputdata()

    elif choice == 2:
        showsummary()

    elif choice == 3:
        num = int(input("Enter a number: "))
        if num < 0:
            print("Factorial is not possible for negative numbers.")
        else:
            print("Factorial of", num, "is:", factorial(num))
    elif choice == 4:

        filterdata()

    elif choice == 5:
        sortdata()

    elif choice == 6:
        mn, mx, tot, avg = getstats()
        if len(getvalues()) == 0:
            print("Please enter data first.")
        else:
            print("Dataset Statistics:")
            print("Minimum:", mn)
            print("Maximum:", mx)
            print("Sum:", tot)
            print("Average:", round(avg, 2))

    elif choice == 7:
        show2d()
        
    elif choice == 8:
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")