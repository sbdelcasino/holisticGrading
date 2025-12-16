from course import Course
from assignment import Assignment, AssignmentList

def add_assignment_to_course(course):
    print("\nEnter assignment details:")
    category = input("Category: ")
    points_earned = float(input("Points Earned: "))
    points_total = float(input("Points Total: "))
    weight = float(input("Assignment Weight: "))
    course.add_assignment(points_earned, points_total, weight, category)
    print("Assignment added!\n")

def display_assignments(course):
    print(f"\nAssignments for {course.name}:")
    current = course.assignments.head
    if not current:
        print("No assignments yet.")
        return
    idx = 1
    while current:
        print(f"{idx}. Category: {current.assignmentCategory}, "
              f"Points Earned: {current.pointsEarned}, "
              f"Points Total: {current.pointsTotal}, "
              f"Weight: {current.assignmentWeight}")
        current = current.next
        idx += 1

def modify_assignment(course):
    assignments = []
    current = course.assignments.head
    while current:
        assignments.append(current)
        current = current.next

    if not assignments:
        print("No assignments to modify.")
        return

    display_assignments(course)
    choice = int(input("Enter assignment number to modify: "))
    if 1 <= choice <= len(assignments):
        a = assignments[choice - 1]
        print("\n1. Change Points Earned")
        print("2. Change Points Total")
        print("3. Change Weight")
        print("4. Change Category")
        option = input("Select field to modify: ")
        if option == "1":
            a.pointsEarned = float(input("New Points Earned: "))
        elif option == "2":
            a.pointsTotal = float(input("New Points Total: "))
        elif option == "3":
            a.assignmentWeight = float(input("New Weight: "))
        elif option == "4":
            a.assignmentCategory = input("New Category: ")
        else:
            print("Invalid option.")
    else:
        print("Invalid assignment number.")

def course_menu(course):
    while True:
        print(f"\n=== {course.name} Menu ===")
        print("1. Add Assignment")
        print("2. Display Assignments")
        print("3. Modify Assignment")
        print("4. Return to Main Menu")
        choice = input("Enter choice: ")

        if choice == "1":
            add_assignment_to_course(course)
        elif choice == "2":
            display_assignments(course)
        elif choice == "3":
            modify_assignment(course)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def StartCourseManager():
    courses = []

    while True:
        print("\n=== Main Menu ===")
        print("a. Create New Course")
        for idx, course in enumerate(courses, start=1):
            print(f"{idx}. Enter {course.name}")
        print("q. Quit")

        choice = input("Enter choice: ")

        if choice == "a":
            name = input("Enter course name: ")
            new_course = Course(name)
            courses.append(new_course)
            print(f"Created course '{name}'")
        elif choice == "q":
            print("Exiting Course Manager...")
            break
        else:
            try:
                choice_int = int(choice)
                if 1 <= choice_int <= len(courses):
                    # Enter the selected course menu
                    course_menu(courses[choice_int - 1])
                else:
                    print("Invalid course number.")
            except ValueError:
                print("Invalid input. Enter a number or 'a' to create a course.")