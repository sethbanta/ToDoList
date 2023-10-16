#Author Seth Banta
import json

#Define variables for use
taskList = []
priorities = []
dueDates = []
titles = []
going = 1
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
            for task in taskList:
                print(task)
        case "u":
            update()
        case "d":
            delete()
        case "s":
            sort()
        case _:
           saveQuestion = input("Save task list? (y/n) ")
           match saveQuestion:
                case "y":
                   print("Saving changes...")
                   exportTasks()
                   exit()
                case _:
                   print("Exiting without saving...")
                   exit()
                   
    
#create tasks
def create():
    #prompt user for task details
    inputTitle = input("Please enter a task title: ")
    inputDescription = input("Please enter a description: ")
    inputPriority = input("Please enter a priority (1-5, 1 being highest, 5 being lowest): ")
    inputDueDate = input("Please enter a due date (MM/DD/YY): ")
    #check if the input is how we want
    check(inputTitle, inputPriority, inputDueDate)
    #create the task and put it in a task list, a priority list, and a due date list for sorting later
    task = Task(inputTitle, inputDescription, inputPriority, inputDueDate)
    taskList.append(task)
    deez = int(task.priority)
    priorities.append(deez)
    month = task.due_date[0:2]
    day = task.due_date[3:5]
    year = task.due_date[6:8]
    titles.append(inputTitle)
    splitDate = f"{year}{month}{day}"
    splitDate = int(splitDate)
    dueDates.append(splitDate)

def createFromFile(title, desc, priority, dueDate):
    #check if the input is how we want
    check(title, priority, dueDate)
    #create the task and put it in a task list, a priority list, and a due date list for sorting later
    task = Task(title, desc, priority, dueDate)
    taskList.append(task)
    deez = int(task.priority)
    priorities.append(deez)
    month = task.due_date[0:2]
    day = task.due_date[3:5]
    year = task.due_date[6:8]
    titles.append(title)
    splitDate = f"{year}{month}{day}"
    splitDate = int(splitDate)
    dueDates.append(splitDate)
            
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
            priorities[index] = int(updatePriority)
            month = updateDueDate[0:2]
            day = updateDueDate[3:5]
            year = updateDueDate[6:8]
            splitDate = f"{year}{month}{day}"
            splitDate = int(splitDate)
            dueDates[index] = splitDate
            titles[index] = updateTitle
    except:
        print("Task not found")
        
#delete tasks
def delete():
    toDelete = input("Please enter the name of the task you would like to delete: ")
    if(toDelete == None or toDelete == ""):
        print("Invalid task provided, returning to menu")
    else:
        for task in taskList:
            if(task.title == toDelete):
                taskList.remove(task)
                print(f"Deleted {toDelete}")
                
        
#sort by priority: low to high
def lowSort():
    #start at index 0
    i = 0
    j = len(priorities)
    for priority in range(i,j):
        shrunkPriorities = priorities[i:j]
        maxPriority = 0
        #grab max priority in the shrunk(recursive) priority list 
        maxPriority = max(shrunkPriorities)
        maxPriorityIndex = shrunkPriorities.index(maxPriority) + i
        #grab current indexes task data
        oldTask = taskList[i]
        oldPriority = priorities[i]
        oldDate = dueDates[i]
        oldTitle = titles[i]
        #swap the indexes
        taskList[i] = taskList[maxPriorityIndex]
        taskList[maxPriorityIndex] = oldTask
        priorities[i] = priorities[maxPriorityIndex]
        priorities[maxPriorityIndex] = oldPriority
        dueDates[i] = dueDates[maxPriorityIndex]
        dueDates[maxPriorityIndex] = oldDate
        titles[i] = titles[maxPriorityIndex]
        titles[maxPriorityIndex] = oldTitle
        i = i+1
    print("Sorted high to low priority")

