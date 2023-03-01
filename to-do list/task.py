# To-do List
# Create separate files for each class, as shown above. You are tasked to create two classes: a Task class and a Section class.
# The Task class should receive a name (string) and a due_date (str) upon initialization. A task also has two attributes: comments (empty list) and completed set to False by default.
# The Task class should also have five additional methods:
# -	change_name(new_name: str)
# o	Changes the name of the task and returns the new name.
# o	If the new name is the same as the current name, returns "Name cannot be the same."
# -	change_due_date(new_date: str) 
# o	Changes the due date of the task and returns the new date.
# o	If the new date is the same as the current date, returns "Date cannot be the same."
# -	add_comment(comment: str)
# o	Adds a comment to the task.
# -	edit_comment(comment_number: int, new_comment: str)
# o	The comment number value represents the index of the comment we want to edit. The method should change the comment and return all the comments, separated by comma and space (", ")
# o	If the comment number is out of range, returns "Cannot find comment."
# -	details()
# o	Returns the task's details in this format:
# "Name: {task_name} - Due Date: {due_date}"
# The Section class should receive a name (string) upon initialization. The task also has one instance attribute: tasks (empty list)
# The Section class should also have four methods:
# -	add_task(new_task: Task)
# o	Adds a new task to the collection and returns "Task {task details} is added to the section"
# o	If the task is already in the collection, returns "Task is already in the section {section_name}"
# -	complete_task(task_name: str) 
# o	Changes the task to completed (True) and returns "Completed task {task_name}"
# o	If the task is not found, returns "Could not find task with the name {task_name}"
# -	clean_section()
# o	Removes all the completed tasks and returns "Cleared {amount of removed tasks} tasks."
# -	view_section()
# o	Returns information about the section and its tasks in this format:
#     "Section {section_name}:
#      {details of the first task}
#      {details of the second task}
#      …
#      {details of the n task}"


class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name):
        if self.name == new_name:
            return "Name cannot be the same."
        self.name = new_name
        return new_name

    def change_due_date(self, new_date):
        if self.due_date == new_date:
            return "Date cannot be the same."
        self.due_date = new_date
        return new_date

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, comment_number, new_comment):
        if comment_number in range(len(self.comments)):
            self.comments[comment_number] = new_comment
            return ", ".join(self.comments)
        return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"