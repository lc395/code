# Function to establish grade category depending on score
def get_grade_category(grade):
    if grade >= 85:
        return 'HD'
    elif grade >= 75:
        return 'D'
    elif grade >= 65:
        return 'C'
    elif grade >= 50:
        return 'P'
    else:
        return 'F'

# A function to return a message for a specific grade category.
def get_category_message(category):
    messages = {
        'HD': "Outstanding performance! Keep it up.",
        'D': "Excellent work!",
        'C': "Good effort!",
        'P': "Satisfactory result but Work hard.",
        'F': "Fail - Needs more improvement."
    }
    return messages.get(category, "There is no message.")

# Adds a new student to the list
def add_student(students):
    name = input("Enter student name: ")
    try:
        grade = int(input("Enter student grade (0-100): "))
        if 0 <= grade <= 100:
            category = get_grade_category(grade)
            message = get_category_message(category)
            students.append({"name": name, "grade": grade, "category": category})
            print(f"Added student: {name} with grade {grade} ({category}) - {message}\n")
        else:
            print("Grade must be between 0 and 100.\n")
    except ValueError:
        print("Invalid input. Grade must be a number.\n")

# To remove the student from the list.
def remove_student(students):
    name = input("Enter student name to remove: ")
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print(f"Removed student: {name}\n")
            return
    print("Student not found.\n")

# Acccording to scenerio update the student grade.
def update_student(students):
    name = input("Enter student name to update: ")
    for student in students:
        if student["name"] == name:
            try:
                new_grade = int(input("Enter new grade (0-100): "))
                if 0 <= new_grade <= 100:
                    category = get_grade_category(new_grade)
                    message = get_category_message(category)
                    student["grade"] = new_grade
                    student["category"] = category
                    print(f"Updated {name}'s grade to {new_grade} ({category}) - {message}\n")
                else:
                    print("Grade must be between 0 and 100.\n")
            except ValueError:
                print("Invalid input. Grade must be a number.\n")
            return
    print("Student not found.\n")

# To show the list of all students with grade and message.
def view_students(students):
    if not students:
        print("No student records found.\n")
        return
    print("\nStudent Records:")
    for student in students:
        name = student["name"]
        grade = student["grade"]
        category = student["category"]
        message = get_category_message(category)
        print(f"- {name}: {grade} ({category}) - {message}")
    print()

# displays the main options from the menu.
def show_menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Student Grade")
    print("4. View All Students")
    print("5. Exit")

# Main loop running the menu system
def main_menu():
    students = []
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            remove_student(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            view_students(students)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Script's entering point
if __name__ == "__main__":
    main_menu()
