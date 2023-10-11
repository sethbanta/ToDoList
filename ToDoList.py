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
        
#create tasks

#read tasks

#update tasks

#delete tasks

#sort by priority: high, low

#sort by due date: closest, furthest

#sort by title alphabetically

#save tasks to file

#import tasks from file