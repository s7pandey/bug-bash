from taskmanager import TaskManager

# Main application interface
class ToDoApp:
    def __init__(self):
        self.manager = TaskManager()

    def run(self):
        print("Welcome to the To-Do List App")
        while True:
            print("\nMenu:")
            print("1. Add Task")
            print("2. Remove Task")
            print("3. Mark Task as Complete")
            print("4. Display Tasks")
            print("5. Exit")
            
            choice = int(input("Choose an option: "))
            
            if choice == 1:
                task_name = input("Enter the task: ")
                self.manager.add_task(task_name)
            elif choice == 2:
                task_name = input("Enter the task to remove: ")
                self.manager.remove_task(task_name)
            elif choice == 3:
                task_name = input("Enter the task to mark as complete: ")
                self.manager.mark_task_complete(task_name)
            elif choice == 4:
                self.manager.display_tasks()
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                pass

# Run the application
if __name__ == "__main__":
    app = ToDoApp()
    app.run()