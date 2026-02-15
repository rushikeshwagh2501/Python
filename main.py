# main.py

from controllers.student_controller import StudentController
from views.student_view import StudentView

def main():
    student_controller = StudentController()
    student_view = StudentView()

    while True:
        choice = student_view.display_menu()
        
        if choice == '1':
            student_info = student_view.prompt_for_student_info()
            student_controller.add_student(student_info)
        elif choice == '2':
            student_controller.list_students()
        elif choice == '3':
            student_id = student_view.prompt_for_student_id()
            student_controller.remove_student(student_id)
        elif choice == '4':
            break
        else:
            student_view.display_error("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()