import csv

students = {}
FILE_NAME = "students.txt"



def add_student(student_id, name, age, *grades):
    student_tuple = (student_id, name)
    students[student_id] = {
        "name": name,
        "age": age,
        "grades": list(grades)
    }
    print(f"Student added: {student_tuple}")
    save_to_file()

def update_student(student_id, name=None, age=None, grades=None):
    if student_id in students:
        if name:
            students[student_id]["name"] = name
        if age:
            students[student_id]["age"] = age
        if grades is not None:
            students[student_id]["grades"] = grades
        print(f"Student {student_id} updated.")
        save_to_file()
    else:
        print("Student not found.")

def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        print(f"Student {student_id} deleted.")
        save_to_file()
    else:
        print("Student not found.")

def display_students(from_file=False):
    if from_file:
        load_from_file()
    if not students:
        print("No students found.")
        return
    for sid, info in students.items():
        print(f"ID: {sid}, Name: {info['name']}, Age: {info['age']}")
        print("Grades:", end=" ")
        for g in info["grades"]:
            print(g, end=" ")
        print("\n---")

def save_to_file():
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        for sid, info in students.items():
            row = [sid, info["name"], info["age"]] + info["grades"]
            writer.writerow(row)

def load_from_file():
    global students
    students.clear()
    try:
        with open(FILE_NAME, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                sid, name, age, *grades = row
                students[sid] = {
                    "name": name,
                    "age": int(age),
                    "grades": list(map(int, grades))
                }
    except FileNotFoundError:
        pass


average = lambda grades: sum(grades) / len(grades) if grades else 0

def modify_list(mylist):
    mylist.append(100)
    return mylist

def modify_number(num):
    num += 10
    return num


def main():
    load_from_file()
    while True:
        print("\n===== STUDENT MANAGEMENT MENU =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display Students (from file)")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            sid = input("Enter ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grades = list(map(int, input("Enter grades separated by space: ").split()))
            add_student(sid, name, age, *grades)

        elif choice == "2":
            display_students()

        elif choice == "3":
            sid = input("Enter ID to update: ")
            name = input("Enter new name (press enter to skip): ") or None
            age_input = input("Enter new age (press enter to skip): ")
            age = int(age_input) if age_input else None
            grade_input = input("Enter new grades separated by space (press enter to skip): ")
            grades = list(map(int, grade_input.split())) if grade_input else None
            update_student(sid, name=name, age=age, grades=grades)

        elif choice == "4":
            sid = input("Enter ID to delete: ")
            delete_student(sid)

        elif choice == "5":
            display_students(from_file=True)

        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")
            continue

if __name__ == "__main__":

    t = (1, 2, 3, 4, 5)
    print("Tuple length:", len(t))
    print("Tuple max:", max(t))
    print("Tuple min:", min(t))

    nums = [1, 2, 3]
    print("Before modify_list:", nums)
    modify_list(nums)
    print("After modify_list:", nums)

    n = 50
    print("Before modify_number:", n)
    modify_number(n)
    print("After modify_number:", n)

    main()
