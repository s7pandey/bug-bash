# Represents a single task in the to-do list
class Task:
    def __init__(self, name):
        if name.strip():
            self.name = name
            self.completed = False
        else:
            print("Error: Task name cannot be empty.")
    
    def mark_complete(self):
        pass
    
    def __str__(self):
        status = "Completed" if self.completed else "Incomplete"
        return f"{self.name} - {status}"