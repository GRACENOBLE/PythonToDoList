todos = ["Go to school","See movie","Do nothing","Sing song"]

while True:
    
    def printTodos():
        print("Your todos are:")
        for index, item in enumerate(todos):
            print(f"{index + 1} {item}")

    def addTask():
        added = str(input("Please input a task to be added"))
        todos.append(added)

    def removeTask():
        removed = str(input("Please type the name of the item you want to be removed"))
        if removed in todos:
            todos.remove(removed)
        else:
            print("Sorry, that item Isnt part of the array.")

    def chooseTask():
        choice = int(input("\n1.Add task\n2.Remove\n"))
        if choice == 1:
            addTask()
        elif choice == 2: 
            removeTask()
        else:
            print("That was an invalid choice, please try again!")
    
    printTodos()
    chooseTask()