from students import Student_det

def main():
    print("------ Student Details ------")

    student1 = Student_det("Vaidu")
    student2 = Student_det("ishu")
    student3 = Student_det("Kusha")
    student4 = Student_det("Alia")

    student1.add_marks([98, 56, 78])
    student2.add_marks([77, 55, 90])
    student3.add_marks([97, 67, 45])
    student4.add_marks([73, 88, 53])

    all_students = [
        student1,
        student2,
        student3,
        student4
    ]

    print("\n------ All Student Records ------")

    records = Student_det.display_students(all_students)

    for record in records:
        print(record)

    print("\n---- Students with Average 80 or More ----")

    filtered_students = Student_det.filter_students(all_students)

    for student in filtered_students:
        print(student.get_data())

    print("\n---- Students Sorted By Average ----")

    sorted_students = Student_det.sort_students(all_students)

    for student in sorted_students:
        print(student.get_data())

if __name__ == "__main__":
    main()

