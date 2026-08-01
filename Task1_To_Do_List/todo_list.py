#to_do_list_python
#TASK1

tasks = []
while True:
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Quit task")
    choice = input("Enter your choice:")
    if choice == 1:
        newtask = input("Enter task:")
        tasks.append(newtask)
    elif choice == "2":
        removetask = input("Enter task to remove:")
        if removetask in tasks:
            tasks.remove(removetask)
            print("Task removed successfully.")
        else:
            print("Task not found.")
    elif choice == "3":
        print("Tasks:")
        for t in tasks:
            print("-",t)
    elif choice=="4":
        break
    else:
        print("invalid")