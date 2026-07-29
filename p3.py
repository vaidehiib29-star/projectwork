print("Welcome to the Student Data Organizer!")

data = {}
lst = []
subs = set()

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    
    c = int(input("Enter your choice: "))
    
    if c == 1:
        print("\nEnter student details:")
        id = input("Student ID: ")
        n = input("Name: ")
        a = int(input("Age: ")) 
        g = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        s = input("Subjects (comma-separated): ")
        
        tup = (id, dob) 
        slist = s.split(",")
        
        for x in slist:
            subs.add(x)
        
        d = {"name": n, "age": a, "grade": g, "subs": slist, "tup": tup}
        
        data[id] = d
        lst.append(d)
        
        print("Student %s added successfully!" % n)
        
    elif c == 2:
        print("\n--- Display All Students ---")
        for k in data:
            v = data[k]
            n = v["name"]
            a = v["age"]
            g = v["grade"]
            s = v["subs"]
            print(f"Student ID: {k} | Name: {n} | Age: {a} | Grade: {g} | Subjects: {s}")
            
    elif c == 3:
        id = input("Enter Student ID to update: ")
        if id in data:
            print("1. Update Age")
            print("2. Update Grade")
            print("3. Update Subjects")
            u = int(input("Choice: "))
            
            if u == 1:
                na = int(input("New Age: "))
                data[id]["age"] = na
                n = data[id]["name"]
                print("Age for {} updated!".format(n))
                
            elif u == 2:
                ng = input("New Grade: ")
                data[id]["grade"] = ng
                n = data[id]["name"]
                print("Grade for {} updated!".format(n))
                
            elif u == 3:
                print("1. Add Subject")
                print("2. Remove Subject")
                su = int(input("Choice: "))
                
                if su == 1:
                    ns = input("New subject name: ")
                    data[id]["subs"].append(ns)
                    subs.add(ns)
                    print("Subject added!")
                    
                elif su == 2:
                    rs = input("Subject name to remove: ")
                    if rs in data[id]["subs"]:
                        data[id]["subs"].remove(rs)
                        print("Subject removed!")
                    else:
                        print("Subject not in list.")
                        
        else:
            print("ID not found.")
            
    elif c == 4:
        id = input("Enter Student ID to delete: ")
        if id in data:
            del data[id]
            print("Student deleted successfully!")
        else:
            print("ID not found.")
            
    elif c == 5:
        print("\nSubjects Offered:")
        for x in subs:
            print(x)
            
    elif c == 6:
        print("\nThank you for using the Student Data Organizer!")
        break