# Task: Simple To-Do (TASK) List




# Define a function called 'menu' that displays options and takes user input
def menu():
    print("1.) Add a new task")  # Print option 1
    print("2.) View the list of tasks")  # Print option 2
    print("3.) Mark a task as completed")  # Print option 3
    print("4.) Remove a task")  # Print option 4
    print("5.) Exit the program")  # Print option 5
    try:
        # Try to convert user input to an integer and return it
        return int(input("Enter your choice: "))  # Ask for user input and return as an integer
    except ValueError:
        # If conversion fails, print an error message and return None
        print("Invalid input. Please enter a number.")  # Print error message
        return None  # Return None if input is not valid

# Define a function to add a task to the list
def add_task(tasks):
    entered_task = input("Enter a task: ")  # Ask for user input
    tasks.append(entered_task)  # Add the task to the list

# Define a function to view the list of tasks
def view_tasks(tasks):
    if tasks:
        print("\nList of tasks:")  # Print heading if tasks exist
        for idx, task in enumerate(tasks, start=1):
            # Loop through tasks, print task number and task description
            print(f"{idx}.) {task}")
    else:
        print("\nNo tasks available.")  # Print if no tasks exist

# Define a function to mark a task as completed
def mark_task_as_completed(tasks):
    view_tasks(tasks)  # Show available tasks
    try:
        completed_marker = int(input("Select the task's number to mark as completed: "))  # Ask for user input
        if 1 <= completed_marker <= len(tasks):
            # Check if input is within valid range
            tasks[completed_marker - 1] += " (COMPLETED!)"  # Mark task as completed
        else:
            print("Invalid task number.")  # Print error message if input is not valid
    except ValueError:
        print("Invalid input. Please enter a number.")  # Print error message for non-integer input

# Define a function to remove a task from the list
def remove_task(tasks):
    view_tasks(tasks)  # Show available tasks
    try:
        task_remover = int(input("Select the task's number to remove: "))  # Ask for user input
        if 1 <= task_remover <= len(tasks):
            # Check if input is within valid range
            tasks.pop(task_remover - 1)  # Remove task from the list
        else:
            print("Invalid task number.")  # Print error message if input is not valid
    except ValueError:
        print("Invalid input. Please enter a number.")  # Print error message for non-integer input

# Define the main function that orchestrates the program flow
def main():
    tasks = []  # Initialize an empty list to store tasks

    while True:  # Start an infinite loop
        menu_option = menu()  # Call the 'menu' function and get user choice

        if menu_option == 1:
            add_task(tasks)  # If user chooses option 1, call 'add_task' function
        elif menu_option == 2:
            view_tasks(tasks)  # If user chooses option 2, call 'view_tasks' function
        elif menu_option == 3:
            mark_task_as_completed(tasks)  # If user chooses option 3, call 'mark_task_as_completed' function
        elif menu_option == 4:
            remove_task(tasks)  # If user chooses option 4, call 'remove_task' function
        elif menu_option == 5:
            break  # Exit the loop if user chooses option 5

if __name__ == "__main__":
    main()  # Start the program by calling the main function