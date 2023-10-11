#Author Seth Banta

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
choice = input('Would you like to create, read, update, delete, sort or exit? (c/r/u/d/s/e)? ')
match choice:
    case "c":
        print('create selected')
    case "r":
        print('read selected')
    case "u":
        print('update selected')
    case "d":
        print('delete selected')
    case "s":
        print('sort selected')
    case _:
        print('exit selected')
    
#create tasks

#read tasks

#update tasks

#delete tasks

#sort by priority: high, low

#sort by due date: closest, furthest

#sort by title alphabetically

#save tasks to file

#import tasks from file