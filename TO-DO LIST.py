import os
import json


class Task:

    def __init__(self, task_id, description, status, due_date=None):
        self.task_id = task_id
        self.description = description
        self.status = status
        self.due_date = due_date


class TodoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists('tasks.txt'):
            with open('tasks.txt', 'r') as f:
                tasks_data = json.load(f)
                for task_data in tasks_data:
                    task = Task(**task_data)
                    self.tasks.append(task)

    def save_tasks(self):
        tasks_data = [task.__dict__ for task in self.tasks]
        with open('tasks.txt', 'w') as f:
            json.dump(tasks_data, f)

    def list_tasks(self):
        for task in self.tasks:
            status = "Done" if task.status else "Not Done"
            due_date = task.due_date if task.due_date else "N/A"
            print(f"{task.task_id}.{task.description}[{status}]Due:{due_date}")

    def add_task(self, description, due_date=None):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, description, False, due_date)
        self.tasks.append(new_task)
        self.save_tasks()

    def update_task(self, task_id, description, status=None, due_date=None):
        task = self.find_task(task_id)
        if task:
            if description:
                task.description = description
            if status is not None:
                task.status = status
            if due_date:
                task.due_date = due_date
            self.save_tasks()
        else:
            print("Task not found.")

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
        else:
            print("Task not found.")

    def find_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None


def main():
    todo_list = TodoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. List tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            todo_list.list_tasks()
        elif choice == '2':
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            todo_list.add_task(description, due_date)
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            description = input("Enter new description(or press Enter):")
            status = input("Is the task done? (y/n): ").lower() == 'y'
            due_date = input("Enter new due date(or press Enter for current):")
            todo_list.update_task(task_id, description, status, due_date)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == '5':
            print("Exiting To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
