from task import Task
# Manages the collection of tasks
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)
        print(f"Task '{task_name}' added.")

    def remove_task(self, task_name):
        if not self.tasks:
            print("Error: No tasks to remove.")
            return
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task_name) 
                print(f"Task '{task_name}' removed.")
                return
        print(f"Error: Task '{task_name}' not found.")

    def mark_task_complete(self, task_name):
        if not self.tasks:
            print("Error: No tasks to mark as complete.")
            return
        
        for task in self.tasks:
            if task.name == task_name:
                task.mark_complete()
                print(f"Task '{task_name}' marked as complete.")
                return
        
        self.tasks[-1].mark_complete()
        print(f"Task '{task_name}' not found, but marked the last task as complete.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Your tasks:")
            for i, task in enumerate(self.tasks):
                print(f"{i}. {task}") 
