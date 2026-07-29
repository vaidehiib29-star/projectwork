students = []
subjects_set = set()
print("Welcome to the student Data Organizer!")
while True:
    print("""Select an opetion:
    1. Add Student
    2. Display All Students
    3. Update Student Information
    4.Delete Student
    5. Display Subjects Offered
    6. Exit""")

    choice = (input("Enter your choice: "))

    if choice == "1":
        print("Enter student details: ")
        student_id = int(input("student ID: "))
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")

        subjects = input("subjects (comma-separated): ").split(",")
        subjects = [subject.strip() for subject in subjects]
        student_info = (student_id,dob)

        student = {
            "id":student_id,
            "info":student_info,
            "name":name,
            "age":age,
            "grade":grade,
            "subjects":subjects
        }

        students.append(student)
        for subject in subjects:
            subjects_set.add(subject)
        print("\nstudent added successfully!")
    elif choice == "2":
        print("\nDisplay All Students: ")
        if len(students) == 0:
            print("No student records found.")      
        else:
            for student in students:
                print(
                    f"student ID: {student['id']} |"
                    f"Name: {student['name']} |"
                    f"Age: {student['age']} |"
                    f"Grade: {student['grade']} |"
                    f"subjects: {','.join(student['subjects'])}" 
                )
    elif choice == "3":
        print("\n Update Student Information: ")

        update_id = int(input("Enter student ID to update"))
        found = False
        for student in students:  
            if student["id"] == update_id:
                found = True
                student["age"] = int(input("Enter new age: "))
                new_subjects = input("Enter new subjects(comma-seprated):").split(",")
                new_subjects = [subject.strip() for subject in new_subjects]
                student["subjects"] = new_subjects
                for subject in new_subjects:
                    subjects_set.add(subject)
                print("Student information updated successfully!")
                break
            if not found:
                print("Student ID not found")   
    elif choice == "4":
        delete_id = int(input("Enter student ID to delete: "))
        found = False
        for i in range(len(students)):
            if students[i]["id"] == delete_id:
                found = True
                print("Student information deleted successfully!")
                break
            if not found:
                print("Student not found.")
    elif choice == "5":
        print("\n subjects offered")
        if len(subjects_set) == 0:
            print("No subjects available.")
        else:
            for subject in subjects_set:
                print(subject) 
    elif choice == "6":
        print("\n Thank you for using the student Data Organizer!")
        break
    else:
        print("Invalid choice. Please try again.")                           

         

                      