#sory by priority: high to low
def highSort():
    #start at index 0
    i = 0
    j = len(priorities)
    for priority in range(i,j):
        shrunkPriorities = priorities[i:j]
        minPriority = 0
        #grab min priority in the shrunk(recursive) priority list 
        minPriority = min(shrunkPriorities)
        minPriorityIndex = shrunkPriorities.index(minPriority) + i
        #grab current indexes task data
        oldTask = taskList[i]
        oldPriority = priorities[i]
        oldDate = dueDates[i]
        oldTitle = titles[i]
        #swap the indexes
        taskList[i] = taskList[minPriorityIndex]
        taskList[minPriorityIndex] = oldTask
        priorities[i] = priorities[minPriorityIndex]
        priorities[minPriorityIndex] = oldPriority
        dueDates[i] = dueDates[minPriorityIndex]
        dueDates[minPriorityIndex] = oldDate
        titles[i] = titles[minPriorityIndex]
        titles[minPriorityIndex] = oldTitle
        i = i+1
    print("Sorted low to high priority")

#sort by due date: closest to furthest
def closeSort():
    #start at index 0
    i = 0
    j = len(dueDates)
    for dueDate in range(i,j):
        #create recursive array
        shrunkDates = dueDates[i:j]
        minDate = 0
        #grab "lowest" date, this should be the soonest
        minDate = min(shrunkDates)
        minDateIndex = shrunkDates.index(minDate) + i
        #grab current indexes data
        oldTask = taskList[i]
        oldPriority = priorities[i]
        oldDate = dueDates[i]
        oldTitle = titles[i]
        #swap the indexes
        taskList[i] = taskList[minDateIndex]
        taskList[minDateIndex] = oldTask
        priorities[i] = priorities[minDateIndex]
        priorities[minDateIndex] = oldPriority
        dueDates[i] = dueDates[minDateIndex]
        dueDates[minDateIndex] = oldDate
        titles[i] = titles[minDateIndex]
        titles[minDateIndex] = oldTitle
        i = i+1
    print("Sorted by soonest to oldest due date")

#sort by due date: furthest to closest
def farSort():
    #start at index 0
    i = 0
    j = len(dueDates)
    for dueDate in range(i,j):
        #create recursive array
        shrunkDates = dueDates[i:j]
        maxDate = 0
        #grab "highest" date, this should be the furthest
        maxDate = max(shrunkDates)
        maxDateIndex = shrunkDates.index(maxDate) + i
        #grab current indexes data
        oldTask = taskList[i]
        oldPriority = priorities[i]
        oldDate = dueDates[i]
        oldTitle = titles[i]
        #swap the indexes
        taskList[i] = taskList[maxDateIndex]
        taskList[maxDateIndex] = oldTask
        priorities[i] = priorities[maxDateIndex]
        priorities[maxDateIndex] = oldPriority
        dueDates[i] = dueDates[maxDateIndex]
        dueDates[maxDateIndex] = oldDate
        titles[i] = titles[maxDateIndex]
        titles[maxDateIndex] = oldTitle
        i = i+1
    print("Sorted by oldest to soonest due date")

#sort by title alphabetically
def titleSort():
    #start at index 0
    i = 0
    j = len(titles)
    for title in range(i,j):
        shrunkTitles = titles[i:j]
        minTitle = 0
        #grab min title in the shrunk(recursive) title list 
        minTitle = min(shrunkTitles)
        minTitleIndex = shrunkTitles.index(minTitle) + i
        #grab current indexes task data
        oldTask = taskList[i]
        oldPriority = priorities[i]
        oldDate = dueDates[i]
        oldTitle = titles[i]
        #swap the indexes
        taskList[i] = taskList[minTitleIndex]
        taskList[minTitleIndex] = oldTask
        priorities[i] = priorities[minTitleIndex]
        priorities[minTitleIndex] = oldPriority
        dueDates[i] = dueDates[minTitleIndex]
        dueDates[minTitleIndex] = oldDate
        titles[i] = titles[minTitleIndex]
        titles[minTitleIndex] = oldTitle
        i = i+1
    print("Sorted alphabetically")

