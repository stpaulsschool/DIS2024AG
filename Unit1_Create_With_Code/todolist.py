#I want a program that asks the user for a title of a book then returns a number how long the string is.
todo_list = []

def add_task(task):
    todo_list.append(task)
    print("Task added: ", task)

def edit_task(index, new_task):
    todo_list[index] = new_task
    print("Task edited: ", todo_list[index])

def view_tasks():
    if not todo_list:
        print("No tasks to show")
    else:
        for i, task in enumerate(todo_list):
            print(i+1, task)

while True:
    print("\nWhat would you like to do?")
    print("1. Add task")
    print("2. Edit task")
    print("3. View tasks")
    print("4. Quit")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        task = input("Enter task: ")
        add_task(task)
    elif choice == 2:
        view_tasks()
        index = int(input("Enter task number to edit: "))-1
        new_task = input("Enter new task: ")
        edit_task(index, new_task)
    elif choice == 3:
        view_tasks()
    elif choice == 4:
        break
    else:
        print("Invalid choice, please try again")