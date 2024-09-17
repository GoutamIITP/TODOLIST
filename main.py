# main.py
from task_manager import TaskManager
from task import Task

def main():
    task_manager = TaskManager()

    while True:
        print("\n1. Add Task\n2. Update Task Status\n3. List Tasks\n4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            new_task = Task(title, description)
            task_manager.add_task(new_task)
            print("Task added successfully!")

        elif choice == "2":
            task_title = input("Enter task title to update status: ")
            new_status = input("Enter new status (Incomplete/Complete): ")
            task_manager.update_task_status(task_title, new_status)
            print("Task status updated successfully!")

        elif choice == "3":
            print("\n--- Task List ---")
            task_manager.list_tasks()

        elif choice == "4":
            print("Exiting ToDo List App. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
