#Author Seth Banta

#Define variables for use
taskList = []
#Define task object
class Task:
    def __init__(self, title, description, priority, due_date):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        
    def __str__(self):
        return f"{self.title}, {self.description}, {self.priority}, {self.due_date}"

#prompt user for input on what they want to do
def prompt():
    choice = input('Would you like to create, read, update, delete, sort or exit? (c/r/u/d/s/e)? ')
    match choice:
        case "c":
            create()
        case "r":
            read()
        case "u":
            update()
        case "d":
            delete()
        case "s":
            print('sort selected')
        case _:
           print('exit selected')
    
#create tasks
def create():
    #prompt user for task details
    inputTitle = input("Please enter a task title: ")
    inputDescription = input("Please enter a description: ")
    inputPriority = input("Please enter a priority (1-5, 1 being highest, 5 being lowest): ")
    inputDueDate = input("Please enter a due date (MM/DD/YY): ")
    check(inputTitle, inputPriority, inputDueDate)
    task = Task(inputTitle, inputDescription, inputPriority, inputDueDate)
    taskList.append(task)
    prompt()
    
#read tasks
def read():
    choice = input("Would you like to print all, or in a sorted format? (p/s) ")
    match choice:
        case "p":
            for task in taskList:
                print(task)
            prompt()
        case "s":
            sort = input("Sort by title, priority, or due date? (t/p/d)" )
            match sort:
                case "t":
                    print("Sort by title")
                case "p":
                    highLow = input("Sort by highest or lowest priority? (h/l) ")
                    match highLow:
                        case "h":
                            print("Sort by high")
                        case "l":
                            print("Sort by low")
                        case _:
                            print("Invalid input")
                            read()
                case "d":
                    oldNew = input("Sort by oldest or newest tasks? (o/n) ")
                    match oldNew:
                        case "o":
                            print("Sort by oldest")
                        case "n":
                            print("Sort by newest")
                        case _:
                            print("Invalid input")
                            read()
                case _:
                    print("Invalid input")
                    read()
        case _:
            print("Invalid input")
            read()
            
#update tasks
def update():
    taskToUpdate = input("Please enter the title of the task you would like to update: ")
    try:
        index = None
        for task in taskList:
            if(task.title == taskToUpdate):
                index = taskList.index(task)
        if(index != None):
            updateTitle = input("Please enter a task title: ")
            updateDescription = input("Please enter a description: ")
            updatePriority = input("Please enter a priority (1-5, 1 being highest, 5 being lowest): ")
            updateDueDate = input("Please enter a due date (MM/DD/YY): ")
            check(updateTitle, updatePriority, updateDueDate)
            updatedTask = Task(updateTitle, updateDescription, updatePriority, updateDueDate)
            taskList[index] = updatedTask
            prompt()
    except:
        print("Task not found")
        prompt()
        
#delete tasks
def delete():
    toDelete = input("Please enter the name of the task you would like to delete: ")
    if(toDelete == None or toDelete == ""):
        print("Invalid task provided, returning to menu")
        prompt()
        return
    else:
        for task in taskList:
            if(task.title == toDelete):
                taskList.remove(task)
                print(f"Deleted {toDelete}")
                prompt()
                return
        print("Task not found, returning to main menu")
        prompt()
        return
                
        
#sort by priority: high, low

#sort by due date: closest, furthest

#sort by title alphabetically

#save tasks to file

#import tasks from file

#check function for checking values entered for a task
def check(inputTitle, inputPriority, inputDueDate):
    month = inputDueDate[0:2]
    day = inputDueDate[3:5]
    year = inputDueDate[6:8]
    #check if they entered stuff how we want
    #if the title is left blank, return to menu
    if(str(inputTitle) == None or str(inputTitle) == ""):
        print("No title found, returning to main menu")
        prompt()
        return   
    #if the priority is less than 1, or more than 5, go back to main menu
    elif((int(inputPriority) > 5 or int(inputPriority) < 1)):
        print("Invalid priority entered, returning to main menu")
        prompt()
        return
    #if the month is less than 1 or greater than 12, or the day is greater than 31 or less than 1, or the year is sooner than 2023 return to main menu
    elif(int(month) > 12 or int(month) < 1 or int(day) > 31 or int(day) < 1 or int(year) < 23):
        print("Invalid due date entered, return to main menu")
        prompt()
        return

#main code
prompt()