#save tasks to file
def exportTasks():
    #begin writing to a string for JSON format
    outputStr = "{\n"
    outputStr += "\t\"tasks\": [\n"
    #for every task in the task list, append it onto the string
    for task in taskList:
        outputStr += "\t\t{\n"
        outputStr += f"\t\t\t\"title\":\"{task.title}\",\n"
        outputStr += f"\t\t\t\"description\":\"{task.description}\",\n"
        outputStr += f"\t\t\t\"priority\":\"{task.priority}\",\n"
        outputStr += f"\t\t\t\"due date\":\"{task.due_date}\"\n"
        outputStr += "\t\t},\n"
    #turn the output string into a list so we can replace the comma on the last closing curly bracket
    outputStrList = list(outputStr)
    #grab the length of the string, then subtract by two so that we remove the comma, instead of the new line character
    strLen = len(outputStrList)
    outputStrList[strLen - 2] = ""
    #join the list into an empty string so we can export
    outputStr = "".join(outputStrList)
    outputStr += "\t]\n"
    outputStr += "}"
    #writes output string to a file name SavedTasks.json, if one doesn't already exist it will be created
    with open("SavedTasks.json", "w") as outfile:
            outfile.write(outputStr)

#import tasks from file
def importTasks():
    try:
        #open out saved tasks file if it exists
        file = open('SavedTasks.json')
        taskList.clear()
        priorities.clear()
        dueDates.clear()
        titles.clear()
        data = json.load(file)
        for i in data['tasks']:
            taskString = str(i)
            splitString = taskString.split('\'')
            taskTitle = splitString[3]
            taskDesc = splitString[7]
            taskPriority = splitString[11]
            taskDueDate = splitString[15]
            createFromFile(taskTitle, taskDesc, taskPriority, taskDueDate)
        file.close()
    except:
        print('')

#check function for checking values entered for a task
def check(inputTitle, inputPriority, inputDueDate):
    month = inputDueDate[0:2]
    day = inputDueDate[3:5]
    year = inputDueDate[6:8]
    #check if they entered stuff how we want
    #if the title is left blank, return to menu
    if(str(inputTitle) == None or str(inputTitle) == ""):
        print("No title found, returning to main menu")
    #if the priority is less than 1, or more than 5, go back to main menu
    elif((int(inputPriority) > 5 or int(inputPriority) < 1)):
        print("Invalid priority entered, returning to main menu")
    #if the month is less than 1 or greater than 12, or the day is greater than 31 or less than 1, or the year is sooner than 2023 return to main menu
    elif(int(month) > 12 or int(month) < 1 or int(day) > 31 or int(day) < 1 or int(year) < 23):
        print("Invalid due date entered, return to main menu")

#function to ask what kind of sorting the user wants to do
def sort():
    type = input("Sort by title, priority, or due date? (t/p/d) " )
    match type:
        case "t":
            titleSort()
        case "p":
            highLow = input("Sort by highest or lowest priority? (h/l) ")
            match highLow:
                case "h":
                    highSort()
                case "l":
                    lowSort()
                case _:
                    print("Invalid input")
                    sort()
        case "d":
            oldNew = input("Sort by oldest or newest tasks? (o/n) ")
            match oldNew:
                case "o":
                    farSort()
                case "n":
                    closeSort()
                case _:
                    print("Invalid input")
                    sort()
        case _:
            print("Invalid input")
            sort()

def getTitle(task):
    return task.title
#main code
#tasks for testing so i dont have to type them over and over
createFromFile("title", "desc", 2, "10/10/23")
createFromFile("second", "task", 3, "10/11/23")
createFromFile("third", "task", 1, "10/12/23")
createFromFile("fourth", "task", 5, "10/13/23")
createFromFile("fifth", "task", 4, "10/14/23")
importTasks()
while (going):
    prompt()