list_of_tasks = []

remove = True
add = True

def addTask():
    task = input("Add a task: \n")
    list_of_tasks.append(task)
    print(f"Task '{task}' added to the list.")

def deleteTask(): 
    listTask()
    try:
        taskToDelete = int(input("Choose the # of the task you want to delete: "))
        if 0 <= taskToDelete < len(list_of_tasks):
            deleted_task = list_of_tasks.pop(taskToDelete)
            print(f"Task '{deleted_task}' has been deleted.")
        else:
            print(f"Task #{taskToDelete} was not found")
    except:
        print("Invalid input")

def listTask():
    if not list_of_tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(list_of_tasks):
            print(f"Task #{index}. {task}")

if __name__ == "__main__":
    print("Welcome to the To Do List App:")

    while add == True:
        print("\n")
        print("----------------------------------------------------------")
        print("Choose one of the following options\n")
        print("1. Add a Task")
        print("2. Delete a Task")
        print("3. List Tasks")
        print("4. Quit")

        choice = input("Enter your choice between 1,2,3 or 4\n")

        if (choice == "1"):
            addTask()
        elif (choice == "2"):
            deleteTask()
        elif (choice == "3"):
            listTask()
        elif (choice == "4"):
            break
        else:
            print("Invalid input. Please try again")

    print("Good Bye")

    

# First, I created a simple list to store tasks. This taught me how to use Python's basic data structures.

# I broke the program into three main functions:

# addTask() - adds items to my list
# deleteTask() - removes items
# listTask() - shows all tasks This taught me how to organize code logically.
# I built a menu system using a while loop and if/elif statements. I learned how to control program flow and create user interfaces.

# I added error handling with try/except blocks because I realized users might type wrong inputs. This taught me defensive programming.

# I learned about list operations like .append() and .pop() to manage my tasks.

# My biggest takeaways were:

# How to structure a complete program
# Working with user input/output
# Managing data in lists
# Handling errors
# Writing clean, organized code
# This project was perfect for me as a beginner because it used real-world concepts and taught me fundamental programming skills. I can now build on this by adding features like saving to files or adding due dates.